%global source0_hash 7e2fa4e8c7c98e8d8140671f5772542afaaa6acccfbd746506886b6d85f7f8d6
%{?mingw_package_header}
Name:           mingw-harfbuzz
Version:        14.5.1
Release:        1%{?dist}
Summary:        MinGW Windows Harfbuzz library
License:        MIT
URL:            http://www.harfbuzz.org
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz
Patch0:        harfbuzz-python.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-icu
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-icu
BuildRequires:  python3
# /oreon:deps
%description
HarfBuzz is an implementation of the OpenType Layout engine.

# Win32
%package -n mingw32-harfbuzz
Summary:        MinGW Windows Harfbuzz library
%description -n mingw32-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw32-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw32-harfbuzz = %{version}-%{release}
Requires:       mingw32-glib2-static
%description -n mingw32-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.

# Win64
%package -n mingw64-harfbuzz
Summary:        MinGW Windows Harfbuzz library
%description -n mingw64-harfbuzz
HarfBuzz is an implementation of the OpenType Layout engine.

%package -n mingw64-harfbuzz-static
Summary:        Static version of the MinGW Windows Harfbuzz library
Requires:       mingw64-harfbuzz = %{version}-%{release}
Requires:       mingw64-glib2-static
%description -n mingw64-harfbuzz-static
Static version of the MinGW Windows Harfbuzz library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir harfbuzz-%{version}
%oreon_prep
%build

export MINGW_BUILDDIR_SUFFIX=static
%mingw_meson --default-library=static
%mingw_ninja
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_meson --default-library=shared
%mingw_ninja
%install
export MINGW_BUILDDIR_SUFFIX=static
%mingw_ninja_install
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_ninja_install
%oreon_autofiles mingw32-harfbuzz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-harfbuzz-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-harfbuzz usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-harfbuzz-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-harfbuzz -f %{oreon_filedir}/mingw32-harfbuzz.list
%files -n mingw32-harfbuzz-static -f %{oreon_filedir}/mingw32-harfbuzz-static.list
%files -n mingw64-harfbuzz -f %{oreon_filedir}/mingw64-harfbuzz.list
%files -n mingw64-harfbuzz-static -f %{oreon_filedir}/mingw64-harfbuzz-static.list

%changelog

%autochangelog
