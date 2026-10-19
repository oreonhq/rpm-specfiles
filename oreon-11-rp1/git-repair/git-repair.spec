%global source0_hash 21cfed1f573d6221352174d782aecd5fa56a07c5abb4cb3478968682d570d5ab
Name:           git-repair
Version:        1.20230814
Release:        1%{?dist}
Summary:        Repairs a damaged git repository
License:        AGPL-3.0-or-later
URL:            https://hackage.haskell.org/package/git-repair
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Requires:       git-core
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-IfElse-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-bytestring-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hslogger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  git-core
# /oreon:deps
%description
Git-repair can repair various forms of damage to git repositories.

It is a complement to git fsck, which finds problems, but does not fix them.

As well as avoiding the need to rm -rf a damaged repository and re-clone, using
git-repair can help rescue commits you've made to the damaged repository and
not yet pushed out.

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
install -m 644 -p -t %{buildroot}%{_mandir}/man1/ ./git-repair.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
