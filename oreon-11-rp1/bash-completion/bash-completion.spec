%global source0_hash 88bcf85124f77f74f2f2f8bcd16ac4382d807a827ede742a64940c7116aea33f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap

Name: bash-completion
Version: 2.18.0
Release: 1%{?dist}
Summary: Programmable completion functions for bash
License: GPL-2.0-or-later
URL: https://github.com/scop/bash-completion
Source0: https://github.com/scop/bash-completion/releases/download/%{version}/bash-completion-%{version}.tar.xz
BuildArch: noarch
Requires: bash
Provides: pkgconfig(bash-completion) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: bash
BuildRequires: sed

%description
bash-completion is a collection of command line completions for bash.

%prep
%oreon_sha256
%autosetup -n bash-completion-%{version} -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_sysconfdir}/profile.d/bash_completion.sh
%{_datadir}/bash-completion
%{_datadir}/pkgconfig/bash-completion.pc
%{_datadir}/cmake/bash-completion
