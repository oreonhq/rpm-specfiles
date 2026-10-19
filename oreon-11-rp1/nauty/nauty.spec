%global source0_hash 1e7f595d42411ae2b1423af31f78fea94d0932e5e1abed01eeba04d90505c824
Name:           nauty
Version:        2.9.3
Release:        1%{?dist}
Summary:        Graph canonical labeling and automorphism group computation
%global nautytarver %(tr . _ <<< %{version})
License:        Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND Knuth-CTAN AND GPL-1.0-or-later
URL:            https://pallini.di.uniroma1.it/
Source0:        https://deb.debian.org/debian/pool/main/n/nauty/nauty_2.9.3.orig.tar.gz
Patch:          %{name}-fix-gt_numorbits.patch
Patch:          %{name}-zlib-dimacs2g.patch
Patch:          %{name}-help2man.patch
Patch:          %{name}-shared.patch
Patch:          %{name}-popcnt.patch
Patch:          %{name}-unbundle-cliquer.patch
Patch:          %{name}-uninitialized.patch
Provides:       bundled(planarity)
Requires:       coreutils
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libcliquer)
BuildRequires:  pkgconfig(zlib-ng)
# /oreon:deps
%description
Nauty and Traces are programs for computing automorphism groups of graphs and
digraphs.  (At present, Traces does not accept digraphs.)  They can also
produce a canonical label.  They are written in a portable subset of C, and
run on a considerable number of different systems.

There is a small suite of programs called gtools included in the package.  For
example, geng can generate non-isomorphic graphs very quickly.  There are also
generators for bipartite graphs, digraphs, and multigraphs, and programs for
manipulating files of graphs in a compact format.

%package     -n libnauty
License:        Apache-2.0
Summary:        Library for graph automorphism
%description -n libnauty
Nauty (No AUTomorphisms, Yes?) is a set of procedures for computing
automorphism groups of graphs and digraphs.  This package contains a library
of nauty procedures.

%package     -n libnauty-devel
License:        Apache-2.0
Summary:        Development files for libnauty
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%description -n libnauty-devel
This package contains files needed to develop programs that use libnauty.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}%{nautytarver}

%conf
# Remove the pregenerated makefile
rm -f makefile

# Regenerate the configure script due to the patches
aclocal
autoreconf -fi

# Fix the pkgconfig file
sed -i 's,/usr/local,%{_prefix},' nauty.pc
if [ '%{_lib}' != 'lib' ]; then
    sed -i 's,/lib,/lib64,' nauty.pc
fi

%build

export CFLAGS='%{build_cflags} -fwrapv -I%{_includedir}/cliquer'
export LIBS='-lz-ng'
%configure \
    --enable-ansi \
    --enable-generic \
%ifarch %{ix86} %{x86_64}
    --disable-popcnt \
    --enable-runtime-popcnt \
%endif
    --disable-static \
    --enable-tls
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
make
%install
%make_install
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N -o %{buildroot}%{_mandir}/man1/$(basename $f).1 \
    --version-string=%{version} $f
done
rm %{buildroot}%{_bindir}/pickg
ln countg %{buildroot}%{_bindir}/pickg
mkdir -p %{buildroot}%{_includedir}/nauty
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/nauty
%oreon_autofiles libnauty usr/*/lib*.so.*
%oreon_autofiles libnauty-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

chmod a+x runalltests
LD_LIBRARY_PATH=$PWD/.libs PATH=$PWD:$PATH make check
%files -f %{oreon_filedir}/main.list
%files -n libnauty -f %{oreon_filedir}/libnauty.list
%files -n libnauty-devel -f %{oreon_filedir}/libnauty-devel.list

%changelog

%autochangelog
