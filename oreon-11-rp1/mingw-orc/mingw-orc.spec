%global source0_hash 4aeb97aea2b58224029dc2b23d7d064cfa990cb4fb8c4da440bcbe9c95bc5d2d
%{?mingw_package_header}
Name:           mingw-orc
Version:        0.4.44
Release:        1%{?dist}
Summary:        Cross compiled Oil Run-time Compiler
License:        LicenseRef-Callaway-BSD
URL:            http://code.entropywave.com/projects/orc/
Source0:        http://gstreamer.freedesktop.org/src/orc/orc-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

# Mingw32
%package -n mingw32-orc
Summary:        Cross compiled Oil Run-time Compiler
%description -n mingw32-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw32-orc-compiler
Summary:        Orc compiler
Requires:       mingw32-orc = %{version}-%{release}
Requires:       pkgconfig
%description -n mingw32-orc-compiler
The Orc compiler, to produce optimized code.

# Mingw64
%package -n mingw64-orc
Summary:        Orc compiler
%description -n mingw64-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw64-orc-compiler
Summary:        Orc compiler
Requires:       mingw64-orc = %{version}-%{release}
Requires:       pkgconfig
%description -n mingw64-orc-compiler
The Orc compiler, to produce optimized code.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n orc-%{version}

%build

%mingw_meson -Dgtk_doc=disabled
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-orc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-orc-compiler usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-orc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-orc-compiler usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-orc -f %{oreon_filedir}/mingw32-orc.list
%files -n mingw32-orc-compiler -f %{oreon_filedir}/mingw32-orc-compiler.list
%files -n mingw64-orc -f %{oreon_filedir}/mingw64-orc.list
%files -n mingw64-orc-compiler -f %{oreon_filedir}/mingw64-orc-compiler.list

%changelog

%autochangelog
