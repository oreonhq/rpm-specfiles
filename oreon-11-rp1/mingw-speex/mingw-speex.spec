%global source0_hash 4b44d4f2b38a370a2d98a78329fefc56a0cf93d1c1be70029217baae6628feea
%{?mingw_package_header}
Name:           mingw-speex
Version:        1.2.1
Release:        1%{?dist}
Summary:        Voice compression format (codec)
License:        BSD-3-clause AND TU-Berlin-1.0
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/speex-%{version}.tar.gz
Patch0:         mingw-speex_build.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libogg
# /oreon:deps
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
%global oreon_srcdir speex-%{version}
%oreon_prep
%build

%mingw_configure --disable-static --enable-binaries
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win32/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win32/libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' build_win64/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' build_win64/libtool
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
%oreon_autofiles mingw32-speex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-speex-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-speex usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-speex-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-speex -f %{oreon_filedir}/mingw32-speex.list
%files -n mingw32-speex-tools -f %{oreon_filedir}/mingw32-speex-tools.list
%files -n mingw64-speex -f %{oreon_filedir}/mingw64-speex.list
%files -n mingw64-speex-tools -f %{oreon_filedir}/mingw64-speex-tools.list

%changelog

%autochangelog
