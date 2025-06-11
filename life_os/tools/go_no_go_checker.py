
"""
Go/No-Go Checker Tool
Evaluates tasks and decisions using structured criteria
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

class GoNoGoChecker:
    """Evaluates decisions and tasks against go/no-go criteria"""
    
    def __init__(self):
        self.evaluation_history = []
    
    def evaluate_task(self, task_config: Dict[str, Any], context: Dict[str, Any] = None) -> bool:
        """Evaluate a task against go/no-go criteria"""
        print(f"🔍 Evaluating task: {task_config.get('name', 'Unknown')}")
        
        # Core go/no-go criteria
        criteria_checks = {
            "has_clear_objectives": self._check_clear_objectives(task_config),
            "resources_available": self._check_resources(task_config, context or {}),
            "aligned_with_priorities": self._check_priority_alignment(task_config),
            "proper_preparation": self._check_preparation(task_config, context or {}),
            "success_criteria_defined": self._check_success_criteria(task_config)
        }
        
        # Additional checks for high-priority tasks
        if task_config.get('priority') == 'high':
            criteria_checks["risk_assessment_complete"] = self._check_risk_assessment(task_config)
            criteria_checks["stakeholder_alignment"] = self._check_stakeholder_alignment(task_config)
        
        # Evaluate all criteria
        passed_criteria = sum(1 for check in criteria_checks.values() if check)
        total_criteria = len(criteria_checks)
        
        # Require 80% of criteria to pass
        threshold = int(total_criteria * 0.8)
        go_decision = passed_criteria >= threshold
        
        # Log evaluation
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
            print(f"    ✅ GO: {passed_criteria}/{total_criteria} criteria passed")
        else:
            print(f"    ❌ NO-GO: Only {passed_criteria}/{total_criteria} criteria passed")
            failed_criteria = [k for k, v in criteria_checks.items() if not v]
            print(f"    Failed criteria: {', '.join(failed_criteria)}")
        
        return go_decision
    
    def evaluate_protocol(self, protocol_config: Dict[str, Any], context: Dict[str, Any]) -> bool:
        """Evaluate a protocol against its specific go/no-go criteria"""
        if 'go_no_go_criteria' not in protocol_config:
            return True  # Default to go if no criteria specified
        
        criteria = protocol_config['go_no_go_criteria']
        all_passed = True
        
        for criterion, required_value in criteria.items():
            if criterion in context:
                actual_value = context[criterion]
                if actual_value != required_value:
                    print(f"    ❌ Criterion failed: {criterion} = {actual_value}, required = {required_value}")
                    all_passed = False
                else:
                    print(f"    ✅ Criterion passed: {criterion} = {actual_value}")
            else:
                print(f"    ⚠️  Missing context for criterion: {criterion}")
                all_passed = False
        
        return all_passed
    
    def _check_clear_objectives(self, task_config: Dict[str, Any]) -> bool:
        """Check if task has clear, measurable objectives"""
        return bool(
            task_config.get('description') and
            (task_config.get('outputs') or task_config.get('success_criteria'))
        )
    
    def _check_resources(self, task_config: Dict[str, Any], context: Dict[str, Any]) -> bool:
        """Check if necessary resources are available"""
        required_inputs = task_config.get('inputs', [])
        if not required_inputs:
            return True  # No specific resource requirements
        
        # Check if required inputs are available in context
        available_resources = context.get('available_resources', [])
        return all(resource in available_resources for resource in required_inputs)
    
    def _check_priority_alignment(self, task_config: Dict[str, Any]) -> bool:
        """Check if task aligns with current priorities"""
        # High and medium priority tasks are generally aligned
        priority = task_config.get('priority', 'low')
        return priority in ['high', 'medium']
    
    def _check_preparation(self, task_config: Dict[str, Any], context: Dict[str, Any]) -> bool:
        """Check if proper preparation has been done"""
        # For now, assume preparation is adequate if planning phase is complete
        return context.get('planning_complete', False) or task_config.get('frequency') == 'continuous'
    
    def _check_success_criteria(self, task_config: Dict[str, Any]) -> bool:
        """Check if success criteria are well-defined"""
        return bool(task_config.get('success_criteria'))
    
    def _check_risk_assessment(self, task_config: Dict[str, Any]) -> bool:
        """Check if risk assessment has been completed for high-priority tasks"""
        # This would integrate with a risk assessment system
        return True  # Placeholder for now
    
    def _check_stakeholder_alignment(self, task_config: Dict[str, Any]) -> bool:
        """Check if relevant stakeholders are aligned"""
        # This would check stakeholder approval for significant tasks
        return True  # Placeholder for now
    
    def get_evaluation_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent evaluation history"""
        return self.evaluation_history[-limit:]
    
    def generate_go_no_go_report(self) -> Dict[str, Any]:
        """Generate a summary report of recent go/no-go decisions"""
        if not self.evaluation_history:
            return {"message": "No evaluations completed yet"}
        
        recent_evaluations = self.evaluation_history[-20:]  # Last 20 evaluations
        
        go_decisions = sum(1 for eval in recent_evaluations if eval['decision'] == 'GO')
        no_go_decisions = len(recent_evaluations) - go_decisions
        
        common_failures = {}
        for eval in recent_evaluations:
            if eval['decision'] == 'NO-GO':
                for criterion, passed in eval['criteria_checks'].items():
                    if not passed:
                        common_failures[criterion] = common_failures.get(criterion, 0) + 1
        
        return {
            "total_evaluations": len(recent_evaluations),
            "go_decisions": go_decisions,
            "no_go_decisions": no_go_decisions,
            "success_rate": go_decisions / len(recent_evaluations) if recent_evaluations else 0,
            "common_failure_points": dict(sorted(common_failures.items(), key=lambda x: x[1], reverse=True)),
            "last_evaluation": recent_evaluations[-1] if recent_evaluations else None
        }

