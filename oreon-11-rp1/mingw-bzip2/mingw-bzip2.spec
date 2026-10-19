%global source0_hash ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269
%?mingw_package_header
Name:           mingw-bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        MinGW port of bzip2 file compression utility
License:        LicenseRef-Callaway-BSD
URL:            http://www.bzip.org/
Source0:        https://sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz
BuildArch:      noarch
Patch12:        bzip2-1.0.5-autoconfiscated.patch
Patch13:        bzip2-use-cdecl-calling-convention.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

This package contains development tools and libraries for use when
cross-compiling Windows software in Fedora.

# Win32
%package -n mingw32-bzip2
Summary:        32 Bit version of bzip2 for Windows
%description -n mingw32-bzip2
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

This package contains development tools and libraries for use when
cross-compiling Windows software in Fedora.

%package -n mingw32-bzip2-static
Summary:        Static library for mingw32-bzip2 development
Requires:       mingw32-bzip2 = %{version}-%{release}
%description -n mingw32-bzip2-static
Static library for mingw32-bzip2 development.

# Win64
%package -n mingw64-bzip2
Summary:        64 Bit version of bzip2 for Windows
%description -n mingw64-bzip2
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

This package contains development tools and libraries for use when
cross-compiling Windows software in Fedora.

%package -n mingw64-bzip2-static
Summary:        Static library for mingw64-bzip2 development
Requires:       mingw64-bzip2 = %{version}-%{release}
%description -n mingw64-bzip2-static
Static library for mingw64-bzip2 development.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n bzip2-%{version}

%patch -P12 -p1 -b .autoconfiscated

%patch -P13 -p1 -b .cdecl

sh ./autogen.sh

%build

%mingw_configure
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
for dir in $RPM_BUILD_ROOT%{mingw32_bindir} $RPM_BUILD_ROOT%{mingw64_bindir} ; do
pushd $dir
rm bzcmp.exe bzegrep.exe bzfgrep.exe bzless.exe
ln -s bzdiff bzcmp
ln -s bzgrep bzegrep
ln -s bzgrep bzfgrep
ln -s bzmore bzless
popd
done
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man1
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man1
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libbz2.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libbz2.la
%oreon_autofiles mingw32-bzip2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-bzip2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-bzip2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-bzip2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-bzip2 -f %{oreon_filedir}/mingw32-bzip2.list
%files -n mingw32-bzip2-static -f %{oreon_filedir}/mingw32-bzip2-static.list
%files -n mingw64-bzip2 -f %{oreon_filedir}/mingw64-bzip2.list
%files -n mingw64-bzip2-static -f %{oreon_filedir}/mingw64-bzip2-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.8-17
- Import
