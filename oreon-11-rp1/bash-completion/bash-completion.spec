# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 88bcf85124f77f74f2f2f8bcd16ac4382d807a827ede742a64940c7116aea33f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# Expected failures in mock, hangs in koji
%bcond_with tests
# The *.py files we ship are not python scripts, #813651
%global _python_bytecompile_errors_terminate_build 0
%define upstream_version 2.18.0

Name:           bash-completion
Version:        2.18
Release:        1%{?dist}
Epoch:          1
Summary:        Programmable completion for Bash

License:        GPL-2.0-or-later
URL:            https://github.com/scop/bash-completion
Source0:        https://github.com/scop/bash-completion/releases/download/%{version}.0/bash-completion-%{version}.0.tar.xz

BuildArch:      noarch
%if %{with tests}
BuildRequires:  dejagnu
BuildRequires:  screen
BuildRequires:  tcllib
%endif
# Needed for rfkill patch as it modifies Makefile.am
# It should be removed while rebasing to bash-completion-2.8
BuildRequires:  automake
BuildRequires: make
BuildRequires:  oreon-rpm-macros
Requires:       bash >= 4.1

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash.

%package devel
Summary: Development files for %{name}
Requires: %{name} =  %{epoch}:%{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%oreon_sha256

%autosetup -n %{name}-%{upstream_version} -p1

%build
# Needed for rfkill patch as it modifies Makefile.am
# It should be removed while rebasing to bash-completion-2.8
autoreconf -fi -v
%configure
%make_build

%install
%make_install

# Updated completion shipped in cowsay package:
rm %{buildroot}%{_datadir}/bash-completion/completions-core/{cowsay,cowthink}.bash

# Bug 1819867 - conflict over the makepkg name with pacman
rm %{buildroot}%{_datadir}/bash-completion/completions-core/makepkg.bash

# Bug 2088307 - Remove completions for prelink
rm %{buildroot}%{_datadir}/bash-completion/completions-core/prelink.bash

rm %{buildroot}%{_datadir}/bash-completion/completions-core/javaws.bash

# Bug 2391218 - patchutils package contains its own completion for this
rm %{buildroot}%{_datadir}/bash-completion/completions-fallback/interdiff.bash

%check
# For some tests involving non-ASCII filenames
export LANG=C.UTF-8
%if %{with tests}
# This stuff borrowed from dejagnu-1.4.4-17 (tests need a terminal)
tmpfile=$(mktemp)
screen -D -m sh -c '( make check ; echo $? ) >'$tmpfile
cat $tmpfile
result=$(tail -n 1 $tmpfile)
rm -f $tmpfile
exit $result
%else
make -C completions check
%endif


%files
%license COPYING
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%doc doc/configuration.md doc/styleguide.md
%config(noreplace) %{_sysconfdir}/profile.d/bash_completion.sh
%{_datadir}/bash-completion/

%files devel
%{_datadir}/cmake/
%{_datadir}/pkgconfig/bash-completion.pc

