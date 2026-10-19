%global source0_hash 1779921d2f76caae0ec02f1614025105728f971c6e961f497ee9fa9f3e824cbc
Name:           gmp-ecm
Version:        7.0.7
Release:        1%{?dist}
Summary:        Elliptic Curve Method for Integer Factorization
License:        GPL-3.0-or-later
URL:            https://gitlab.inria.fr/zimmerma/ecm
Source0:        https://gitlab.inria.fr/zimmerma/ecm/-/archive/git-%{version}/ecm-git-%{version}.tar.bz2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  make
# /oreon:deps
%description
Programs and libraries employing elliptic curve method for factoring
integers (with GMP for arbitrary precision integers).

%package        libs
Summary:        Elliptic Curve Method library
License:        LGPL-3.0-or-later
%description    libs
The %{name} elliptic curve method library.

%package        devel
Summary:        Files useful for %{name} development
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description    devel
The libraries and header files for using %{name} for development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ecm-git-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix non-UTF-8 encodings
for badfile in AUTHORS ; do
  iconv -f iso-8859-1 -t utf-8 -o $badfile.UTF-8 $badfile 
  touch -r $badfile $badfile.UTF-8
  mv $badfile.UTF-8 $badfile
done

# Fix the FSF's address
for badfile in `grep -FRl 'Fifth Floor' .`; do
  sed -e 's/Fifth Floor/Suite 500/' -e 's/02111-1307/02110-1335/' \
      -i.orig $badfile
  fixtimestamp $badfile
done

# Generate the configure script
autoreconf -fi .

%build

%configure --disable-static --enable-shared --enable-openmp \
  --disable-gmp-cflags \
%ifarch %{ix86}
  --enable-sse2 \
%else
  --disable-sse2 \
%endif
  CFLAGS='%{build_cflags} -Wa,--noexecstack' \
  LDFLAGS='%{build_ldflags} -Wl,-z,noexecstack -lgmp -lgomp'
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
%make_build
%install
%make_install INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
pushd $RPM_BUILD_ROOT%{_bindir}
  mv ecm %{name}
popd
pushd $RPM_BUILD_ROOT%{_mandir}/man1
  for file in ecm.1*; do
    mv $file ${file/ecm/%{name}}
  done
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$PWD/.libs
make check
%files -f %{oreon_filedir}/main.list
%files -n gmp-ecm-libs -f %{oreon_filedir}/gmp-ecm-libs.list
%files -n gmp-ecm-devel -f %{oreon_filedir}/gmp-ecm-devel.list

%changelog

%autochangelog
