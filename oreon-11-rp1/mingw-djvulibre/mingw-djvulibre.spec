%global source0_hash d3b4b03ae2bdca8516a36ef6eb27b777f0528c9eda26745d9962824a3fdfeccf

%{?mingw_package_header}

%global pkgname djvulibre

Name:          mingw-%{pkgname}
Version:       3.5.29
Release:       3%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
License:       GPL-2.0-or-later
URL:           http://djvu.sourceforge.net/
Source0:       http://downloads.sourceforge.net/djvu/%{pkgname}-%{version}.tar.gz

BuildRequires: automake autoconf libtool make

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo

%description
%{summary}.

%package -n mingw32-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.

%package -n mingw64-%{pkgname}
Summary:        MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the  MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%mingw_configure
# Parallel build is broken
%mingw_make

%install
%{mingw_make} install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove shell scripts
rm -f %{buildroot}%{mingw32_bindir}/{any2djvu,djvudigital}
rm -f %{buildroot}%{mingw64_bindir}/{any2djvu,djvudigital}

# Remove data
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libdjvulibre-21.dll
%{mingw32_includedir}/libdjvu/
%{mingw32_libdir}/libdjvulibre.dll.a
%{mingw32_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libdjvulibre-21.dll
%{mingw64_includedir}/libdjvu/
%{mingw64_libdir}/libdjvulibre.dll.a
%{mingw64_libdir}/pkgconfig/ddjvuapi.pc

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