class GoNoGoChecker:
    """Tool for making go/no-go decisions based on multiple criteria"""
    
    def __init__(self):
        self.evaluation_criteria = {
            'impact': {'weight': 0.3, 'threshold': 3.0},
            'feasibility': {'weight': 0.25, 'threshold': 3.0},
            'alignment': {'weight': 0.2, 'threshold': 3.0},
            'resources': {'weight': 0.15, 'threshold': 3.0},
            'timing': {'weight': 0.1, 'threshold': 3.0}
        }
        
    def evaluate_task(self, task_config: Dict[str, Any]) -> bool:
        """
        Evaluate a task configuration and return go/no-go decision
        
        Args:
            task_config: Dictionary containing task configuration
            
        Returns:
            bool: True for go, False for no-go
        """
        if not task_config:
            return False
            
        # Extract evaluation metrics from task config
        scores = self._calculate_scores(task_config)
        
        # Calculate weighted score
        weighted_score = self._calculate_weighted_score(scores)
        
        # Make decision based on threshold
        decision = self._make_decision(weighted_score, scores)
        
        # Log decision for transparency
        self._log_decision(task_config.get('name', 'Unknown Task'), scores, weighted_score, decision)
        
        return decision
    
    def _calculate_scores(self, task_config: Dict[str, Any]) -> Dict[str, float]:
        """Calculate individual criterion scores"""
        scores = {}
        
        # Impact score (1-5): How much value does this create?
        priority = task_config.get('priority', 'medium')
        impact_map = {'low': 2.0, 'medium': 3.5, 'high': 5.0}
        scores['impact'] = impact_map.get(priority, 3.0)
        
        # Feasibility score (1-5): How achievable is this?
        # Based on complexity and resource requirements
        frequency = task_config.get('frequency', 'daily')
        feasibility_map = {'continuous': 3.0, 'daily': 4.0, 'weekly': 4.5, 'monthly': 5.0}
        scores['feasibility'] = feasibility_map.get(frequency, 3.5)
        
        # Alignment score (1-5): How well does this align with goals?
        success_criteria = task_config.get('success_criteria', {})
        scores['alignment'] = 4.0 if success_criteria else 2.0
        
        # Resources score (1-5): Do we have what we need?
        inputs = task_config.get('inputs', [])
        outputs = task_config.get('outputs', [])
        if inputs and outputs:
            scores['resources'] = 4.0
        elif inputs or outputs:
            scores['resources'] = 3.0
        else:
            scores['resources'] = 2.0
            
        # Timing score (1-5): Is this the right time?
        assigned_agent = task_config.get('assigned_agent')
        scores['timing'] = 4.0 if assigned_agent else 3.0
        
        return scores
    
    def _calculate_weighted_score(self, scores: Dict[str, float]) -> float:
        """Calculate weighted average score"""
        weighted_sum = 0.0
        total_weight = 0.0
        
        for criterion, score in scores.items():
            if criterion in self.evaluation_criteria:
                weight = self.evaluation_criteria[criterion]['weight']
                weighted_sum += score * weight
                total_weight += weight
                
        return weighted_sum / total_weight if total_weight > 0 else 0.0
    
    def _make_decision(self, weighted_score: float, individual_scores: Dict[str, float]) -> bool:
        """Make final go/no-go decision"""
        # Check if weighted score meets threshold
        if weighted_score < 3.0:
            return False
            
        # Check if any critical criterion fails
        for criterion, score in individual_scores.items():
            if criterion in self.evaluation_criteria:
                threshold = self.evaluation_criteria[criterion]['threshold']
                if score < threshold and criterion in ['feasibility', 'resources']:
                    return False
                    
        return True
    
    def _log_decision(self, task_name: str, scores: Dict[str, float], 
                     weighted_score: float, decision: bool):
        """Log decision details for transparency"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        decision_text = "GO" if decision else "NO-GO"
        
        print(f"\n🔍 Go/No-Go Decision for '{task_name}' at {timestamp}")
        print(f"   Overall Score: {weighted_score:.2f}/5.0")
        print(f"   Decision: {decision_text}")
        print("   Individual Scores:")
        for criterion, score in scores.items():
            print(f"     {criterion.title()}: {score:.1f}/5.0")
    
    def update_criteria(self, new_criteria: Dict[str, Dict[str, float]]):
        """Update evaluation criteria and weights"""
        self.evaluation_criteria.update(new_criteria)
        
    def get_decision_summary(self, task_configs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate summary of decisions for multiple tasks"""
        summary = {
            'total_tasks': len(task_configs),
            'go_decisions': 0,
            'no_go_decisions': 0,
            'average_score': 0.0,
            'decisions': []
        }
        
        total_score = 0.0
        
        for task_config in task_configs:
            decision = self.evaluate_task(task_config)
            scores = self._calculate_scores(task_config)
            weighted_score = self._calculate_weighted_score(scores)
            
            summary['decisions'].append({
                'task': task_config.get('name', 'Unknown'),
                'decision': decision,
                'score': weighted_score
            })
            
            if decision:
                summary['go_decisions'] += 1
            else:
                summary['no_go_decisions'] += 1
                
            total_score += weighted_score
        
        if summary['total_tasks'] > 0:
            summary['average_score'] = total_score / summary['total_tasks']
            
        return summary
