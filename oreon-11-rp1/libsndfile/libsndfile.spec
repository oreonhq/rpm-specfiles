%global source0_hash 3799ca9924d3125038880367bf1468e53a1b7e3686a934f098b7e1d286cdb80e
Summary:        Library for reading and writing sound files
Name:		libsndfile
Version:	1.2.2
Release:        11%{?dist}
License:	LGPL-2.1-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:		http://libsndfile.github.io/libsndfile/
Source0:        https://github.com/libsndfile/libsndfile/releases/download/%{version}/libsndfile-%{version}.tar.xz
Patch0:		libsndfile-1.0.25-system-gsm.patch
Patch1:	libsndfile-1.2.2-cve-2024-50612.patch
Patch2:	libsndfile-1.2.2-stdbool.patch
Patch3: libsndfile-1.2.2-tests-opus.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  lame-devel
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mpg123-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sqlite-devel
# /oreon:deps
%description
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface. It can
currently read/write 8, 16, 24 and 32-bit PCM files as well as 32 and
64-bit floating point WAV files and a number of compressed formats. It
compiles and runs on *nix, MacOS, and Win32.

%package devel
Summary:	Development files for libsndfile
Requires:	%{name}%{?_isa} = %{version}-%{release} pkgconfig
%description devel
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains files needed to develop with libsndfile.

%package utils
Summary:	Command Line Utilities for libsndfile
Requires:	%{name} = %{version}-%{release}
%description utils
libsndfile is a C library for reading and writing sound files such as
AIFF, AU, WAV, and others through one standard interface.
This package contains command line utilities for libsndfile.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .system-gsm
%patch -P 1 -p1 -b .cve-2024-50612
%patch -P 2 -p1 -b .stdbool
%patch -P 3 -p1 -b .tests-opus
rm -r src/GSM610

%build

autoreconf -I M4 -fiv # for system-gsm patch
%configure \
	--disable-dependency-tracking \
	--enable-sqlite \
	--enable-alsa \
	--enable-largefile \
	--enable-mpeg \
	--disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -rf __docs
mkdir __docs
cp -pR $RPM_BUILD_ROOT%{_docdir}/%{name}/* __docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
find %{buildroot} -type f -name "*.la" -delete
mv %{buildroot}%{_includedir}/sndfile.h \
   %{buildroot}%{_includedir}/sndfile-%{__isa_bits}.h
cat > %{buildroot}%{_includedir}/sndfile.h <<EOF
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

LD_LIBRARY_PATH=$PWD/src/.libs make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libsndfile-devel -f %{oreon_filedir}/libsndfile-devel.list
%files -n libsndfile-utils -f %{oreon_filedir}/libsndfile-utils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-11
- Prepare for Oreon 11 (RP1)
