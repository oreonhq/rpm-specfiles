%global source0_hash c3d23b37dfd6e39f2e09f091b77b1541fbfa17c4f0b6bf5c89baef7229080e17

%{?mingw_package_header}

%global pkgname libsigc++30

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:          mingw-%{pkgname}
Version:       3.6.0
Release:       7%{?dist}
Summary:       MinGW Windows sigc++ 3.0 library

License:       LGPL-2.0-or-later
BuildArch:     noarch
URL:           https://github.com/libsigcplusplus/libsigcplusplus
Source0:       https://download.gnome.org/sources/libsigc++/%{release_version}/libsigc++-%{version}.tar.xz

BuildRequires: meson

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libsigc++-%{version}

%build
%mingw_meson
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libsigc-3.0-0.dll
%{mingw32_includedir}/sigc++-3.0/
%{mingw32_libdir}/sigc++-3.0/
%{mingw32_libdir}/libsigc-3.0.dll.a
%{mingw32_libdir}/pkgconfig/sigc++-3.0.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libsigc-3.0-0.dll
%{mingw64_includedir}/sigc++-3.0/
%{mingw64_libdir}/sigc++-3.0/
%{mingw64_libdir}/libsigc-3.0.dll.a
%{mingw64_libdir}/pkgconfig/sigc++-3.0.pc

%changelog
%autochangelog
