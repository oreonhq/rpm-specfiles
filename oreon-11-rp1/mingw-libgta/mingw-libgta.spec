%global source0_hash d445667e145f755f0bc34ac89b63a6bfdce1eea943f87ee7a3f23dc0dcede8b1
%{?mingw_package_header}
%global pkgname libgta
Name:          mingw-%{pkgname}
Version:       1.2.1
Release:        1%{?dist}
Summary:        MinGW Windows GTA library
License:       LicenseRef-Callaway-LGPLv2+
BuildArch:     noarch
URL:           http://gta.nongnu.org
Source0:        https://marlam.de/gta/releases/%{pkgname}-%{version}.tar.xz
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-xz-libs
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-xz-libs
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows GTA library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GTA library
%description -n mingw32-%{pkgname}
MinGW Windows GTA library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GTA library
%description -n mingw64-%{pkgname}
MinGW Windows GTA library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_configure --disable-static
%mingw_make_build V=1
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgta -f %{oreon_filedir}/mingw32-libgta.list
%files -n mingw64-libgta -f %{oreon_filedir}/mingw64-libgta.list

%changelog

%autochangelog
