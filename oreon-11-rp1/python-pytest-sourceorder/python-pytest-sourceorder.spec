%global source0_hash 1fd888ea08f3b13489016850c80d07742c19d6f177daf3c3b73a87f8f6a45bb1

Name: python-pytest-sourceorder
Version: 0.6.0
Release: 19%{?dist}
Summary: Test-ordering plugin for pytest

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/encukou/pytest-sourceorder

Source0: https://github.com/encukou/pytest-sourceorder/archive/v%{version}.tar.gz#/pytest-sourceorder-%{version}.tar.gz

# Compatibility with pytest 8.4+
Patch:   https://pagure.io/python-pytest-sourceorder/pull-request/4.patch

BuildArch: noarch
BuildRequires: python3-devel

%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%package -n python3-pytest-sourceorder
Summary: %summary

%{?python_provide:%python_provide python3-pytest-sourceorder}

%description -n python3-pytest-sourceorder
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pytest-sourceorder-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_sourceorder

%check
%tox

%files -n python3-pytest-sourceorder -f %{pyproject_files}
%license COPYING
%doc README.rst

%changelog
%autochangelog
