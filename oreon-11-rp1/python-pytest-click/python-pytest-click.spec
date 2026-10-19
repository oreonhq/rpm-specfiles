%global source0_hash fdd9f6721f877dda021e7c5dc73e70aecd37e5ed23ec6820f8a7b3fd7b4f8d30
Name:           python-pytest-click
Version:        1.1.0
Release:        14%{?dist}
Summary:        Pytest plugin for Click
License:        MIT
URL:            https://github.com/Stranger6667/pytest-click
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_click/pytest_click-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%package -n     python3-pytest-click
Summary:        Pytest plugin for Click
%description -n python3-pytest-click
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_click-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-pytest-click usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-pytest-click -f %{oreon_filedir}/python3-pytest-click.list

%changelog

%autochangelog
