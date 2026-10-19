%global source3_hash e3a994d82e644b03a792a930f574002658412f62407f5fee083f2555c5f23118
%global source2_hash 3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986
%global source1_hash 06ae367f70e34e5e5b27fac2296f7bdf33e36d5c016b1545020239fc49e5dd56
%global source0_hash b617ae7cccb076ac029bd4ff54cb11bcc55a756f13e12052081ce4d90f2e6d61
%global cmake_module_ver 2018.02
%global api_major 6
%global api_minor 0
%global api_patch 0
%global api_version %{api_major}.%{api_minor}.%{api_patch}
Name:          servus
Version:       1.5.2
%global version_major 1
%global version_minor 6
%global version_patch 0
Release:        1%{?dist}
Summary:        Zeroconf discovery in C++
License:       LGPL-3.0-only AND LicenseRef-RSA
URL:           https://github.com/HBPVIS/Servus
Source0:        https://github.com/HBPVIS/Servus/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
Source2:       https://www.gnu.org/licenses/gpl-3.0.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
Source4:       %{name}.desktop
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
Patch:        servus-1.5.2-stdexcept-fix.patch
Patch:        servus-1.5.2-copy-const-fix.patch
Patch:        servus-1.5.2-libdir-fix.patch
Patch:        servus-1.5.2-cmake-4-fix.patch
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  sed
# /oreon:deps
%description
Servus is a small C++ network utility library that provides a zeroconf API,
URI parsing and UUIDs.

%package devel
Summary:       Development files for servus
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for servus.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -n Servus-%{version}
mv CMake-%{cmake_module_ver}/* CMake/common/
rm -f CMake-%{cmake_module_ver}/.gitignore
rmdir CMake-%{cmake_module_ver}
%autopatch -p1
cp -a %{SOURCE2} COPYING
cp -a %{SOURCE3} COPYING.LESSER

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE4}
pushd %{buildroot}%{_libdir}
for f in libServus.so libServusQt.so;
do
  [ -f "$f.%{api_major}" ]
  rm -f $f $f.%{api_major}
  mv $f.%{version_major}.%{version_minor}.%{version_patch} $f.%{api_version}
  ln -s $f.%{api_version} $f.%{api_major}
  ln -s $f.%{api_major} $f
done
pushd %{buildroot}%{_datadir}/Servus/CMake
sed -i 's/%{version_major}\.%{version_minor}\.%{version_patch}/%{api_version}/g' \
 ./ServusConfigVersion.cmake ./ServusTargets-debug.cmake
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n servus-devel -f %{oreon_filedir}/servus-devel.list

%changelog

%autochangelog
