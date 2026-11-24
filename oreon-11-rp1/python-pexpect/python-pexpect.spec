# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 13756b834dba0adf7603be77d943cc427011983ecd7c58b59b9bf122a1063e40
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{!?with_check: %global with_check 0}

%bcond_without check

%global modname pexpect

Name:           python-%{modname}
Summary:        Unicode-aware Pure Python Expect-like module
Version:        4.9.0
Release:        1%{?dist}

License:        ISC AND BSD-3-Clause
URL:            https://github.com/pexpect/pexpect
Source0:        https://github.com/pexpect/pexpect/archive/refs/tags/4.9.tar.gz#/pexpect-%{version}.tar.gz

Patch0:         794.patch
Patch1:         808.patch
Patch2:         827.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  /usr/bin/man
%if %{with check}
BuildRequires:  openssl
BuildRequires:  python-unversioned-command
%endif

BuildArch:      noarch

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to automate setup scripts for duplicating
software package installations on different servers. And it can be used for
automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
Pexpect is pure Python. Unlike other Expect-like modules for Python, Pexpect
does not require TCL or Expect nor does it require C extensions to be
compiled.  It should work on any platform that supports the standard Python
pty module.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-pytest
BuildRequires:  python3-ptyprocess
BuildRequires:  zsh
Requires:       python3-ptyprocess

%description -n python3-%{modname}
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands. This package contains the
python3 version of this module.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to automate setup scripts for duplicating
software package installations on different servers. And it can be used for
automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
Pexpect is pure Python. Unlike other Expect-like modules for Python, Pexpect
does not require TCL or Expect nor does it require C extensions to be
compiled.  It should work on any platform that supports the standard Python
pty module.

%prep
%oreon_sha256
%autosetup -n pexpect-4.9 -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/pexpect/tests

%if %{with check}
%check
export PYTHONIOENCODING=UTF-8
export NO_COLOR=1
echo "set enable-bracketed-paste off" > .inputrc
export INPUTRC=$PWD/.inputrc

%{python3} ./tools/display-sighandlers.py
%{python3} ./tools/display-terminalinfo.py
export CI=true
ignore="${ignore-} --ignore=tests/test_performance.py"
ignore="${ignore-} --ignore=tests/test_replwrap.py"
ignore="${ignore-} --ignore=tests/test_env.py"
python3 -m pytest ${ignore-}
%endif

%files -n python3-%{modname}
%license LICENSE
%doc doc examples
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.dist-info

%changelog
%autochangelog
