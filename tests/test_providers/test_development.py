# -*- coding: utf-8 -*-

import pytest

from mimesis import Development, data


class TestDevelopment(object):

    @pytest.fixture
    def dev(self):
        return Development()

    def test_license(self, dev):
        result = dev.software_license()
        assert result in data.LICENSES

    def test_version_control_system(self, dev):
        vcs = ['Git', 'Subversion']
        assert dev.version_control_system() in vcs

    def test_version(self, dev):
        result = dev.version().split('.')
        result = [int(i) for i in result]

        assert len(result) == 3

        major = result[0]
        assert (major >= 0) and (major <= 11)

        minor = result[1]
        assert (minor >= 0) and (minor <= 11)

        patch = result[2]
        assert (patch >= 0) and (patch <= 11)

        pre_release = dev.version(pre_release=True)
        assert len(pre_release.split('.')) == 4

        # Use calendar versioning
        calver = dev.version(calver=True)
        y, *_ = calver.split('.')
        assert (int(y) >= 2016) and (int(y) <= 2018)

    def test_programming_language(self, dev):
        result = dev.programming_language()
        assert result in data.PROGRAMMING_LANGS

    def test_database(self, dev):
        result = dev.database()
        assert result in data.SQL

        result = dev.database(nosql=True)
        assert result in data.NOSQL

    def test_other(self, dev):
        result = dev.container()
        assert result in data.CONTAINER

    def test_frontend(self, dev):
        result = dev.frontend()
        assert result in data.FRONTEND

    def test_backend(self, dev):
        _result = dev.backend()
        assert _result in data.BACKEND

    def test_os(self, dev):
        result = dev.os()
        assert result in data.OS

    def test_boolean(self, dev):
        result = dev.boolean()
        assert result or (not result)


class TestSeededDevelopment(object):

    @pytest.fixture
    def dv1(self, seed):
        return Development(seed=seed)

    @pytest.fixture
    def dv2(self, seed):
        return Development(seed=seed)

    def test_software_license(self, dv1, dv2):
        assert dv1.software_license() == dv2.software_license()

    def test_version_control_system(self, dv1, dv2):
        assert dv1.version_control_system() == dv2.version_control_system()

    def test_version(self, dv1, dv2):
        assert dv1.version() == dv2.version()

    def test_programming_language(self, dv1, dv2):
        assert dv1.programming_language() == dv2.programming_language()

    def test_database(self, dv1, dv2):
        assert dv1.database() == dv2.database()

    def test_container(self, dv1, dv2):
        assert dv1.container() == dv2.container()

    def test_frontend(self, dv1, dv2):
        assert dv1.frontend() == dv2.frontend()

    def test_backend(self, dv1, dv2):
        assert dv1.backend() == dv2.backend()

    def test_os(self, dv1, dv2):
        assert dv1.os() == dv2.os()

    def test_boolean(self, dv1, dv2):
        assert dv1.boolean() == dv2.boolean()
