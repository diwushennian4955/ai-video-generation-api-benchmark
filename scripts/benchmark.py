"""
AI Video Generation API Benchmark 2026
Compare Sora 2, Veo 3, Runway Gen-4, and Kling AI via NexaAPI unified endpoint.

Usage: python benchmark.py --prompt "Your prompt here" --duration 5

Get your NexaAPI key at: https://nexa-api.com
pip install nexaapi  →  https://pypi.org/project/nexaapi/
"""

import argparse
import time
from nexaapi import NexaAPI

MODELS = [
    ('sora-2', 'OpenAI', 'Cinematic storytelling'),
    ('veo-3', 'Google', 'Realistic motion'),
    ('runway-gen4', 'Runway', 'Creative/artistic'),
    ('kling-v3-pro', 'Kling AI', 'High quality, competitive pricing'),
]

def run_benchmark(api_key: str, prompt: str, duration: int = 5):
    """Run the same prompt across all video models and compare results."""
    client = NexaAPI(api_key=api_key)
    
    print(f"\n{'='*60}")
    print(f"AI Video Generation Benchmark 2026")
    print(f"{'='*60}")
    print(f"Prompt: {prompt}")
    print(f"Duration: {duration}s | Aspect: 16:9")
    print(f"{'='*60}\n")
    
    results = []
    for model, provider, description in MODELS:
        print(f"Testing {model} ({provider}) — {description}...")
        start = time.time()
        try:
            response = client.video.generate(
                model=model,
                prompt=prompt,
                duration=duration,
                aspect_ratio='16:9',
                quality='cinematic'
            )
            elapsed = time.time() - start
            results.append({
                'model': model,
                'provider': provider,
                'url': response.video_url,
                'time': elapsed,
                'status': 'success'
            })
            print(f"  ✅ {elapsed:.1f}s | {response.video_url}")
        except Exception as e:
            elapsed = time.time() - start
            results.append({'model': model, 'provider': provider, 'error': str(e), 'time': elapsed, 'status': 'error'})
            print(f"  ❌ {elapsed:.1f}s | Error: {e}")
    
    print(f"\n{'='*60}")
    print("Results Summary:")
    for r in sorted(results, key=lambda x: x['time']):
        status = '✅' if r['status'] == 'success' else '❌'
        print(f"  {status} {r['model']:<20} {r['time']:.1f}s")
    
    print(f"\n→ All models available at https://nexa-api.com")
    print(f"→ RapidAPI: https://rapidapi.com/user/nexaquency")
    print(f"{'='*60}\n")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Video Generation Benchmark 2026")
    parser.add_argument("--api-key", required=True, help="NexaAPI key (get free at nexa-api.com)")
    parser.add_argument("--prompt", default="A cinematic drone shot over a misty mountain range at golden hour", help="Video prompt")
    parser.add_argument("--duration", type=int, default=5, help="Video duration in seconds")
    args = parser.parse_args()
    
    run_benchmark(args.api_key, args.prompt, args.duration)
