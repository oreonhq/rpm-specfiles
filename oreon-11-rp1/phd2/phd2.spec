%global source0_hash none
%global gittag v2.6.14
Name:           phd2
%if "%{?gittag}"
Version:        2.6.14
%else
Version:        2.6.11^dev4^%{date}%{shortcommit}
%endif
Release:        1%{?dist}
Summary:        Telescope guiding software
License:        BSD-3-Clause AND LGPL-2.1-or-later AND ICU
URL:            http://openphdguiding.org/
%if "%{?gittag}"
Source0:        %{name}-%{version}-purged.tar.xz
%else
%endif
Source1:        generate-tarball.sh
Patch99:        phd2_2.9.10_std_cflags.patch
Patch101:       phd2-eigen3.patch
ExcludeArch:    %{ix86}
Recommends:     libindi
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libindi-static
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libindi)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
PHD2 is telescope guiding software that simplifies the process of tracking
a guide star, letting you concentrate on other aspects of deep-sky imaging
or spectroscopy.

%prep

%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

# Remove spurious executable bit set on icons and docs
find icons -type f -print0 |xargs -0 chmod -x
chmod -x doc/PHD_2.0_Architecture.docx

%build

%{cmake} -DUSE_SYSTEM_CFITSIO=ON \
            -DUSE_SYSTEM_LIBUSB=ON \
            -DUSE_SYSTEM_EIGEN3=ON \
            -DUSE_SYSTEM_GTEST=ON \
            -DUSE_SYSTEM_LIBINDI=ON \
            -DOPENSOURCE_ONLY=ON
%cmake_build -j1
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

%ctest
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
