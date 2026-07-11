from src.config.constants import MAX_CODE_SIZE, SUPPORTED_LANGUAGES


def validate_code_size(code: str) -> bool:
    # Returns False if code exceeds the maximum allowed size
    return len(code) <= MAX_CODE_SIZE


def validate_language(filename: str) -> bool:
    # Checks if the file extension maps to a supported language
    extension_map = {
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".go": "go",
        ".rs": "rust",
        ".php": "php",
        ".rb": "ruby"
    }

    for ext, lang in extension_map.items():
        if filename.endswith(ext) and lang in SUPPORTED_LANGUAGES:
            return True

    return False
