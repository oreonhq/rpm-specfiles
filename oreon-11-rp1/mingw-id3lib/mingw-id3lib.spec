%global source0_hash 2749cc3c0cd7280b299518b1ddf5a5bcfe2d1100614519b68702230e26c7d079

%{?mingw_package_header}

%global _basename id3lib

Summary:        Library for manipulating ID3v1 and ID3v2 tags
Name:           mingw-%{_basename}
Version:        3.8.3
Release:        59%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.id3lib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/id3lib/%{_basename}-%{version}.tar.gz
Patch0:         id3lib-3.8.3-io_helpers-163101.patch
Patch1:         id3lib-3.8.3-mkstemp.patch
Patch2:         id3lib-3.8.3-includes.patch
Patch3:         http://launchpadlibrarian.net/33114077/id3lib-vbr_buffer_overflow.diff
Patch4:         id3lib-3.8.3-autoreconf.patch
Patch5:         id3lib-3.8.3-mingw.patch
Patch6:         http://anonscm.debian.org/viewvc/collab-maint/deb-maint/id3lib/trunk/debian/patches/60-fix_make_check.patch
Patch7:         http://anonscm.debian.org/viewvc/collab-maint/deb-maint/id3lib/trunk/debian/patches/60-id3lib-missing-nullpointer-check.patch
Patch8:         id3lib-3.8.3-fix-utf16-stringlists.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.

%package -n     mingw32-%{_basename}
Summary:        Library for manipulating ID3v1 and ID3v2 tags

%description -n mingw32-%{_basename}
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.
This is the MinGW version, built for the win32 target.

%package -n     mingw32-%{_basename}-tools
Summary:        Tools for manipulating ID3v1 and ID3v2 tags
Requires:       mingw32-%{_basename} = %{version}-%{release}

%description -n mingw32-%{_basename}-tools
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.
These are the MinGW tools, built for the win32 target.

%package -n     mingw64-%{_basename}
Summary:        Library for manipulating ID3v1 and ID3v2 tags

%description -n mingw64-%{_basename}
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.
This is the MinGW version, built for the win64 target.

%package -n     mingw64-%{_basename}-tools
Summary:        Tools for manipulating ID3v1 and ID3v2 tags
Requires:       mingw64-%{_basename} = %{version}-%{release}

%description -n mingw64-%{_basename}-tools
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities. Additionally, it can
tell mp3 header info, like bitrate etc.
These are the MinGW tools, built for the win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_basename}-%{version}
%patch -P0 -p1 -b .io_helpers-163101
%patch -P1 -p1 -b .mkstemp
%patch -P2 -p1 -b .gcc43
%patch -P3 -p1
%patch -P4 -p1 -b .autoreconf
%patch -P5 -p1 -b .mingw
%patch -P6 -p1 -b .make-check
%patch -P7 -p1 -b .nullpointer
%patch -P8 -p1 -b .string-lists
chmod -x src/*.h src/*.cpp include/id3/*.h
iconv -f ISO-8859-1 -t UTF8 ChangeLog > tmp && \
touch -r ChangeLog tmp && \
mv tmp ChangeLog
iconv -f ISO-8859-1 -t UTF8 THANKS > tmp && \
touch -r THANKS tmp && \
mv tmp THANKS

%build
autoreconf --force --install
%{mingw_configure} --disable-dependency-tracking --disable-static
%{mingw_make} V=1 %{?_smp_mflags} libid3_la_LIBADD=-lz

%install
%{mingw_make} DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}/%{mingw32_libdir}/*.la
rm -f %{buildroot}/%{mingw64_libdir}/*.la

%check
%{mingw_make} check

%files -n mingw32-%{_basename}
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README THANKS TODO
%{mingw32_bindir}/libid3-3-8-3.dll
%{mingw32_libdir}/libid3.dll.a
%{mingw32_includedir}/id3.h
%{mingw32_includedir}/id3/

%files -n mingw32-%{_basename}-tools
%{mingw32_bindir}/id3convert.exe
%{mingw32_bindir}/id3cp.exe
%{mingw32_bindir}/id3info.exe
%{mingw32_bindir}/id3tag.exe

%files -n mingw64-%{_basename}
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README THANKS TODO
%{mingw64_bindir}/libid3-3-8-3.dll
%{mingw64_libdir}/libid3.dll.a
%{mingw64_includedir}/id3.h
%{mingw64_includedir}/id3/

%files -n mingw64-%{_basename}-tools
%{mingw64_bindir}/id3convert.exe
%{mingw64_bindir}/id3cp.exe
%{mingw64_bindir}/id3info.exe
%{mingw64_bindir}/id3tag.exe

%changelog
%autochangelog
