%global source0_hash dd9d825e496435fb3beba3ae7bea9f77e821e894667d07431d1d4c8c570b9e58

# Expected failures in mock, hangs in koji
%bcond_with tests
# The *.py files we ship are not python scripts, #813651
%global _python_bytecompile_errors_terminate_build 0
%define upstream_version 2.17.0

Name:           bash-completion
Version:        2.17
Release:        2%{?dist}
Epoch:          1
Summary:        Programmable completion for Bash

License:        GPL-2.0-or-later
URL:            https://github.com/scop/bash-completion
Source0:        https://github.com/scop/bash-completion/releases/download/2.17.0/bash-completion-2.17.0.tar.xz

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
rm %{buildroot}%{_datadir}/bash-completion/completions/{cowsay,cowthink}

# Bug 1819867 - conflict over the makepkg name with pacman
rm %{buildroot}%{_datadir}/bash-completion/completions/makepkg

# Bug 2088307 - Remove completions for prelink
rm %{buildroot}%{_datadir}/bash-completion/completions/prelink

# Bug 2188865 - Remove bash completions for javaws as it's not shipped with Fedora
rm %{buildroot}%{_datadir}/bash-completion/completions/javaws

# Bug 2391218 - patchutils package contains its own completion for this
rm %{buildroot}%{_datadir}/bash-completion/completions/interdiff

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
%{_sysconfdir}/bash_completion.d/000_bash_completion_compat.bash
%{_datadir}/bash-completion/

%files devel
%{_datadir}/cmake/
%{_datadir}/pkgconfig/bash-completion.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17-2
- Prepare for Oreon 11 (RP1)
