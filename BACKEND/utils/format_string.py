"""Format String Utility"""
import unicodedata
import re


class FormatStringAccents:
    """
    Format string utilities for Vietnamese text
    Matches FormatStringAccents.java
    """
    
    @staticmethod
    def remove_accents(text: str) -> str:
        """Remove Vietnamese accents from string"""
        if not text:
            return text
        
        # Normalize to NFD (decomposed form)
        nfkd = unicodedata.normalize('NFKD', text)
        
        # Filter out combining characters
        result = ''.join([c for c in nfkd if not unicodedata.combining(c)])
        
        return result
    
    @staticmethod
    def to_slug(text: str) -> str:
        """Convert text to URL-friendly slug"""
        if not text:
            return text
        
        # Remove accents
        text = FormatStringAccents.remove_accents(text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text)
        
        # Remove special characters
        text = re.sub(r'[^a-z0-9\-]', '', text)
        
        # Remove multiple hyphens
        text = re.sub(r'\-+', '-', text)
        
        # Remove leading/trailing hyphens
        text = text.strip('-')
        
        return text
    
    @staticmethod
    def normalize_search_text(text: str) -> str:
        """Normalize text for search (lowercase + remove accents)"""
        if not text:
            return text
        
        text = FormatStringAccents.remove_accents(text)
        return text.lower().strip()
