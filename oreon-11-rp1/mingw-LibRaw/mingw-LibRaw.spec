%global source0_hash de86b035655accff8d4010f1a221fdf50d353cb7b1422ba26f14a0db92612cfa
%{?mingw_package_header}
%global pkgname LibRaw
Name:          mingw-%{pkgname}
Version:       0.22.2
Release:        1%{?dist}
Summary:        Library for reading RAW files obtained from digital photo cameras
License:       BSD-3-Clause AND (CDDL-1.0 OR LGPL-2.1-only)
BuildArch:     noarch
URL:           http://www.libraw.org
Source0:        http://www.libraw.org/data/%{pkgname}-%{version}.tar.gz
Provides: bundled(dcraw)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-jasper
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-jasper
BuildRequires:  mingw64-lcms2
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-static
%{summary}.

%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-tools
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-static
%{summary}.

%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-tools
%{summary}.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

# Remove executable bit on license files
chmod -x LICENSE.CDDL
chmod -x LICENSE.LGPL

%build

autoreconf -ifv
%mingw_configure --enable-jasper --enable-lcms CPPFLAGS=-DLIBRAW_NODLL
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-LibRaw -f %{oreon_filedir}/mingw32-LibRaw.list
%files -n mingw32-LibRaw-static -f %{oreon_filedir}/mingw32-LibRaw-static.list
%files -n mingw32-LibRaw-tools -f %{oreon_filedir}/mingw32-LibRaw-tools.list
%files -n mingw64-LibRaw -f %{oreon_filedir}/mingw64-LibRaw.list
%files -n mingw64-LibRaw-static -f %{oreon_filedir}/mingw64-LibRaw-static.list
%files -n mingw64-LibRaw-tools -f %{oreon_filedir}/mingw64-LibRaw-tools.list

%changelog

%autochangelog
