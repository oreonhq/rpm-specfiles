%global source2_hash d6f2efcb9d76fb490db8dd955f5f87d18907cf1b5c286c6c47cb1c1363bf5cb7
%global source0_hash 7498ada8e67bff63e45e3afbc3bcf2bc0b9ce6d898282c4ef9ed55952b9eb638
ExcludeArch: %{ix86}
%global giturl  https://github.com/ocaml/opam
%global testurl https://github.com/ocaml/opam-repository
Name:           opam
Version:        2.6.0
Release:        1%{?dist}
Summary:        Source-based package manager for OCaml
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://opam.ocaml.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz
Source1:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz.sig
Source2:        https://opam.ocaml.org/opam-dev-pubkey.pgp
Source3:        %{testurl}/archive/0070613707.tar.gz
Source4:        %{testurl}/archive/009e00fa.tar.gz
Source5:        %{testurl}/archive/11ea1cb.tar.gz
Source6:        %{testurl}/archive/143dd2a2f59f5befbf3cb90bb2667f911737fbf8.tar.gz
Source7:        %{testurl}/archive/297366c.tar.gz
Source8:        %{testurl}/archive/3235916.tar.gz
Source9:        %{testurl}/archive/7090735c.tar.gz
Source10:       %{testurl}/archive/7371c1d9.tar.gz
Source11:       %{testurl}/archive/a5d7cdc0.tar.gz
Source12:       %{testurl}/archive/ad4dd344.tar.gz
Source13:       %{testurl}/archive/c1842d168d.tar.gz
Source14:       %{testurl}/archive/c1ba97dafe95c865d37ad4d88f6e57c9ffbe7f0a.tar.gz
Source15:       %{testurl}/archive/de897adf36c4230dfea812f40c98223b31c4521a.tar.gz
Source16:       %{testurl}/archive/f372039d.tar.gz
Patch:          %{name}-disable-tests.patch
Requires:       bubblewrap
Requires:       bzip2
Requires:       gcc
Requires:       gzip
Requires:       make
Requires:       tar
Requires:       unzip
Requires:       xz
Requires:       opam-installer%{?_isa} = %{version}-%{release}
Recommends:     git-core
Suggests:       darcs
Suggests:       mercurial
Suggests:       rsync
# oreon:deps
BuildRequires:  bubblewrap
BuildRequires:  bzip2
BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  mercurial
BuildRequires:  ocaml
BuildRequires:  ocaml-base64-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-jsonm-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-opam-0install-cudf-devel
BuildRequires:  ocaml-opam-file-format-devel
BuildRequires:  ocaml-patch-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  ocaml-spdx-licenses-devel
BuildRequires:  ocaml-swhid-core-devel
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-z3-devel
BuildRequires:  openssl
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  xxd
BuildRequires:  xz
# /oreon:deps
%description
Opam is a source-based package manager for OCaml.  It supports multiple
simultaneous compiler installations, flexible package constraints, and a
Git-friendly development workflow.

%package installer
Summary:        Standalone script for opam install files
%description installer
Standalone script for working with opam .install files, see the opam package
for more information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n %{name}-full-%{version} -p1
sed -e 's,%%SOURCE3%%,%{SOURCE3},' \
    -e 's,%%SOURCE4%%,%{SOURCE4},' \
    -e 's,%%SOURCE5%%,%{SOURCE5},' \
    -e 's,%%SOURCE6%%,%{SOURCE6},' \
    -e 's,%%SOURCE7%%,%{SOURCE7},' \
    -e 's,%%SOURCE8%%,%{SOURCE8},' \
    -e 's,%%SOURCE9%%,%{SOURCE9},' \
    -e 's,%%SOURCE10%%,%{SOURCE10},' \
    -e 's,%%SOURCE11%%,%{SOURCE11},' \
    -e 's,%%SOURCE12%%,%{SOURCE12},' \
    -e 's,%%SOURCE13%%,%{SOURCE13},' \
    -e 's,%%SOURCE14%%,%{SOURCE14},' \
    -e 's,%%SOURCE15%%,%{SOURCE15},' \
    -e 's,%%SOURCE16%%,%{SOURCE16},' \
    -i tests/reftests/dune.inc

%build

export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'
%configure
%make_build
%install
export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'
%make_install
rm -rf %{buildroot}%{_prefix}/doc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

git config --global init.defaultBranch main
git config --global user.email 'mockbuild@fedoraproject.org'
git config --global user.name 'Mock Builder'
export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'
make tests
%files -f %{oreon_filedir}/main.list
%files -n opam-installer -f %{oreon_filedir}/opam-installer.list

%changelog

%autochangelog
