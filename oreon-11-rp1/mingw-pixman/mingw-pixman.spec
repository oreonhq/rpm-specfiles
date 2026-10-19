%global source0_hash d09c44ebc3bd5bee7021c79f922fe8fb2fb57f7320f55e97ff9914d2346a591c
%{?mingw_package_header}
Name:           mingw-pixman
Version:        0.46.4
Release:        1%{?dist}
Summary:        MinGW Windows Pixman library
License:        MIT
URL:            http://cgit.freedesktop.org/pixman/
Source0:        http://cairographics.org/releases/pixman-%{version}.tar.gz
Source1:        make-pixman-snapshot.sh
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libgomp
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libgomp
# /oreon:deps
%description
MinGW Windows Pixman library.

# Win32
%package -n mingw32-pixman
Summary:        MinGW Windows Pixman library
%description -n mingw32-pixman
MinGW Windows Pixman library.

%package -n mingw32-pixman-static
Summary:        Static version of the MinGW Windows Pixman library
Requires:       mingw32-pixman = %{version}-%{release}
%description -n mingw32-pixman-static
Static version of the MinGW Windows Pixman library.

# Win64
%package -n mingw64-pixman
Summary:        MinGW Windows Pixman library
%description -n mingw64-pixman
MinGW Windows Pixman library.

%package -n mingw64-pixman-static
Summary:        Static version of the cross compiled Pixman library
Requires:       mingw64-pixman = %{version}-%{release}
%description -n mingw64-pixman-static
Static version of the cross compiled Pixman library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pixman-%{version}
%oreon_prep
%build

%mingw_meson --default-library=both -Dgtk=disabled
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-pixman usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-pixman-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pixman usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pixman-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-pixman -f %{oreon_filedir}/mingw32-pixman.list
%files -n mingw32-pixman-static -f %{oreon_filedir}/mingw32-pixman-static.list
%files -n mingw64-pixman -f %{oreon_filedir}/mingw64-pixman.list
%files -n mingw64-pixman-static -f %{oreon_filedir}/mingw64-pixman-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.46.4-2
- Prepare for Oreon 11 (RP1)
