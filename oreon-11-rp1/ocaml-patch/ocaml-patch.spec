%global source1_hash 7942daf122187ff629ec9c1fe372f39aa5669d55a950f0d451dbc920e4fd7252
%global source0_hash 0c5a5ec82e25d08372e499c2a2810b25d389ed9a7cd948c5eb54ed18f8eeb8d7
%global giturl  https://github.com/hannesm/patch
Name:           ocaml-patch
Version:        3.1.2
Release:        1%{?dist}
Summary:        Parse unified and git diff output and apply patches in memory
License:        ISC
URL:            https://hannesm.github.io/patch/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/patch-%{version}.tar.gz
Source1:        https://codeberg.org/kit-ty-kate/ocaml-patch-tests/archive/main.tar.gz#/ocaml-patch-tests.tar.gz
ExcludeArch:    %{ix86}
%ifarch %{x86_64}
%endif
# oreon:deps
BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
The patch module lets you apply your unified diffs in pure OCaml.

The loosely specified `diff` file format is widely used for transmitting
differences of line-based information.  The motivating example is opam, which
is able to validate updates being cryptographically signed by providing a
unified diff.  In addition, some support for the git diff format is available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%package     -n opatch
Summary:        Command line tool to apply a diff to a directory
%description -n opatch
This package contains a pure OCaml command line tool to apply a unified or git
patch to a directory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n patch-%{version}
tar -C test/data/external --strip-components=1 -xf %{SOURCE1}

%build

%dune_build
%install
%dune_install -s
rm %{buildroot}%{ocamldir}/opatch/META
sed -i '/META/d' .ofiles-opatch
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -n 'Apply a diff to a directory' \
  -o %{buildroot}%{_mandir}/man1/opatch.1 %{buildroot}%{_bindir}/opatch
%ifarch %{x86_64}
%oreon_autofiles opatch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-patch-devel -f %{oreon_filedir}/ocaml-patch-devel.list
%files -n opatch -f %{oreon_filedir}/opatch.list

%changelog

%autochangelog
