%global source0_hash d445667e145f755f0bc34ac89b63a6bfdce1eea943f87ee7a3f23dc0dcede8b1

%{?mingw_package_header}

%global pkgname libgta

Name:          mingw-%{pkgname}
Version:       1.2.1
Release:       14%{?dist}
Summary:       MinGW Windows GTA library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
BuildArch:     noarch
URL:           http://gta.nongnu.org
Source0:       https://marlam.de/gta/releases/%{pkgname}-%{version}.tar.xz

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-bzip2
BuildRequires: mingw32-zlib
BuildRequires: mingw32-xz-libs

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-bzip2
BuildRequires: mingw64-zlib
BuildRequires: mingw64-xz-libs

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

# Remove documentation
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgta-1.dll
%{mingw32_includedir}/gta/
%{mingw32_libdir}/libgta.dll.a
%{mingw32_libdir}/pkgconfig/gta.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgta-1.dll
%{mingw64_includedir}/gta/
%{mingw64_libdir}/libgta.dll.a
%{mingw64_libdir}/pkgconfig/gta.pc

%changelog
%autochangelog
