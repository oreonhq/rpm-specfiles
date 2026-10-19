%global source0_hash e889ac9c7e8a6bdfc31972bf1f1254b84882cb52931608bada62e8febbf0270b
%{?mingw_package_header}
%global origname sdl12-compat
Name:           mingw-%{origname}
Version:        1.2.76
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL 1.2 runtime compatibility library using SDL 2.0
License:        Zlib AND MIT AND (MIT-0 OR LicenseRef-Fedora-Public-Domain)
URL:            https://github.com/libsdl-org/%{origname}
Source0:        https://github.com/libsdl-org/%{origname}/archive/release-%{version}/%{origname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw32-%{origname}
Summary:        MinGW 32-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
Obsoletes:      mingw32-SDL < 1.2.15-19
Conflicts:      mingw32-SDL < 1.2.50
Provides:       mingw32-SDL = %{version}
Requires:       mingw32-SDL2 >= 2.0.18
%description -n mingw32-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 32-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw64-%{origname}
Summary:        MinGW 64-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
Obsoletes:      mingw64-SDL < 1.2.15-19
Conflicts:      mingw64-SDL < 1.2.50
Provides:       mingw64-SDL = %{version}
Requires:       mingw64-SDL2 >= 2.0.18
%description -n mingw64-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 64-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{origname}-release-%{version} -S git_am

%build

%mingw_cmake
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-sdl12-compat -f %{oreon_filedir}/mingw32-sdl12-compat.list
%files -n mingw64-sdl12-compat -f %{oreon_filedir}/mingw64-sdl12-compat.list

%changelog

%autochangelog
