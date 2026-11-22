import random

def get_knowledge_base():
    """Simulates a reliable, factual knowledge base."""
    return {
        "apple_color": "red or green",
        "banana_shape": "curved",
        "orange_taste": "citrusy and sweet",
        "strawberry_seeds": "outside",
        "kiwi_origin": "China",
        "grape_growth": "bunches"
    }

def simulate_ai_response(query, knowledge_base, hallucination_chance=0.4):
    """
    Simulates an AI's response. It sometimes provides correct info
    but can 'hallucinate' (provide incorrect/fabricated info) for demonstration.
    """
    # Simulate AI attempting to answer from its 'training' (knowledge_base)
    if query in knowledge_base and random.random() > hallucination_chance:
        # AI gives a correct answer (no hallucination)
        return knowledge_base[query]
    else:
        # --- AI Hallucination Simulation ---
        # For queries it doesn't know or with a certain probability, it fabricates.
        if query == "apple_color":
            return "blue" # A plausible but incorrect hallucination
        elif query == "banana_shape":
            return "straight" # Another hallucination
        elif query == "orange_taste":
            return "spicy" # A less plausible but still hallucination
        elif query == "strawberry_seeds":
            return "inside" # Hallucination
        elif query == "kiwi_origin":
            return "New Zealand" # Common misconception, good for hallucination
        elif query == "mango_season":
            return "winter" # Fabricated answer for an unknown query
        else:
            return "I'm not sure, but I think it's a new type of fruit." # Generic fabrication

def verify_ai_response(query, ai_response, knowledge_base):
    """
    Demonstrates a defense method: verifying AI output against a trusted knowledge base.
    This helps detect 'hallucinations'.
    """
    if query in knowledge_base:
        correct_answer = knowledge_base[query]
        # Simple check: Is the correct answer (or part of it) present in the AI's response?
        if correct_answer.lower() in ai_response.lower():
            return True, "Response is consistent with the trusted knowledge base."
        else:
            return False, f"Response '{ai_response}' is inconsistent with known fact: '{correct_answer}'."
    else:
        # If the query itself is not in the knowledge base, direct verification is harder.
        # The AI might be speculating, which is a form of hallucination if presented as fact.
        return False, "Query not directly verifiable in knowledge base. AI might be speculating."

def run_example():
    kb = get_knowledge_base()
    queries = [
        "apple_color",
        "banana_shape",
        "orange_taste",
        "strawberry_seeds",
        "kiwi_origin",
        "grape_growth",
        "mango_season" # Query not directly in knowledge base
    ]

    print("--- Simulating AI Responses and Verification ---")
    for query in queries:
        print(f"\nQuery: What is the {query.replace('_', ' ')}?")
        ai_response = simulate_ai_response(query, kb) # AI generates a response
        print(f"AI Response: {ai_response}")

        # --- Defense Method: Verification against trusted source ---
        is_accurate, verification_message = verify_ai_response(query, ai_response, kb)
        if is_accurate:
            print(f"Verification: ✅ {verification_message}")
        else:
            print(f"Verification: ❌ {verification_message}")
            # If inconsistent, show what the correct answer should have been
            if query in kb:
                print(f"   (Correct answer for '{query}': {kb[query]})\n")
            else:
                print(f"   (No direct fact for '{query}' in KB. AI likely fabricated.)\n")

if __name__ == "__main__":
    run_example()
