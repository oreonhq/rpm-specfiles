%{!?with_check: %global with_check 0}
%global source0_hash 13756b834dba0adf7603be77d943cc427011983ecd7c58b59b9bf122a1063e40
%bcond_without check
%global modname pexpect
Name:           python-%{modname}
Summary:        Unicode-aware Pure Python Expect-like module
Version:        4.9.0
Release:        1%{?dist}
License:        ISC AND BSD-3-Clause
URL:            https://github.com/pexpect/pexpect
Source0:        https://github.com/pexpect/pexpect/archive/refs/tags/4.9.tar.gz#/pexpect-%{version}.tar.gz
Patch:        https://github.com/pexpect/pexpect/pull/808.patch
%if %{with check}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pexpect = %{version}-%{release}
# /oreon:deps
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
Summary:        Unicode-aware Pure Python Expect-like module
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pexpect-4.9
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}%{python3_sitelib}/pexpect/tests
%oreon_autofiles main usr/lib/python3*/site-packages/pexpect* usr/lib64/python3*/site-packages/pexpect* usr/bin/*
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
%files
%files -n python3-pexpect -f %{oreon_filedir}/python3-pexpect.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.9.0-15
- Import
