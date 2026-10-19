%global source0_hash 80cddc18212e00beba0fcd64b7bdf64e56010438e23c10968c9f526a6d88fec3
%global debug_package %{nil}
Name:           fflas-ffpack
Version:        2.5.0
Release:        1%{?dist}
Summary:        Finite field linear algebra subroutines
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND
                CECILL-B AND
                FSFAP AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later AND
                GPL-2.0-or-later WITH Autoconf-exception-generic
                }
URL:            https://linbox-team.github.io/fflas-ffpack/
%global forgeurl https://github.com/linbox-team/fflas-ffpack
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/releases/download/v%{version}/fflas_ffpack-%{version}.tar.bz2
Source1:        fflas-ffpack-config.1
Patch:          0001-fix-perf-publisher.patch
Patch:          %{forgeurl}/pull/384.patch
Patch:          %{forgeurl}/pull/385.patch
Patch:          %{forgeurl}/pull/379.patch
ExcludeArch:    %{ix86}
%global common_description %{expand: \
The FFLAS-FFPACK library provides a set of basic routines for linear algebra
over a finite field or the ring of integers with dense and sparse matrices.}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(givaro)
# /oreon:deps
%description
%{common_description}

%package devel
Summary:        Header files for developing with fflas-ffpack
Requires:       givaro-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}
Provides:       fflas-ffpack-static = %{version}-%{release}
%description devel
%{common_description}

This package provides the header files for developing applications that use
FFLAS-FFPACK.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fflas_ffpack-%{version} -p1
# Skip test-echelon for now due to failures.
# See https://github.com/linbox-team/fflas-ffpack/issues/282
sed -i '/^[[:blank:]]*test-echelon/d' tests/Makefile.am

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines
sed -i 's,%{_bindir}/env bash,%{_bindir}/bash,' fflas-ffpack-config.in

# Remove parts of the configure script that select non-default architectures
# and ABIs. On x86_64, we could rely on up to SSE2, but there are no explicit
# SIMD routines below SSE4.1 in the library, so it is not worth worrying about.
sed -i '/INSTR_SET/,/fabi-version/d' configure.ac

%conf
# Regenerate configure after monkeying with configure.ac
autoreconf --force --install --verbose

# We define __FFLASFFPACK_HAVE_CBLAS to bypass CBLAS detection so that the
# configure script detects USER LAPACK. Ideally, this would be reported
# upstream, but it’s difficult to describe the problem precisely.
%configure \
  --disable-static \
  --enable-openmp \
  --without-archnative \
  --with-blas-cflags="$(pkgconf --cflags flexiblas) -D__FFLASFFPACK_HAVE_CBLAS=1" \
  --with-blas-libs="$(pkgconf --libs flexiblas)"
chmod -v a+x fflas-ffpack-config

%build

%make_build
%install
%make_install
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p '%{SOURCE1}'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export FLEXIBLAS=netlib
%make_build check
%files -f %{oreon_filedir}/main.list
%files -n fflas-ffpack-devel -f %{oreon_filedir}/fflas-ffpack-devel.list

%changelog

%autochangelog
