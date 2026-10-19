%global source1_hash 1568e6e67d96968560bde7f37110e0aff9072fe03f2e6658101072429524cf77
%global source0_hash 38a8cd2fc30273d43d4495c8df161f8a3dead15925d12a0f0717467eab26c4ea
%{?haskell_setup}
%global htmlentities html-entities-1.1.4.7
%global subpkgs %{htmlentities}
%global shortname cblrpm
Name:           cabal-rpm
Version:        2.3.2
Release:        8%{?dist}
Summary:        RPM packaging tool for Haskell Cabal-based packages
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/cabal-rpm
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{htmlentities}/%{htmlentities}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
Provides:       %{shortname} = %{version}-%{release}
Requires:       cabal-install
Requires:       dos2unix
Requires:       ghc-rpm-macros
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       wget
Requires:       yum-utils
Recommends:     stack > 2.7
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cached-json-file-devel
BuildRequires:  ghc-cached-json-file-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-fedora-krb-devel
BuildRequires:  ghc-fedora-krb-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-query-devel
BuildRequires:  ghc-http-query-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-simple-cabal-devel
BuildRequires:  ghc-simple-cabal-prof
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-args-prof
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-cmd-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  help2man
# /oreon:deps
%description
This package provides a RPM packaging tool for Haskell Cabal-based packages.

cabal-rpm has commands to generate a RPM spec file and srpm for a package.
It can rpmbuild packages, dnf/yum install their dependencies, prep packages,
and install them. There are commands to list package dependencies and missing
dependencies. The diff command compares the current spec file with a freshly
generated one, the update command updates the spec file to latest version from
Stackage or Hackage, and the refresh command updates the spec file to the
current cabal-rpm packaging. It also handles Hackage revisions of packages.
Standalone packages can also be made, built with cabal-install.

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l MIT %{htmlentities}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_bin_build
%install
%ghc_libs_install %{subpkgs}
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
ln -s %{name} %{buildroot}%{_bindir}/%{shortname}
sed -i -e "s/ _%{name} / _%{name} %{shortname} /" %{buildroot}%{bash_completions_dir}/%{name}
ln -s %{name} %{buildroot}%{_datadir}/bash-completion/completions/%{shortname}
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/%{shortname}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
