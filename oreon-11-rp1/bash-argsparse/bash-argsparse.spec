%global source0_hash 858ec1178a2df92733733a7d2d3f3e2dce1986f7c961affc471ac078c8ed6276

Summary: An high level argument parsing library for bash
Name: bash-argsparse
Version: 1.8
Release: 9%{?dist}
License: WTFPL
URL: https://github.com/Anvil/bash-argsparse
Source0: http://argsparse.livna.org/%{name}-%{version}.tar.gz
BuildArch: noarch
# Binaries are required for unittest to perform cleanly.
BuildRequires: doxygen
BuildRequires: glibc-common
BuildRequires: util-linux
BuildRequires: /usr/bin/host

Requires: bash >= 4.1
Requires: util-linux
Requires: glibc-common
Requires: /usr/bin/host

%description
An high level argument parsing library for bash.

The purpose is to replace the option-parsing and usage-describing
functions commonly rewritten in all scripts.

This library is implemented for bash version 4. Prior versions of bash
will fail at interpreting that code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

%build
# Nothing to build, except the documentation.
doxygen

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 argsparse.sh %{buildroot}/%{_bindir}
ln -s argsparse.sh %{buildroot}/%{_bindir}/argsparse

%check
./unittest

%files
%doc tutorial README.md html COPYING
%{_bindir}/argsparse
%{_bindir}/argsparse.sh

%changelog
%autochangelog
