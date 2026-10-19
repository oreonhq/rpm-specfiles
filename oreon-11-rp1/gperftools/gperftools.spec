%global source0_hash 2a28d54af7303f56583c051efd6e011b75a109262d0c763a2a242dff94eb59b2
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:		gperftools
Version:	2.18.90
Release:        1%{?dist}
License:	BSD-3-Clause
Summary:        Very fast malloc and performance analysis tools
URL:		https://github.com/gperftools/gperftools
Source0:        https://github.com/gperftools/gperftools/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch1:		gperftools-2.17-disable-generic-dynamic-tls.patch
ExcludeArch:	s390
Requires:	gperftools-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libunwind-devel
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Perf Tools is a collection of performance analysis tools, including a
high-performance multi-threaded malloc() implementation that works
particularly well with threads and STL, a thread-friendly heap-checker,
a heap profiler, and a cpu-profiler.

This is a metapackage which pulls in all of the gperftools binaries,
libraries, and development headers, so that you can use them.

%package devel
Summary:	Development libraries and headers for gperftools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Provides:	google-perftools-devel = %{version}-%{release}
Obsoletes:	google-perftools-devel < 2.0
%description devel
Libraries and headers for developing applications that use gperftools.

%package libs
Summary:	Libraries provided by gperftools
Provides:	google-perftools-libs = %{version}-%{release}
Obsoletes:	google-perftools-libs < 2.0
%description libs
Libraries provided by gperftools, including libtcmalloc and libprofiler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%autopatch -p1
sed -i 's/\r//' README_windows.txt
chmod -x src/*.h src/*.cc
autoreconf -ifv

%build

CFLAGS=`echo $RPM_OPT_FLAGS -fno-strict-aliasing -Wno-unused-local-typedefs -DTCMALLOC_LARGE_PAGES | sed -e 's|-fexceptions||g'`
CXXFLAGS=`echo $RPM_OPT_FLAGS -fno-strict-aliasing -Wno-unused-local-typedefs -DTCMALLOC_LARGE_PAGES | sed -e 's|-fexceptions||g'`
%configure \
%ifarch aarch64
	--disable-general-dynamic-tls \
%endif
	--disable-dynamic-sized-delete-support \
	--disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
%install
%make_install docdir=%{_pkgdocdir}/
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -rf %{buildroot}%{_pkgdocdir}/INSTALL
%ldconfig_scriptlets libs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gperftools-devel -f %{oreon_filedir}/gperftools-devel.list
%files -n gperftools-libs -f %{oreon_filedir}/gperftools-libs.list

%changelog

%autochangelog

