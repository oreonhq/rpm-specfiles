%global source0_hash 033b8259f1c39523ade290c3b0abbf33401473ae29d913b0ebeeb7cd2d1a545a
%bcond tests 0
Name:           dnf-repo
Version:        0.6.2
Release:        1%{?dist}
Summary:        A dnf wrapper with fine control of enabled repos
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/dnf-repo
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dnf
BuildRequires:  fedora-repos
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Glob-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-curl-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-directory-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  help2man
# /oreon:deps
%description
A command-line wrapper of the dnf package manager to control the repos enabled
for a dnf invocation.

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
