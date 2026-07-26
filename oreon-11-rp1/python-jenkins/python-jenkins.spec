%global source0_hash 8f4761c391ac11e8c1f23f771010920c10440497705ab7175d52358f5a12dc98

%global pypi_name python_jenkins

Name:           python-jenkins
Version:        1.8.3
Release:        %autorelease
Summary:        Python bindings for the remote Jenkins API

License:        BSD-3-Clause
URL:            https://python-jenkins.readthedocs.org/en/latest
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
# Contents of `test-requirements.txt`:
BuildRequires:  python%{python3_pkgversion}-cmd2
BuildRequires:  python%{python3_pkgversion}-coverage >= 3.6
BuildRequires:  python%{python3_pkgversion}-subunit
BuildRequires:  python%{python3_pkgversion}-requests-mock >= 1.11.0
BuildRequires:  python%{python3_pkgversion}-requests-kerberos
BuildRequires:  python%{python3_pkgversion}-sphinx >= 4.4.0
BuildRequires:  python%{python3_pkgversion}-stestr >= 2.0.0
BuildRequires:  python%{python3_pkgversion}-testscenarios
BuildRequires:  python%{python3_pkgversion}-testtools
BuildRequires:  pre-commit
BuildRequires:  python%{python3_pkgversion}-multiprocess

Recommends:     python%{python3_pkgversion}-requests_kerberos

%description
Python Jenkins is a library for the remote API of the Jenkins continuous
integration server. It is useful for creating and managing jobs as well as
build nodes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove env from __init__.py
sed -i '1{s|^#!/usr/bin/env python||}' jenkins/__init__.py

%generate_buildrequires
export PBR_VERSION=%{version}

%pyproject_buildrequires

%build
export PBR_VERSION=%{version}

%pyproject_wheel

PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=$PWD \
  %make_build -C doc html man
rm doc/build/html/.buildinfo

%install
export PBR_VERSION=%{version}

%pyproject_install
%pyproject_save_files jenkins

install -D -m0644 -p doc/build/man/pythonjenkins.1 %{buildroot}%{_mandir}/man1/pythonjenkins.1

%check
%{__python3} -m testtools.run discover tests

%files -f %{pyproject_files}
%doc README.rst doc/build/html
%license COPYING
%{_mandir}/man1/pythonjenkins.1.*

%changelog
%autochangelog
