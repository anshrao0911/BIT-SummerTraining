"""Custom exceptions used by the scanner."""


class MangaScannerError(Exception):
    """Base class for scanner-specific errors."""


class SourceNotFoundError(MangaScannerError):
    """Raised when the input path does not exist."""


class UnsupportedSourceError(MangaScannerError):
    """Raised when an input path is not a supported folder, archive, or PDF."""


class EmptySourceError(MangaScannerError):
    """Raised when a supported input contains no readable pages."""


class CorruptSourceError(MangaScannerError):
    """Raised when a supported input cannot be opened or decoded."""
