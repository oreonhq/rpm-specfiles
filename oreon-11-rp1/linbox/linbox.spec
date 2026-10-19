%global source0_hash 490de446eecf260de2d9df9b5663c566b75a59e18c14b1f46a2d84fb08deb490
%global giturl  https://github.com/linbox-team/linbox
Name:           linbox
Version:        1.7.1
%global so_version 0
Release:        1%{?dist}
Summary:        C++ Library for High-Performance Exact Linear Algebra
License:        LGPL-2.1-or-later
URL:            https://linalg.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{giturl}/pull/326.patch
ExcludeArch:    %{ix86}
Obsoletes:      linbox-doc < 1.7.0-1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expat-devel
BuildRequires:  fflas-ffpack-devel
BuildRequires:  flexiblas-devel
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  givaro-devel
BuildRequires:  iml-devel
BuildRequires:  libfplll-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ntl-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  saclib-devel
BuildRequires:  tinyxml2-devel
# /oreon:deps
%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package        devel
Summary:        Development libraries/headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fflas-ffpack-devel%{?_isa}
Requires:       iml-devel%{?_isa}
Requires:       libfplll-devel%{?_isa}
Requires:       ntl-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}
%description    devel
Headers and libraries for development with %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Adapt to the way saclib is packaged in Fedora
sed -e 's,include/saclib,&/saclib,' \
    -e '/saclib\.h/,+1s/__GNU_MP_VERSION < 3/SACMAJVERS < 2/' \
    -i macros/saclib-check.m4

# Remove spurious executable bits
find -O3 . \( -name \*.h -o -name \*.inl \) -perm /0111 -exec chmod a-x {} +

%build

autoreconf -fi
export CPPFLAGS='-I%{_includedir}/saclib'
%configure --disable-silent-rules \
  --disable-static \
  --with-ocl=yes \
  --with-saclib=yes \
  --without-archnative
chmod -v a+x linbox-config
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
sed -i 's|-O2|-Og|g' tests/Makefile
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -vrf '%{buildroot}%{_prefix}/doc'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=$PWD/linbox/.libs %make_build check -j1
%files -f %{oreon_filedir}/main.list
%files -n linbox-devel -f %{oreon_filedir}/linbox-devel.list
%files -n linbox-doc -f %{oreon_filedir}/linbox-doc.list

%changelog

%autochangelog
