%global source0_hash 837b2869aa001b1d9c72cc70ac02cc603ff93632f0c67936dacb3bda91c58d60

Name:           ocaml-gsl
Version:        1.25.1
Release:        7%{?dist}
Summary:        Interface to GSL (GNU scientific library) for OCaml
License:        GPL-3.0-or-later

# "Architectures with double-word alignment for doubles are not supported"
# Specifically you should look at this file:
# %%{_libdir}/ocaml/caml/config.h
# and if it has '#define ARCH_ALIGN_DOUBLE' then it is not supported,
# but if it has '#undef ARCH_ALIGN_DOUBLE' then it is OK.
#
# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{arm} %{ix86}

URL:            https://github.com/mmottl/gsl-ocaml
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/gsl-%{version}.tbz

BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl) >= 2.0

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

%autosetup -n gsl-%{version} -p1

%build
export GSL_CBLAS_LIB="-lflexiblas"
%dune_build

%install
export GSL_CBLAS_LIB="-lflexiblas"
%dune_install

%check
export GSL_CBLAS_LIB="-lflexiblas"
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc examples
%license LICENSE.md

%changelog
%autochangelog
