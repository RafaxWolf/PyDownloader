def get_provider(url, providers):
    for provider in providers:
        if provider.supports(url):
            return provider
    raise ValueError(f"No provider found for URL: {url}")