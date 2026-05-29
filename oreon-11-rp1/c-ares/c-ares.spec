%global source0_hash 912dd7cc3b3e8a79c52fd7fb9c0f4ecf0aaa73e45efda880266a2d6e26b84ef5

%global use_cmake 1

Summary: A library that performs asynchronous DNS operations
Name: c-ares
Version: 1.34.6
Release: 3%{?dist}
License: MIT
URL: http://c-ares.org/
Source0:        https://github.com/c-ares/c-ares/releases/download/v1.34.6/c-ares-1.34.6.tar.gz
BuildRequires: gcc
%if %{use_cmake}
BuildRequires: cmake
%else
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif
BuildRequires: make

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package devel
Summary: Development files for c-ares
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries needed to
compile applications or shared objects that use c-ares.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# f=CHANGES ; iconv -f iso-8859-1 -t utf-8 $f -o $f.utf8 ; mv $f.utf8 $f

%build
# autoreconf -if
# %%configure --enable-shared --disable-static \
#            --disable-dependency-tracking
%if %{use_cmake}
%{cmake} -DCARES_BUILD_TOOLS:BOOL=OFF
%cmake_build
%else
autoreconf -if
%configure --enable-shared --disable-static \
           --disable-dependency-tracking
%{__make} %{?_smp_mflags}
%endif

%install
%if %{use_cmake}
%cmake_install
%else
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libcares.la
%endif

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md RELEASE-NOTES.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/ares.h
%{_includedir}/ares_build.h
%{_includedir}/ares_dns.h
%{_includedir}/ares_dns_record.h
%{_includedir}/ares_nameser.h
# %%{_includedir}/ares_rules.h
%{_includedir}/ares_version.h
%{_libdir}/*.so
%if %{use_cmake}
%{_libdir}/cmake/c-ares/
%endif
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.34.6-3
- Prepare for Oreon 11 (RP1)
