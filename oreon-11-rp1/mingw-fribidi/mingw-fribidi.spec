%global source0_hash 6949dcde27d41cebad1fd741fcafc36d55a1020d2d872d4a6eb3914caabbada2
%{?mingw_package_header}
%global pkgname fribidi
Name:          mingw-%{pkgname}
Version:       1.0.17
Release:        1%{?dist}
Summary:        MinGW Windows fribidi library
License:       LGPL-2.0-or-later
BuildArch:     noarch
URL:           https://github.com/%{pkgname}/%{pkgname}
Source0:        https://github.com/%{pkgname}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.xz
Patch0:        fribidi-drop-bundled-gnulib.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_meson --default-library=both -Ddocs=false
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-fribidi -f %{oreon_filedir}/mingw32-fribidi.list
%files -n mingw32-fribidi-static -f %{oreon_filedir}/mingw32-fribidi-static.list
%files -n mingw64-fribidi -f %{oreon_filedir}/mingw64-fribidi.list
%files -n mingw64-fribidi-static -f %{oreon_filedir}/mingw64-fribidi-static.list

%changelog

%autochangelog
