# Pydantic Interview Notes

## Core Concepts
- **Type Coercion & Validation**: Ensures dynamic input matches declared type hints.
- **Fast Execution**: Written in Rust (`pydantic-core`).
- **BaseModel**: The foundational class inherited by custom schemas.

## Key Decorators & Features
- `Field(...)`: Sets constraints (`gt`, `lt`, `min_length`, regex) and descriptions.
- `@field_validator`: Validates individual attributes.
- `@model_validator`: Performs validation across multiple fields.
- `computed_field`: Computes property values during model serialization.

## Key Utility Methods
- `Model.model_validate_json()`: Direct JSON string parsing.
- `Model.model_dump()`: Converts instance into a Python dict.
- `Model.model_dump_json()`: Converts instance into a JSON string.