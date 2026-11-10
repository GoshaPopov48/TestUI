from uuid import uuid4


def generate_unique_name(prefix: str) -> str:
    suffix = uuid4().hex[:6]
    return f"{prefix}_{suffix}"

def generate_project_name(prefix: str) -> str:
    suffix = uuid4().hex[:3]
    return f"{prefix}_{suffix}"

def generate_project_id_name(prefix: str) -> str:
    suffix = uuid4().hex[:3]
    return f"{prefix}_{suffix}"

def generate_issue_title(prefix: str)-> str:
    suffix = uuid4().hex[:7]
    return f"{prefix}_{suffix}"

def generate_issue_description(prefix: str)-> str:
    suffix = uuid4().hex[:120]
    return f"{prefix}_{suffix}"

def generate_comment(prefix: str)-> str:
    suffix = uuid4().hex[:230]
    return f"{prefix}_{suffix}"

