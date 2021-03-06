from datetime import datetime
from typing import Any, Dict, Union

from github.Branch import Branch
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.WorkflowRun import WorkflowRun

class Workflow(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def get_runs(
        self,
        actor: Union[str, NamedUser, _NotSetType],
        branch: Union[str, Branch, _NotSetType],
        event: Union[str, _NotSetType],
        status: Union[str, _NotSetType]
    ) -> PaginatedList[WorkflowRun]: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def badge_url(self) -> str: ...
