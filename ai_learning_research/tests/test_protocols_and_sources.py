"""
Automated Verification Suite for the AI-Augmented Engineering Mastery Framework.

Verifies:
1. Academic bibliographic audit integrity (Corrected DOIs, authors, venues, empirical rigor).
2. Research-informed system prompt guardrails (graduated assistance, role definitions).
3. Protocol structural completeness (Objective, Grounding, Workflow, Checkpoint).
4. 30-Day Sprint continuity (4-metric scorecard, daily routine, JobPulse focus).
5. Clean repository references (zero absolute local disk paths in README).
"""

import os
import re
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_sources_metadata():
    """Verify that SOURCES.md exists and contains all required scholarly citations with verified DOIs/URLs."""
    sources_path = os.path.join(BASE_DIR, "SOURCES.md")
    assert os.path.isfile(sources_path), "SOURCES.md not found"

    with open(sources_path, "r", encoding="utf-8") as f:
        content = f.read()

    required_authors = [
        "Prather",
        "Mozannar",
        "Denny",
        "Kazemitabaar",
        "Mollick",
        "Margulieux",
        "Sweller",
        "Bjork",
        "Ericsson",
        "Roediger",
        "Chi",
        "Peng",
        "Cowan",
        "Maier",
    ]

    for author in required_authors:
        assert author in content, f"Missing citation or reference for {author}"

    # Verify specific verified DOIs and URLs
    verified_identifiers = [
        "10.1145/3632620.3671116",  # Prather et al. ICER 2024
        "10.1145/3613904.3641936",  # Mozannar et al. CHI 2024
        "10.1145/3613904.3642773",  # Kazemitabaar et al. (CodeAid) CHI 2024
        "10.1017/S0140525X01003922", # Cowan 2001
        "10.1037/edu0000108",        # Margulieux & Catrambone 2016
        "10.1111/j.1745-6916.2006.00012.x", # Roediger & Karpicke 2006
        "2605.04779",               # Maier et al. May 2026 meta-analysis
    ]

    for identifier in verified_identifiers:
        assert identifier in content, f"Verified identifier {identifier} missing in SOURCES.md"


def test_system_prompts_guardrails():
    """Verify system prompts enforce graduated assistance and structured pedagogical constraints."""
    prompts_dir = os.path.join(BASE_DIR, "prompts")
    assert os.path.isdir(prompts_dir), "prompts directory not found"

    expected_prompts = [
        ("socratic_mentor.prompt.md", ["GRADUATED ASSISTANCE", "SUBGOAL", "Tier 1"]),
        ("adversarial_tester.prompt.md", ["DO NOT FIX", "Vulnerability", "PyTest"]),
        ("architecture_challenger.prompt.md", ["COUNTER-ARGUMENT", "SCALE", "Trade-off"]),
        ("dsa_coach.prompt.md", ["NEVER WRITE", "PATTERN", "COMPLEXITY"]),
    ]

    for filename, required_phrases in expected_prompts:
        prompt_path = os.path.join(prompts_dir, filename)
        assert os.path.isfile(prompt_path), f"Prompt file {filename} not found"

        with open(prompt_path, "r", encoding="utf-8") as f:
            text = f.read()

        for phrase in required_phrases:
            assert phrase.lower() in text.lower(), f"Prompt {filename} missing required constraint: '{phrase}'"


def test_protocols_completeness():
    """Verify that all 4 learning protocols contain the required pedagogical sections."""
    protocols_dir = os.path.join(BASE_DIR, "protocols")
    assert os.path.isdir(protocols_dir), "protocols directory not found"

    expected_protocols = [
        "01_socratic_subgoal_decomposition.md",
        "02_adversarial_code_review.md",
        "03_active_recall_mutation_drills.md",
        "04_feynman_interrogation.md",
    ]

    required_sections = [
        "## 1. Objective",
        "## 2. Theoretical Grounding",
        "## 3.",
        "## 4. Verification Checkpoint",
    ]

    for filename in expected_protocols:
        proto_path = os.path.join(protocols_dir, filename)
        assert os.path.isfile(proto_path), f"Protocol {filename} not found"

        with open(proto_path, "r", encoding="utf-8") as f:
            text = f.read()

        for section in required_sections:
            assert section in text, f"Protocol {filename} missing structural section '{section}'"


def test_roadmap_continuity_and_scorecard():
    """Verify that the 30-Day Sprint covers the 4-metric scorecard, daily routine, and JobPulse training ground."""
    roadmap_path = os.path.join(BASE_DIR, "roadmap", "30_day_ai_backend_sprint.md")
    assert os.path.isfile(roadmap_path), "Roadmap file not found"

    with open(roadmap_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Verify all 4 weeks exist
    assert "WEEK 1" in text
    assert "WEEK 2" in text
    assert "WEEK 3" in text
    assert "WEEK 4" in text

    # Verify 4-metric learning scorecard
    assert "Independent Completion" in text
    assert "Debugging Ability" in text
    assert "Technical Explanation" in text
    assert "Conceptual Transfer" in text

    # Verify daily operating routine
    assert "120 minutes" in text
    assert "45 minutes" in text
    assert "35 minutes" in text
    assert "20 minutes" in text

    # Verify JobPulse focus
    assert "JobPulse" in text


def test_anti_patterns_and_cognitive_architecture():
    """Verify that the cognitive architecture and anti-patterns documents are comprehensive."""
    framework_dir = os.path.join(BASE_DIR, "framework")
    cog_path = os.path.join(framework_dir, "cognitive_architecture.md")
    anti_path = os.path.join(framework_dir, "anti_patterns.md")

    assert os.path.isfile(cog_path), "cognitive_architecture.md not found"
    assert os.path.isfile(anti_path), "anti_patterns.md not found"

    with open(cog_path, "r", encoding="utf-8") as f:
        cog_text = f.read()
    assert "Cowan" in cog_text
    assert "Sweller" in cog_text
    assert "Maier" in cog_text
    assert "Graduated Assistance" in cog_text

    with open(anti_path, "r", encoding="utf-8") as f:
        anti_text = f.read()
    assert "Anti-Pattern 1" in anti_text
    assert "Anti-Pattern 2" in anti_text
    assert "Anti-Pattern 3" in anti_text
    assert "Anti-Pattern 4" in anti_text
    assert "Anti-Pattern 5" in anti_text
    assert "Anti-Pattern 6" in anti_text


def test_no_local_disk_paths_in_readme():
    """Verify that ai_learning_research/README.md does not contain local absolute file:/// or C: paths."""
    readme_path = os.path.join(BASE_DIR, "README.md")
    assert os.path.isfile(readme_path), "README.md not found"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert "file:///" not in content, "README.md contains local file:/// URLs"
    assert "C:\\Users\\" not in content, "README.md contains local Windows disk paths"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
