%global source0_hash b5cce325449aac746d5ca963d84688a627cca5b38d41e636cf71c68b60495b3e
ExcludeArch: %{ix86}
%ifarch %{ocaml_native_compiler}
%ifarch x86_64
%global num_arch amd64
%else
%ifarch aarch64
%global num_arch arm64
%else
%ifarch ppc64le
%global num_arch power
%else
%global num_arch %{_arch}
%endif
%endif
%endif
%else
%global num_arch none
%endif
Name:           ocaml-num
Version:        1.6
Release:        1%{?dist}
Summary:        Legacy Num library for arbitrary-precision integer and rational arithmetic
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/num
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml/num/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-src-Add-g-flag-to-mklib.patch
%global __ocaml_requires_opts -i Longident -i Topdirs
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
This library implements arbitrary-precision arithmetic on big integers
and on rationals.

This is a legacy library. It used to be part of the core OCaml
distribution (in otherlibs/num) but is now distributed separately. New
applications that need arbitrary-precision arithmetic should use the
Zarith library (https://github.com/ocaml/Zarith) instead of the Num
library, and older applications that already use Num are encouraged to
switch to Zarith. Zarith delivers much better performance than Num and
has a nicer API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n num-%{version} -p1

# FIXME: ocaml-findlib complains that num is already installed without this
sed -i 's,cp \(META.num META\),mv \1,' src/Makefile

%build

make opam-modern PROFILE=release ARCH=%{num_arch} FLAMBDA=true
%check

make -j1 test PROFILE=release ARCH=%{num_arch} FLAMBDA=true
%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%make_install ARCH=%{num_arch}
mv %{buildroot}%{ocamldir}/*.{a,cm*,mli} %{buildroot}%{ocamldir}/num
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-num-devel -f %{oreon_filedir}/ocaml-num-devel.list

%changelog

%autochangelog
