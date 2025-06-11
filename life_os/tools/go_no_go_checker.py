
"""
Go/No-Go Checker Tool
Evaluates tasks and decisions using structured criteria
"""

from typing import Dict, Any, List
from datetime import datetime

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
