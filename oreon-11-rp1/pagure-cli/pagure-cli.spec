%global source0_hash bfc39c4adbb18cce88a171f0fe38ebb40ee67ac3140121643e3a6efe3a298df6
Name:           pagure-cli
Version:        0.2.3
Release:        1%{?dist}
Summary:        A Pagure gitforge query tool
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/pagure-cli
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-query-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-pagure-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  help2man
# /oreon:deps
%description
A command-line Pagure (gitforge) client for querying and listing projects,
users, groups, and issues.

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
%{buildroot}%{_bindir}/pagure --bash-completion-script pagure | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/pagure
%{buildroot}%{_bindir}/pagure --fish-completion-script pagure > %{buildroot}%{fish_completions_dir}/pagure
%{buildroot}%{_bindir}/pagure --zsh-completion-script pagure | sed s/filenames/default/ > %{buildroot}%{zsh_completions_dir}/_pagure
mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/pagure > %{buildroot}%{_mandir}/man1/pagure.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
