%global source3_hash f639656fc21925c45f3f55769b9fb7a90699e943376a725e215a5deea473b3e4
%global source2_hash 1110389daf57bfc33d593961e9898210e0395814ff93688b03f2ba32230c92cb
%global source1_hash babe34be05e187b038cce7661d3b4b8b0b00cc3602211a5400efa91d977bfbf9
%global source0_hash ed96909037b21f1e157dfb9290dbd09c6d58ffdc907d68c0988ff11e96d75d07
%{?haskell_setup}
%global coprapi copr-api-0.2.0
%global fedorakrb fedora-krb-0.1.0
%global say say-0.1.0.1
%global subpkgs %{coprapi} %{fedorakrb} %{say}
Name:           fbrnch
Version:        1.8.1
Release:        1%{?dist}
Summary:        Fedora packager tool to build package branches
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/fbrnch
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{coprapi}/%{coprapi}.tar.gz
Source2:        https://hackage.haskell.org/package/%{fedorakrb}/%{fedorakrb}.tar.gz
Source3:        https://hackage.haskell.org/package/%{say}/%{say}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
Requires:       bodhi-client
Requires:       curl
Requires:       fedpkg
Requires:       git-core
Requires:       koji
Requires:       openssh-clients
Requires:       rpm-build
Requires:       rpmautospec
Requires:       rpmdevtools
Requires:       util-linux-script
Recommends:     copr-cli
Recommends:     fedora-review
Recommends:     koji-tool
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bodhi-devel
BuildRequires:  ghc-bodhi-prof
BuildRequires:  ghc-bugzilla-redhat-devel
BuildRequires:  ghc-bugzilla-redhat-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-config-ini-devel
BuildRequires:  ghc-config-ini-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-either-prof
BuildRequires:  ghc-email-validate-devel
BuildRequires:  ghc-email-validate-prof
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-extra-prof
BuildRequires:  ghc-fedora-releases-devel
BuildRequires:  ghc-fedora-releases-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-directory-devel
BuildRequires:  ghc-http-directory-prof
BuildRequires:  ghc-http-query-devel
BuildRequires:  ghc-http-query-prof
BuildRequires:  ghc-koji-devel
BuildRequires:  ghc-koji-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-pagure-devel
BuildRequires:  ghc-pagure-prof
BuildRequires:  ghc-pretty-terminal-devel
BuildRequires:  ghc-pretty-terminal-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-rpm-nvr-devel
BuildRequires:  ghc-rpm-nvr-prof
BuildRequires:  ghc-rpmbuild-order-devel
BuildRequires:  ghc-rpmbuild-order-prof
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-select-rpms-devel
BuildRequires:  ghc-select-rpms-prof
BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-args-prof
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-simple-cmd-prof
BuildRequires:  ghc-simple-prompt-devel
BuildRequires:  ghc-simple-prompt-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-typed-process-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-xdg-basedir-devel
BuildRequires:  ghc-xdg-basedir-prof
BuildRequires:  help2man
# /oreon:deps
%description
Fbrnch (fedora branch or "f-branch" for short) is a convenient packaging tool
for Fedora Packagers, with integration for Bugzilla, Koji, and Bodhi.

Features include:
- merging and building a package across release branches
- automated parallel builds of sets of packages in dependency order
- creating, updating and listing one's package reviews
- requesting repos for new approved packages and branch requests
- import srpms from package reviews
- progressive copr builds
and many more commands.

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l GPL-3.0-or-later %{coprapi}
%ghc_lib_subpackage -l GPL-2.0-or-later %{fedorakrb}
%ghc_lib_subpackage -l MIT %{say}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -a1 -a2 -a3
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
