#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime

API_KEY = os.environ.get('NEWSAPI_KEY')
BASE_URL = 'https://newsapi.org/v2'

# 뉴스 검색 키워드
QUERIES = {
      '기업뉴스': 'startup Korean company employment',
      'AI뉴스': 'AI technology LLM agent'
}

def fetch_news(query, language='ko'):
      """NewsAPI에서 뉴스 검색"""
      try:
                response = requests.get(
                              f'{BASE_URL}/everything',
                              params={
                                                'q': query,
                                                'language': language,
                                                'sortBy': 'publishedAt',
                                                'pageSize': 5,
                                                'apiKey': API_KEY
                              },
                              timeout=10
                )
                response.raise_for_status()
                return response.json()
except Exception as e:
        print(f"Error fetching news for '{query}': {e}")
        return {'articles': []}

def format_news(articles):
      """뉴스를 마크다운 형식으로 변환"""
      md = []
      for i, article in enumerate(articles[:5], 1):
                title = article.get('title', 'No title')
                source = article.get('source', {}).get('name', 'Unknown')
                published = article.get('publishedAt', 'No date')[:10]
                description = article.get('description', 'No description')
                url = article.get('url', '#')

        md.append(f"### {i}. {title}")
        md.append(f"**출처:** {source} | **날짜:** {published}")
        md.append(f"**요약:** {description}")
        md.append(f"[기사 읽기]({url})")
        md.append("")

    return '\n'.join(md)

def main():
      today = datetime.now().strftime('%Y-%m-%d')
    filename = f'news_{today}.md'

    with open(filename, 'w', encoding='utf-8') as f:
              f.write(f"# 뉴스 큐레이션 - {today}\n\n")

        for category, query in QUERIES.items():
                      f.write(f"## {category}\n\n")
                      data = fetch_news(query)
                      articles = data.get('articles', [])
                      f.write(format_news(articles))
                      f.write("\n")

    print(f"✅ 뉴스 큐레이션 완료: {filename}")

if __name__ == '__main__':
      main()
