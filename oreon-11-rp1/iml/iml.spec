%global source0_hash 1dad666850895a5709b00b97422e2273f293cfadea7697a9f90b90953e847c2a
%bcond autoreconf 1
Name:           iml
Version:        1.0.5
%global so_version 0
Release:        1%{?dist}
Summary:        Finds solutions to systems of linear equations over integers
License:        BSD-3-Clause
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                X11
                }
URL:            https://cs.uwaterloo.ca/~astorjoh/iml.html
Source0:        https://cs.uwaterloo.ca/~astorjoh/iml-%{version}.tar.bz2
Source1:        iml-license-clarification.eml
ExcludeArch:    %{ix86}
%if %{with autoreconf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
IML provides efficient routines to compute exact solutions to dense systems of
linear equations over the integers. The following functionality is provided:
  • Nonsingular rational system solving.
  • Compute the right nullspace of an integer matrix.
  • Certified linear system solving.

%package        devel
Summary:        Development files for iml
Requires:       iml%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}
%description    devel
The iml-devel package contains libraries and header files for developing
applications that use iml.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp -p '%{SOURCE1}' .
awk  '/Copyright notice/ {n=1}; n && /\*\// {n=0}; n' src/iml.h |
  sed -r 's/^ \* ?//' > LICENSE
rm -v cblas.h

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

%configure \
  --enable-shared \
  --disable-static \
  --with-cblas="$(pkgconf --libs flexiblas)" \
  --with-cblas-include="$(pkgconf --cflags flexiblas | sed -r 's/^-I//')"

# Get rid of undesirable hardcoded rpaths; work around libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%build

%make_build
%install
%make_install
rm -vr '%{buildroot}%{_datadir}/iml'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH="${PWD}/src/.libs" %make_build check
%files -f %{oreon_filedir}/main.list
%files -n iml-devel -f %{oreon_filedir}/iml-devel.list

%changelog

%autochangelog
