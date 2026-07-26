%global source0_hash 53ced4aff74e28a1d8018eb2b4974519028db3c12471ab6dff1c873578c9af4e

Name:          commoncpp2
Version:       1.8.1
Release:       37%{?dist}
Summary:       GNU Common C++ class framework

# Library is GPLv2+ with exceptions
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions
URL:           http://www.gnu.org/software/commoncpp/
Source0:       https://ftp.gnu.org/gnu/commoncpp/%{name}-%{version}.tar.gz

# Fix mkfifo modes: S_IREAD | S_IWRITE -> S_IRUSR | S_IWUSR
Patch1:        commoncpp2-statfix.patch
# Fix build against GCC9+
Patch2:        commoncpp2-gcc9.patch
# Fix two occurences of incorrect sizeof usage
Patch3:        commoncpp2_sizeof.patch
# Replace obsolete macros
Patch4:        commoncpp2_obsoletem4.patch
# Call setgroups before setuid
Patch5:        commoncpp2_setgroups.patch
# Disable thread1 test which is badly written and hangs (or takes a very long time)
# Add return code to detect failure/success
Patch6:        commoncpp2_tests.patch

BuildRequires: automake autoconf libtool
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: make

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
# Automatically converted from old format: GPLv2+ with exceptions and GFDL - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-GFDL
BuildArch:     noarch

%description doc
The %{name}-doc package contains the developer documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Kill rpath
autoreconf -ifv
%configure \
    --disable-static \
    --disable-dependency-tracking

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Parallel build occasionally broken
make CXX="g++ -std=c++14"

# Build tests
pushd tests
%make_build CXX="g++ -std=c++14"
popd

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Drop info index
rm -f %{buildroot}%{_infodir}/dir

%check
pushd tests
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./test.sh
popd

%files
%doc README ChangeLog
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/ccgnu2-config
%{_includedir}/cc++/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libccext2.pc
%{_libdir}/pkgconfig/libccgnu2.pc
%{_datadir}/aclocal/ost_check2.m4

%files doc
%doc doc/html
%{_infodir}/commoncpp2.info*

%changelog
%autochangelog
