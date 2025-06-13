"""
Go/No-Go Checker Tool
Evaluates tasks and decisions using structured criteria
"""
from typing import Dict, Any, List
from datetime import datetime


class GoNoGoChecker:
    """Evaluates decisions and tasks against go/no-go criteria"""

    def __init__(self):
        self.evaluation_history = []

    def evaluate_task(self,
                      task_config: Dict[str, Any],
                      context: Dict[str, Any] = None) -> bool:
        """Evaluate a task against go/no-go criteria"""
        print(f"🔍 Evaluating task: {task_config.get('name', 'Unknown')}")

        criteria_checks = {
            "has_clear_objectives":
            self._check_clear_objectives(task_config),
            "resources_available":
            self._check_resources(task_config, context or {}),
            "aligned_with_priorities":
            self._check_priority_alignment(task_config),
            "proper_preparation":
            self._check_preparation(task_config, context or {}),
            "success_criteria_defined":
            self._check_success_criteria(task_config)
        }

        if task_config.get('priority') == 'high':
            criteria_checks[
                "risk_assessment_complete"] = self._check_risk_assessment(
                    task_config)
            criteria_checks[
                "stakeholder_alignment"] = self._check_stakeholder_alignment(
                    task_config)

        passed_criteria = sum(1 for check in criteria_checks.values() if check)
        total_criteria = len(criteria_checks)
        threshold = int(total_criteria * 0.8)
        go_decision = passed_criteria >= threshold

        evaluation = {
            "timestamp": datetime.now().isoformat(),
            "task": task_config.get('name', 'Unknown'),
            "criteria_checks": criteria_checks,
            "passed_criteria": passed_criteria,
            "total_criteria": total_criteria,
            "decision": "GO" if go_decision else "NO-GO",
            "context": context or {}
        }
        self.evaluation_history.append(evaluation)

        if go_decision:
            print(
                f"    ✅ GO: {passed_criteria}/{total_criteria} criteria passed"
            )
        else:
            print(
                f"    ❌ NO-GO: Only {passed_criteria}/{total_criteria} criteria passed"
            )
            print(
                f"    Failed criteria: {', '.join(k for k, v in criteria_checks.items() if not v)}"
            )

        return go_decision

    def evaluate_protocol(self, protocol: 'ProtocolDocument',
                          context: Dict[str, Any]) -> bool:
        """Evaluate a protocol against its go/no-go criteria"""
        print(f"🔍 Evaluating protocol: {protocol.name}")
        criteria = protocol.go_no_go_criteria
        all_passed = True

        for criterion, required_value in criteria.items():
            if criterion in context:
                actual_value = context[criterion]
                if actual_value != required_value:
                    print(
                        f"    ❌ Criterion failed: {criterion} = {actual_value}, required = {required_value}"
                    )
                    all_passed = False
                else:
                    print(
                        f"    ✅ Criterion passed: {criterion} = {actual_value}"
                    )
            else:
                print(f"    ⚠️ Missing context for criterion: {criterion}")
                all_passed = False

        evaluation = {
            "timestamp": datetime.now().isoformat(),
            "protocol": protocol.name,
            "criteria_checks": {
                criterion:
                criterion in context and context[criterion] == required_value
                for criterion, required_value in criteria.items()
            },
            "decision": "GO" if all_passed else "NO-GO",
            "context": context
        }
        self.evaluation_history.append(evaluation)

        return all_passed

    def _check_clear_objectives(self, task_config: Dict[str, Any]) -> bool:
        return bool(task_config.get('description'))

    def _check_resources(self, task_config: Dict[str, Any],
                         context: Dict[str, Any]) -> bool:
        required_inputs = task_config.get('inputs', [])
        if not required_inputs:
            return True
        available_resources = context.get('available_resources', [])
        return all(resource in available_resources
                   for resource in required_inputs)

    def _check_priority_alignment(self, task_config: Dict[str, Any]) -> bool:
        priority = task_config.get('priority', 'low')
        return priority in ['high', 'medium']

    def _check_preparation(self, task_config: Dict[str, Any],
                           context: Dict[str, Any]) -> bool:
        return context.get(
            'planning_complete',
            False) or task_config.get('frequency') == 'continuous'

    def _check_success_criteria(self, task_config: Dict[str, Any]) -> bool:
        return bool(task_config.get('success_criteria', {}))

    def _check_risk_assessment(self, task_config: Dict[str, Any]) -> bool:
        return True

    def _check_stakeholder_alignment(self, task_config: Dict[str,
                                                             Any]) -> bool:
        return True

    def get_evaluation_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        return self.evaluation_history[-limit:]

    def generate_go_no_go_report(self) -> Dict[str, Any]:
        if not self.evaluation_history:
            return {"message": "No evaluations completed yet"}

        recent_evaluations = self.evaluation_history[-20:]
        go_decisions = sum(1 for eval in recent_evaluations
                           if eval['decision'] == 'GO')
        no_go_decisions = len(recent_evaluations) - go_decisions
        common_failures = {}
        for eval in recent_evaluations:
            if eval['decision'] == 'NO-GO':
                for criterion, passed in eval.get('criteria_checks',
                                                  {}).items():
                    if not passed:
                        common_failures[criterion] = common_failures.get(
                            criterion, 0) + 1

        return {
            "total_evaluations":
            len(recent_evaluations),
            "go_decisions":
            go_decisions,
            "no_go_decisions":
            no_go_decisions,
            "success_rate":
            go_decisions /
            len(recent_evaluations) if recent_evaluations else 0,
            "common_failure_points":
            dict(
                sorted(common_failures.items(),
                       key=lambda x: x[1],
                       reverse=True)),
            "last_evaluation":
            recent_evaluations[-1] if recent_evaluations else None
        }
