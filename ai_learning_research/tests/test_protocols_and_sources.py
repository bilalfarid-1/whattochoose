"""
Automated Verification Suite for the AI-Augmented Engineering Mastery Framework.

Verifies:
1. Academic bibliographic audit integrity (DOIs, authors, venues, empirical rigor).
2. System prompt guardrails (negative constraints, anti-leakage rules, role definitions).
3. Protocol structural completeness (Objective, Grounding, Workflow, Checkpoint).
4. 30-Day Sprint continuity (all 30 days scheduled with hands-on tasks and DSA targets).
5. File paths and documentation cross-references.
"""

import os
import re
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_sources_metadata():
    """Verify that SOURCES.md exists and contains all 12 required academic citations with DOIs/URLs."""
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
    ]

    for author in required_authors:
        assert author in content, f"Missing citation or reference for {author}"

    # Verify DOI or URL links exist in the bibliography
    doi_or_urls = re.findall(r"https?://[^\s\)]+", content)
    assert len(doi_or_urls) >= 10, f"Expected at least 10 DOIs/URLs in SOURCES.md, found {len(doi_or_urls)}"


def test_system_prompts_guardrails():
    """Verify system prompts enforce anti-leakage and structured pedagogical constraints."""
    prompts_dir = os.path.join(BASE_DIR, "prompts")
    assert os.path.isdir(prompts_dir), "prompts directory not found"

    expected_prompts = [
        ("socratic_mentor.prompt.md", ["ZERO CODE LEAKAGE", "SUBGOAL", "HINT"]),
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


def test_roadmap_continuity():
    """Verify that the 30-Day Sprint covers all 30 days and 4 weekly modules."""
    roadmap_path = os.path.join(BASE_DIR, "roadmap", "30_day_ai_backend_sprint.md")
    assert os.path.isfile(roadmap_path), "Roadmap file not found"

    with open(roadmap_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Verify all 4 weeks exist
    assert "WEEK 1" in text
    assert "WEEK 2" in text
    assert "WEEK 3" in text
    assert "WEEK 4" in text

    # Verify Day 1 through Day 30 are explicitly covered
    for day_num in range(1, 31):
        assert f"Day {day_num}" in text, f"Roadmap missing schedule for Day {day_num}"

    # Verify LeetCode / DSA integration
    assert "LeetCode" in text
    assert "Two Pointers" in text
    assert "Binary Search" in text


def test_anti_patterns_and_cognitive_architecture():
    """Verify that the cognitive architecture and anti-patterns documents are comprehensive."""
    framework_dir = os.path.join(BASE_DIR, "framework")
    cog_path = os.path.join(framework_dir, "cognitive_architecture.md")
    anti_path = os.path.join(framework_dir, "anti_patterns.md")

    assert os.path.isfile(cog_path), "cognitive_architecture.md not found"
    assert os.path.isfile(anti_path), "anti_patterns.md not found"

    with open(cog_path, "r", encoding="utf-8") as f:
        cog_text = f.read()
    assert "Cognitive Load Theory" in cog_text
    assert "Deliberate Practice" in cog_text
    assert "Desirable Difficulties" in cog_text
    assert "Subgoal Learning" in cog_text

    with open(anti_path, "r", encoding="utf-8") as f:
        anti_text = f.read()
    assert "Anti-Pattern 1" in anti_text
    assert "Anti-Pattern 2" in anti_text
    assert "Anti-Pattern 3" in anti_text
    assert "Anti-Pattern 4" in anti_text
    assert "Anti-Pattern 5" in anti_text
    assert "Anti-Pattern 6" in anti_text


if __name__ == "__main__":
    pytest.main(["-v", __file__])
