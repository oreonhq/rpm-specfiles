%global source0_hash 4b44d4f2b38a370a2d98a78329fefc56a0cf93d1c1be70029217baae6628feea

%{?mingw_package_header}

Name:           mingw-speex
Version:        1.2.1
Release:        2%{?dist}
Summary:        Voice compression format (codec)

License:        BSD-3-clause AND TU-Berlin-1.0
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/speex-%{version}.tar.gz
# Fix build
Patch0:         mingw-speex_build.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

%package -n mingw32-speex
Summary:    Voice compression format (codec)

%description -n mingw32-speex
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the MinGW version, built for the win32 target.

%package -n mingw32-speex-tools
Summary:    The tools package for mingw32-speex
Requires:   mingw32-speex = %{version}-%{release}

%description -n mingw32-speex-tools
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This package contains tools files for the MinGW version of speex, built
for the win32 target.

%package -n mingw64-speex
Summary:    Voice compression format (codec)

%description -n mingw64-speex
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the MinGW version, built for the win64 target.

%package -n mingw64-speex-tools
Summary:    The tools package for mingw64-speex
Requires:   mingw64-speex = %{version}-%{release}

%description -n mingw64-speex-tools
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This package contains tools files for the MinGW version of speex, built
for the win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n speex-%{version}

%build
%mingw_configure --disable-static --enable-binaries

# Remove rpath from speexenc and speexdec
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win32/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win32/libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win64/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win64/libtool

# Fix libtool to recognize win64 archives
sed -i 's|file format pe-i386(\.\*architecture: i386)?|file format pe-x86-64|g' build_win64/libtool

%mingw_make_build

%install
%mingw_make_install
rm -f %{buildroot}%{mingw32_libdir}/libspeex*.la
rm -f %{buildroot}%{mingw64_libdir}/libspeex*.la
rm -f %{buildroot}%{mingw32_docdir}/speex/manual.pdf
rm -f %{buildroot}%{mingw64_docdir}/speex/manual.pdf
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

%files -n mingw32-speex
%license COPYING
%doc AUTHORS TODO ChangeLog README
%{mingw32_bindir}/libspeex-1.dll
%{mingw32_includedir}/speex
%{mingw32_datadir}/aclocal/speex.m4
%{mingw32_libdir}/pkgconfig/speex*.pc
%{mingw32_libdir}/libspeex.dll.a

%files -n mingw32-speex-tools
%{mingw32_bindir}/speexenc.exe
%{mingw32_bindir}/speexdec.exe

%files -n mingw64-speex
%license COPYING
%doc AUTHORS TODO ChangeLog README
%{mingw64_bindir}/libspeex-1.dll
%{mingw64_includedir}/speex
%{mingw64_datadir}/aclocal/speex.m4
%{mingw64_libdir}/pkgconfig/speex*.pc
%{mingw64_libdir}/libspeex.dll.a

%files -n mingw64-speex-tools
%{mingw64_bindir}/speexenc.exe
%{mingw64_bindir}/speexdec.exe

%changelog
%autochangelog
