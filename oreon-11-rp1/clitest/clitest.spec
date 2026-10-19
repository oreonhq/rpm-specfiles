%global source0_hash 4005de0bc27e4676e418ab1e1e64861272aa74af1212c73a1173760fc449b049
%global forgeurl https://github.com/aureliojargas/clitest
%global tag %{version}
Name:    clitest
Version: 0.5.0
Release:        9%{?dist}
Summary:        Command Line Tester
License: MIT
URL:     %{forgeurl}
%forgemeta
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:     noarch
Requires: diffutils
Requires: sed
Requires: grep
Suggests: perl
# oreon:deps
BuildRequires:  /usr/bin/perl
BuildRequires:  bash
BuildRequires:  dash
BuildRequires:  make
BuildRequires:  mksh
BuildRequires:  zsh
# /oreon:deps
%description
clitest is a portable POSIX shell script that performs automatic testing in \
Unix command lines.

It's the same concept as in Python's doctest module: you document both the \
commands and their expected output, using the familiar interactive prompt \
format, and a specialized tool tests them.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%check

make test docker_run=
%install
install -D -m755 -p clitest %{buildroot}%{_bindir}/clitest
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
