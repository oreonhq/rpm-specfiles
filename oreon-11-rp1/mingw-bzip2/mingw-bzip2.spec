%global source0_hash none

%?mingw_package_header

Name:           mingw-bzip2
Version:        1.0.8
Release:        17%{?dist}
Summary:        MinGW port of bzip2 file compression utility

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.bzip.org/
Source0:        http://www.bzip.org/%{version}/bzip2-%{version}.tar.gz

BuildArch:      noarch

Patch12:        bzip2-1.0.5-autoconfiscated.patch

# Export all symbols using the cdecl calling convention instead of
# stdcall as it is also done by various other downstream distributors
# (like mingw.org and gnuwin32) and it resolves various autoconf and
# cmake detection issues (RHBZ #811909, RHBZ #812573)
# Patch is taken from the gnuwin32 project
Patch13:        bzip2-use-cdecl-calling-convention.patch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  autoconf, automake, libtool


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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n bzip2-%{version}

%patch -P12 -p1 -b .autoconfiscated

%patch -P13 -p1 -b .cdecl

sh ./autogen.sh


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# The binaries which are symlinks contain the full buildroot
# name in the symlink, so replace those.
for dir in $RPM_BUILD_ROOT%{mingw32_bindir} $RPM_BUILD_ROOT%{mingw64_bindir} ; do
pushd $dir
rm bzcmp.exe bzegrep.exe bzfgrep.exe bzless.exe
ln -s bzdiff bzcmp
ln -s bzgrep bzegrep
ln -s bzgrep bzfgrep
ln -s bzmore bzless
popd
done


# Remove the manpages, they're duplicates of the native package,
# and located in the wrong place anyway.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man1
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man1

# Remove libtool .la files.
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libbz2.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libbz2.la

# Win32
%files -n mingw32-bzip2
%doc COPYING
%{mingw32_bindir}/libbz2-1.dll
%{mingw32_bindir}/bunzip2.exe
%{mingw32_bindir}/bzcat.exe
%{mingw32_bindir}/bzcmp
%{mingw32_bindir}/bzdiff
%{mingw32_bindir}/bzegrep
%{mingw32_bindir}/bzfgrep
%{mingw32_bindir}/bzgrep
%{mingw32_bindir}/bzip2.exe
%{mingw32_bindir}/bzip2recover.exe
%{mingw32_bindir}/bzless
%{mingw32_bindir}/bzmore
%{mingw32_includedir}/bzlib.h
%{mingw32_libdir}/libbz2.dll.a
%{mingw32_libdir}/pkgconfig/bzip2.pc

%files -n mingw32-bzip2-static
%{mingw32_libdir}/libbz2.a

# Win64
%files -n mingw64-bzip2
%doc COPYING
%{mingw64_bindir}/libbz2-1.dll
%{mingw64_bindir}/bunzip2.exe
%{mingw64_bindir}/bzcat.exe
%{mingw64_bindir}/bzcmp
%{mingw64_bindir}/bzdiff
%{mingw64_bindir}/bzegrep
%{mingw64_bindir}/bzfgrep
%{mingw64_bindir}/bzgrep
%{mingw64_bindir}/bzip2.exe
%{mingw64_bindir}/bzip2recover.exe
%{mingw64_bindir}/bzless
%{mingw64_bindir}/bzmore
%{mingw64_includedir}/bzlib.h
%{mingw64_libdir}/libbz2.dll.a
%{mingw64_libdir}/pkgconfig/bzip2.pc

%files -n mingw64-bzip2-static
%{mingw64_libdir}/libbz2.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.8-17
- Import
