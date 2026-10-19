%global source0_hash 837b2869aa001b1d9c72cc70ac02cc603ff93632f0c67936dacb3bda91c58d60
Name:           ocaml-gsl
Version:        1.25.1
Release:        7%{?dist}
Summary:        Interface to GSL (GNU scientific library) for OCaml
License:        GPL-3.0-or-later
ExcludeArch:    %{arm} %{ix86}
URL:            https://github.com/mmottl/gsl-ocaml
VCS:            git:%{url}.git
Source0:        https://github.com/mmottl/gsl-ocaml/releases/download/%{version}/gsl-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl)
# /oreon:deps
%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gsl-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gsl-%{version}
%oreon_prep
%build

export GSL_CBLAS_LIB="-lflexiblas"
%dune_build
%install
export GSL_CBLAS_LIB="-lflexiblas"
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export GSL_CBLAS_LIB="-lflexiblas"
%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-gsl-devel -f %{oreon_filedir}/ocaml-gsl-devel.list

%changelog

%autochangelog
