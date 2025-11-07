import json
import ollama
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_with_model(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)
        prompt = data.get("prompt", "")
        if not prompt:
            return JsonResponse({"error": "Prompt required"}, status=400)

        response = ollama.chat(
            model="Phi-3-mini-4k-instruct-q4_2.gguf",
            messages=[{"role": "user", "content": prompt}],
        )

        return JsonResponse(
            {"response": response["message"]["content"]},
            json_dumps_params={'ensure_ascii': False}
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
