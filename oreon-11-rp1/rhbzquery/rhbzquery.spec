%global source0_hash efb446f2200fd99b6452df557e7c72cba40eac89a37a3c1ed5fec5f905475253
%bcond tests 1
Name:           rhbzquery
Version:        0.4.5
Release:        1%{?dist}
Summary:        Bugzilla query tool
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/rhbzquery
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-config-ini-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-email-validate-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  ghc-text-devel
BuildRequires:  help2man
# /oreon:deps
%description
A CLI tool for creating bugzilla queries for bugzilla.redhat.com.

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
