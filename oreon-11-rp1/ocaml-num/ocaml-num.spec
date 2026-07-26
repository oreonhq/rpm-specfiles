%global source0_hash b5cce325449aac746d5ca963d84688a627cca5b38d41e636cf71c68b60495b3e

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
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
Release:        4%{?dist}
Summary:        Legacy Num library for arbitrary-precision integer and rational arithmetic
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://github.com/ocaml/num
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Downstream patch to add -g flag.
Patch:          0001-src-Add-g-flag-to-mklib.patch

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Longident -i Topdirs

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

# Version 1.6 removed the directory directive from the META file.  Somehow, we
# now install the files in the wrong directory.  Probably one of the lines
# above needs to be tweaked, but I am unsure how.
mv %{buildroot}%{ocamldir}/*.{a,cm*,mli} %{buildroot}%{ocamldir}/num

%ocaml_files

%files -f .ofiles
%doc Changelog README.md
%license LICENSE

%files devel -f .ofiles-devel
%license LICENSE

%changelog
%autochangelog
