%global source0_hash 8d34b3860192f6d2ac017537884b099b13a492ed4884130c65da5173d5162590

Summary:	Library for easy parsing of XMP metadata
Name:		exempi
Version:	2.6.4
Release:	9%{?dist}
License:	BSD-3-Clause
URL:		http://libopenraw.freedesktop.org/wiki/Exempi
Source0:        https://gitlab.freedesktop.org/libopenraw/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	gcc-c++
BuildRequires:	boost-devel expat-devel zlib-devel pkgconfig
# Work around for aarch64 support (https://bugzilla.redhat.com/show_bug.cgi?id=925327)
BuildRequires:	autoconf automake libtool
BuildRequires: make
Provides:	bundled(md5-polstra)

%description
Exempi provides a library for easy parsing of XMP metadata. It is a port of 
Adobe XMP SDK to work on UNIX and to be build with GNU automake.
It includes XMPCore and XMPFiles.

%package devel
Summary:	Headers for developing programs that will use %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains the libraries and header files needed for
developing with exempi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
libtoolize -vi
NOCONFIGURE=1 ./autogen.sh
# BanEntityUsage needed for #888765
%configure CPPFLAGS="-I%{_includedir} -fno-strict-aliasing -DBanAllEntityUsage=1"

# Disable rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
%ifarch s390x
# testcore test fails on big endian arches since exempi 2.5.2:
# https://gitlab.freedesktop.org/libopenraw/exempi/-/issues/23
make check || [ "$(grep '^FAIL:' exempi/test-suite.log)" = "FAIL: tests/testcore" ]
%else
make check
%endif

%install
%make_install

rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/*.a

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/exempi
%{_libdir}/libexempi.so.8*
%{_mandir}/man1/exempi.1*

%files devel
%{_includedir}/exempi-2.0/
%{_libdir}/libexempi.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.4-9
- Prepare for Oreon 11 (RP1)
