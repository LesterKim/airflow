# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Base classes for DAG and DagBag."""

from abc import ABCMeta, abstractmethod


class BaseDag(metaclass=ABCMeta):
    """
    Base DAG object that both the SimpleDag and DAG inherit.
    """

    @property
    @abstractmethod
    def dag_id(self):
        """
        :return: the DAG ID
        :rtype: unicode
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def task_ids(self):
        """
        :return: A list of task IDs that are in this DAG
        :rtype: List[unicode]
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def full_filepath(self):
        """
        :return: The absolute path to the file that contains this DAG's definition
        :rtype: unicode
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def concurrency(self):
        """
        :return: maximum number of tasks that can run simultaneously from this DAG
        :rtype: int
        """
        raise NotImplementedError()

    @abstractmethod
    def is_paused(self):
        """
        :return: whether this DAG is paused or not
        :rtype: bool
        """
        raise NotImplementedError()

    @abstractmethod
    def pickle_id(self):
        """
        :return: The pickle ID for this DAG, if it has one. Otherwise None.
        :rtype: unicode
        """
        raise NotImplementedError


class BaseDagBag:
    """
    Base object that both the SimpleDagBag and DagBag inherit.
    """
    @property
    @abstractmethod
    def dag_ids(self):
        """
        :return: a list of DAG IDs in this bag
        :rtype: List[unicode]
        """
        raise NotImplementedError()

    @abstractmethod
    def get_dag(self, dag_id):
        """
        :return: whether the task exists in this bag
        :rtype: airflow.dag.base_dag.BaseDag
        """
        raise NotImplementedError()
