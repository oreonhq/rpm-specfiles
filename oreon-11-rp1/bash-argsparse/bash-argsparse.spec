%global source0_hash e56ed8b499d2604f914037954d98ea683a50776373d01ac951b314070af29233
Summary:        An high level argument parsing library for bash
Name: bash-argsparse
Version: 1.8
Release:        9%{?dist}
License: WTFPL
URL: https://github.com/Anvil/bash-argsparse
Source0:        http://argsparse.livna.org/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: bash >= 4.1
Requires: util-linux
Requires: glibc-common
Requires: /usr/bin/host
# oreon:deps
BuildRequires:  /usr/bin/host
BuildRequires:  doxygen
BuildRequires:  glibc-common
BuildRequires:  util-linux
# /oreon:deps
%description
An high level argument parsing library for bash.

The purpose is to replace the option-parsing and usage-describing
functions commonly rewritten in all scripts.

This library is implemented for bash version 4. Prior versions of bash
will fail at interpreting that code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

doxygen
%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 argsparse.sh %{buildroot}/%{_bindir}
ln -s argsparse.sh %{buildroot}/%{_bindir}/argsparse
%oreon_autofiles main

%check

./unittest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
