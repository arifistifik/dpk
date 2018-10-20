# -*- coding: utf-8 -*-



import github.GithubObject

import github.CommitStatus
import github.Repository


class CommitCombinedStatus(github.GithubObject.NonCompletableGithubObject):
    """
    This class represents CommitCombinedStatuses. The reference can be found here https://developer.github.com/v3/repos/statuses/#get-the-combined-status-for-a-specific-ref
    """

    def __repr__(self):
        return self.get__repr__({"sha": self._sha.value, "state": self._state.value})

    @property
    def state(self):
        """
        :type: string
        """
        return self._state.value

    @property
    def sha(self):
        """
        :type: string
        """
        return self._sha.value

    @property
    def total_count(self):
        """
        :type: integer
        """
        return self._total_count.value

    @property
    def commit_url(self):
        """
        :type: string
        """
        return self._commit_url.value

    @property
    def url(self):
        """
        :type: string
        """
        return self._url.value

    @property
    def repository(self):
        """
        :type: :class:`github.Repository.Repository`
        """
        return self._repository.value

    @property
    def statuses(self):
        """
        :type: list of :class:`CommitStatus`
        """
        return self._statuses.value

    def _initAttributes(self):
        self._state = github.GithubObject.NotSet
        self._sha = github.GithubObject.NotSet
        self._total_count = github.GithubObject.NotSet
        self._commit_url = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet
        self._repository = github.GithubObject.NotSet
        self._statuses = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "state" in attributes:  
            self._state = self._makeStringAttribute(attributes["state"])
        if "sha" in attributes:  
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "total_count" in attributes:  
            self._total_count = self._makeIntAttribute(attributes["total_count"])
        if "commit_url" in attributes:  
            self._commit_url = self._makeStringAttribute(attributes["commit_url"])
        if "url" in attributes:  
            self._url = self._makeStringAttribute(attributes["url"])
        if "repository" in attributes:  
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
        if "statuses" in attributes:  
            self._statuses = self._makeListOfClassesAttribute(github.CommitStatus.CommitStatus, attributes["statuses"])