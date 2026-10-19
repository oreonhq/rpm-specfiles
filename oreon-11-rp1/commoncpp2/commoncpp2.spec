%global source0_hash 53ced4aff74e28a1d8018eb2b4974519028db3c12471ab6dff1c873578c9af4e
Name:          commoncpp2
Version:       1.8.1
Release:        1%{?dist}
Summary:        GNU Common C++ class framework
License:       LicenseRef-Callaway-GPLv2+-with-exceptions
URL:           http://www.gnu.org/software/commoncpp/
Source0:        https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz
Patch1:        commoncpp2-statfix.patch
Patch2:        commoncpp2-gcc9.patch
Patch3:        commoncpp2_sizeof.patch
Patch4:        commoncpp2_obsoletem4.patch
Patch5:        commoncpp2_setgroups.patch
Patch6:        commoncpp2_tests.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
GNU Common C++ is a portable and highly optimized class framework for writing
C++ applications that need to use threads, sockets, XML parsing,
serialization, config files, etc. This framework offers a class foundation
that hides platform differences from your C++ application so that you need
not write platform specific code. GNU Common C++ has been ported to compile
natively on most platforms which support posix threads.

%package devel
Summary:       Header files and libraries for %{name} development
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      libxml2-devel%{?_isa}
Requires:      zlib-devel%{?_isa}
%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.

%package doc
Summary:       Developer documentation for %{name}
License:       LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-GFDL
BuildArch:     noarch
%description doc
The %{name}-doc package contains the developer documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ifv
%configure \
    --disable-static \
    --disable-dependency-tracking
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
make CXX="g++ -std=c++14"
pushd tests
%make_build CXX="g++ -std=c++14"
popd
%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles commoncpp2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles commoncpp2-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd tests
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test.sh
popd
%files -f %{oreon_filedir}/main.list
%files -n commoncpp2-devel -f %{oreon_filedir}/commoncpp2-devel.list
%files -n commoncpp2-doc -f %{oreon_filedir}/commoncpp2-doc.list

%changelog

%autochangelog
