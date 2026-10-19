%global source0_hash b3c0520f0cea974886e1b4b7927a9a4547d0ce8302c10a82b0bed65fc5f4f9e2
%bcond tests 0
Name:           koji-tool
Version:        1.3.1
Release:        1%{?dist}
Summary:        Koji CLI tool for querying tasks and installing builds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/koji-tool
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Recommends:     krb5-workstation
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-directory-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-koji-devel
BuildRequires:  ghc-pretty-simple-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-rpm-nvr-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-select-rpms-devel
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-xdg-userdirs-devel
BuildRequires:  help2man
# /oreon:deps
%description
Koji-tool is a CLI interface to Koji with commands to query builds, tasks,
install rpms, and track buildlog sizes.

Koji is the RPM-based buildsystem of Fedora Linux and CentOS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup

%build

%ghc_bin_build
%install
%ghc_bin_install
set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{fish_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}
%{buildroot}%{_bindir}/%{name} --fish-completion-script %{name} > %{buildroot}%{fish_completions_dir}/%{name}
%{buildroot}%{_bindir}/%{name} --zsh-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{zsh_completions_dir}/_%{name}
mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%check

%if %{with tests}
PATH=%{buildroot}%{_bindir}:$PATH
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
