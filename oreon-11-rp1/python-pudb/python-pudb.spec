%global source0_hash e6dedb81fc3c8cdcd66cf62e86337cb913570ebb2c994c9ab52012d059e086ad

%global srcname pudb

Name:          python-pudb
Version:       2025.1.5
Release:       %autorelease
Summary:       A full-screen, console-based Python debugger
License:       MIT
URL:           https://github.com/inducer/pudb
Source0:       %{pypi_source}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-mock
BuildRequires: pyproject-rpm-macros

%global _description %{expand:
PuDB is a full-screen, console-based visual debugger for Python.

Its goal is to provide all the niceties of modern GUI-based debuggers in a more
lightweight and keyboard-friendly package. PuDB allows you to debug code right
where you write and test it--in a terminal. If you've worked with the excellent
(but nowadays ancient) DOS-based Turbo Pascal or C tools, PuDB's UI might look
familiar.}

%description %_description

%package -n python3-%{srcname}
Summary:       A full-screen, console-based Python debugger
%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

sed -i '1{\@^#! /usr/bin/env python@d}' pudb/debugger.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pudb

%changelog
%autochangelog
