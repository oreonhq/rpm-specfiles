%global source0_hash cf724962efd12144dd89bf9655b74482e6b8dd76fdbbc3f7d5d2195f14b8650c
Name:           ostree-pin
Version:        0.1.1
Release:        1%{?dist}
Summary:        Tool to update ostree deployment pin
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/ostree-pin
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-gi-gio-devel
BuildRequires:  ghc-gi-ostree-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  help2man
# /oreon:deps
%description
CLI tool to easily pin the current ostree deployment.

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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
