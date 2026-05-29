%global source0_hash none

%bcond_without check

%global modname pexpect

Name:           python-%{modname}
Summary:        Unicode-aware Pure Python Expect-like module
Version:        4.9.0
Release:        15%{?dist}

# All the files have ISC license except the
# following two that have BSD license:
# python-pexpect/pexpect-4.8.0/pexpect/pty_spawn.py
# python-pexpect/pexpect-4.8.0/pexpect/spawnbase.py
License:        ISC AND BSD-3-Clause
URL:            https://github.com/pexpect/pexpect
Source0:        https://github.com/pexpect/pexpect/archive/4.9.0/pexpect-4.9.0.tar.gz

# Force NO_COLOR=1 to fix test failures with Python 3.13+ REPL
Patch:        https://github.com/pexpect/pexpect/pull/808.patch
# Tests: Avoid the multiprocessing forkserver method (for Python 3.14+ compatibility)
Patch:          https://github.com/pexpect/pexpect/pull/808.patch

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{modname}-%{version} -p 1

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
# workaround for https://bugzilla.redhat.com/show_bug.cgi?id=1914843
# upstream: https://github.com/pexpect/pexpect/issues/669
# There's a patch upstream that we can presumable remove this after
# it merges and is released.
# Thx for the suggestion Miro: https://www.spinics.net/lists/fedora-devel/msg283026.html
echo "set enable-bracketed-paste off" > .inputrc
export INPUTRC=$PWD/.inputrc

%{python3} ./tools/display-sighandlers.py
%{python3} ./tools/display-terminalinfo.py
export CI=true
# Gating downstream builds on particular benchmark results doesn’t make sense
# across diverse hardware.
ignore="${ignore-} --ignore=tests/test_performance.py"
%pytest ${ignore-}
%endif

%files -n python3-%{modname}
%license LICENSE
%doc doc examples
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.dist-info

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.9.0-15
- Import
