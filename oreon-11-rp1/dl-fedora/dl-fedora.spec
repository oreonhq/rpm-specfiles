%global source0_hash b894efd14296bee72c68e56ccba1c542c9d2a3a7e409c503756366cb820a9162
%bcond tests 0
Name:           dl-fedora
Version:        2.2
Release:        1%{?dist}
Summary:        Fedora image download tool
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/dl-fedora
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-fedora-releases-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-directory-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-pretty-terminal-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-xdg-userdirs-devel
BuildRequires:  help2man
# /oreon:deps
%description
Tool to download Fedora and Centos Stream iso and image files.

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
