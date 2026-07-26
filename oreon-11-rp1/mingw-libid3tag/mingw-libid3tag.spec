%global source0_hash 63da4f6e7997278f8a3fef4c6a372d342f705051d1eeb6a46a86b03610e26151

%{?mingw_package_header}

%global _basename libid3tag

Name:           mingw-%{_basename}
Version:        0.15.1b
Release:        43%{?dist}
Summary:        ID3 tag manipulation library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.underbit.com/products/mad/
Source0:        http://downloads.sourceforge.net/mad/%{_basename}-%{version}.tar.gz
# Fix CVE-2008-2109 (rhbz#445812)
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
# Build libraries with "-no-undefined"
Patch1:         libid3tag-mingw.patch
Patch2:         libid3tag-0.15.1b-id3v1-zero-padding.patch
Patch3:         libid3tag-0.15.1b-handle-unknown-encoding.patch
Patch4:         libid3tag-0.15.1b-id3v2-endless-loop.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=869598
Patch5:         libid3tag-0.15.1b-gperf-size_t.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib >= 1.1.4

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib >= 1.1.4

BuildRequires:  gperf

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%package -n     mingw32-%{_basename}
Summary:        ID3 tag manipulation library

%description -n mingw32-%{_basename}
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.
This is the MinGW version, built for the win32 target.

%package -n     mingw64-%{_basename}
Summary:        ID3 tag manipulation library

%description -n mingw64-%{_basename}
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.
This is the MinGW version, built for the win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_basename}-%{version}
%patch -P0 -p0 -b .CVE-2008-2109
%patch -P1 -p0 -b .mingw
%patch -P2 -p1 -b .zero-padding
%patch -P3 -p1 -b .unknown-encoding
%patch -P4 -p0 -b .endless-loop
%patch -P5 -p1 -b .gperf

# Force these files to be regenerated from the .gperf sources.
rm compat.c frametype.c

# *.pc originally from the Debian package.
cat << \EOF > %{name}32.pc
prefix=%{mingw32_prefix}
exec_prefix=%{mingw32_exec_prefix}
libdir=%{mingw32_libdir}
includedir=%{mingw32_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -lid3tag
Cflags:
EOF

cat << \EOF > %{name}64.pc
prefix=%{mingw64_prefix}
exec_prefix=%{mingw64_exec_prefix}
libdir=%{mingw64_libdir}
includedir=%{mingw64_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -lid3tag
Cflags:
EOF

%build
%{mingw_configure} --disable-dependency-tracking --disable-static

# Fix libtool to recognize win64 archives
sed -i 's|file format pei\*-i386(\.\*architecture: i386)?|file format pe-x86-64|g' build_win64/libtool

%{mingw_make} %{?_smp_mflags}

%install
%{mingw_make} install DESTDIR=%{buildroot}
install -Dpm 644 %{name}32.pc %{buildroot}%{mingw32_libdir}/pkgconfig/id3tag.pc
install -Dpm 644 %{name}64.pc %{buildroot}%{mingw64_libdir}/pkgconfig/id3tag.pc
rm -f %{buildroot}/%{mingw32_libdir}/*.la
rm -f %{buildroot}/%{mingw64_libdir}/*.la

%files -n mingw32-%{_basename}
%doc CHANGES CREDITS README
%license COPYING COPYRIGHT
%{mingw32_bindir}/libid3tag-0.dll
%{mingw32_includedir}/id3tag.h
%{mingw32_libdir}/libid3tag.dll.a
%{mingw32_libdir}/pkgconfig/id3tag.pc

%files -n mingw64-%{_basename}
%doc CHANGES CREDITS README
%license COPYING COPYRIGHT
%{mingw64_bindir}/libid3tag-0.dll
%{mingw64_includedir}/id3tag.h
%{mingw64_libdir}/libid3tag.dll.a
%{mingw64_libdir}/pkgconfig/id3tag.pc

%changelog
%autochangelog
