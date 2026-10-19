%global source1_hash 20e7afa8535676530875a126092304bc91feb7742a4971fcec99e6cfb77c95db
%global source0_hash 4a1013eebb50f728fc601bdd833b0b2870333c3b3e5a816eeba921d95bec6f15
Name:           glpk
Version:        5.0
Release:        16%{?dist}
Summary:        GNU Linear Programming Kit
License:        GPL-3.0-or-later AND MIT
URL:            https://www.gnu.org/software/glpk/
Source0:        https://ftp.gnu.org/gnu/glpk/glpk-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/glpk/glpk-%{version}.tar.gz.sig
Source2:        gpgkey-D17BF2305981E818.gpg
Patch:          %{name}-4.65-unbundle-zlib.patch
Patch:          %{name}-4.65-unbundle-suitesparse.patch
Patch:          %{name}-4.65-alias.patch
Patch:          %{name}-5.0-bool.patch
Patch:          %{name}-5.0-zlib-ng.patch
Provides:       bundled(minisat) = 1.14.1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gmp-devel
BuildRequires:  gpgverify
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libiodbc)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  suitesparse-devel
# /oreon:deps
%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP), and
other related problems. It is a set of routines written in ANSI C and
organized in the form of a callable library.

GLPK supports the GNU MathProg language, which is a subset of the AMPL
language.

The GLPK package includes the following main components:

 * Revised simplex method.
 * Primal-dual interior point method.
 * Branch-and-bound method.
 * Translator for GNU MathProg.
 * Application program interface (API).
 * Stand-alone LP/MIP solver. 

%package        doc
License:        GFDL-1.3-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a
Summary:        Documentation for %{name}
%description    doc
Documentation subpackage for %{name}.

%package devel
Summary:        Development headers and files for GLPK
Requires:       %{name}%{_isa} = %{version}-%{release}
%description devel
The glpk-devel package contains libraries and headers for developing
applications which use GLPK (GNU Linear Programming Kit).

%package utils
Summary:        GLPK-related utilities and examples
Requires:       %{name}%{_isa} = %{version}-%{release}
%description utils
The glpk-utils package contains the standalone solver program glpsol that uses
GLPK (GNU Linear Programming Kit).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

%conf
# Unbundle zlib and suitesparse
rm -fr src/{amd,colamd,zlib}

%build

export CPPFLAGS="$(pkg-config --cflags libmariadb)"
export LIBS=-ldl
autoreconf -ifs
%configure --disable-static --with-gmp \
           --enable-dl=dlfcn --enable-odbc --enable-mysql
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool
%make_build
%install
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
make check
rm -Rf examples/{.deps,.libs,Makefile*,glpsol,glpsol.o} doc/*.tex
%files -f %{oreon_filedir}/main.list
%files -n glpk-doc -f %{oreon_filedir}/glpk-doc.list
%files -n glpk-devel -f %{oreon_filedir}/glpk-devel.list
%files -n glpk-utils -f %{oreon_filedir}/glpk-utils.list

%changelog

%autochangelog
