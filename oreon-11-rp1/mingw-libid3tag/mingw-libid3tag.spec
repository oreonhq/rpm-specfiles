%global source0_hash 63da4f6e7997278f8a3fef4c6a372d342f705051d1eeb6a46a86b03610e26151
%{?mingw_package_header}
%global _basename libid3tag
Name:           mingw-%{_basename}
Version:        0.15.1b
Release:        43%{?dist}
Summary:        ID3 tag manipulation library
License:        GPL-2.0-or-later
URL:            http://www.underbit.com/products/mad/
Source0:        http://downloads.sourceforge.net/mad/%{_basename}-%{version}.tar.gz
Patch0:         libid3tag-0.15.1b-fix_overflow.patch
Patch1:         libid3tag-mingw.patch
Patch2:         libid3tag-0.15.1b-id3v1-zero-padding.patch
Patch3:         libid3tag-0.15.1b-handle-unknown-encoding.patch
Patch4:         libid3tag-0.15.1b-id3v2-endless-loop.patch
Patch5:         libid3tag-0.15.1b-gperf-size_t.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib
# /oreon:deps
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
sed -i 's|file format pei\*-i386(\.\*architecture: i386)?|file format pe-x86-64|g' build_win64/libtool
%{mingw_make} %{?_smp_mflags}
%install
%{mingw_make} install DESTDIR=%{buildroot}
install -Dpm 644 %{name}32.pc %{buildroot}%{mingw32_libdir}/pkgconfig/id3tag.pc
install -Dpm 644 %{name}64.pc %{buildroot}%{mingw64_libdir}/pkgconfig/id3tag.pc
rm -f %{buildroot}/%{mingw32_libdir}/*.la
rm -f %{buildroot}/%{mingw64_libdir}/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libid3tag -f %{oreon_filedir}/mingw32-libid3tag.list
%files -n mingw64-libid3tag -f %{oreon_filedir}/mingw64-libid3tag.list

%changelog

%autochangelog
