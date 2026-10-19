%global source1_hash d6d1e593e607830ec0d6342bacab877ac348175c100ab1a168f6a4e2fdd216da
%global source0_hash 170c396f59e37851ed626c07756dc394841f7597895e691bf26049fee9725a6c
Name:           bench
Version:        1.0.13
Release:        1%{?dist}
Summary:        Command-line benchmark tool
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/bench
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}.cabal#/%{name}-%{version}.cabal
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-criterion-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-turtle-devel
BuildRequires:  help2man
# /oreon:deps
%description
Think of this as a more powerful alternative to the 'time' command.
Use this command-line tool to benchmark a command using Haskell's 'criterion'
library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
dos2unix -k -n %{SOURCE1} %{name}.cabal
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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
