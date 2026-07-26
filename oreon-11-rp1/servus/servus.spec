%global source0_hash b617ae7cccb076ac029bd4ff54cb11bcc55a756f13e12052081ce4d90f2e6d61

%global cmake_module_ver 2018.02

%global api_major 6
%global api_minor 0
%global api_patch 0
%global api_version %{api_major}.%{api_minor}.%{api_patch}

Name:          servus
Version:       1.5.2
#%%global version_major %%(ver=%%{version}; echo ${ver%%.*})
#%%global version_minor %%(ver=%%{version}; ver=`echo ${ver#*.}`; echo ${ver%.*})
#%%global version_patch %%(ver=%%{version}; echo ${ver##*.})

# version hardcoded in the macros differs from the package version, upstream bug
%global version_major 1
%global version_minor 6
%global version_patch 0
Release:       16%{?dist}
Summary:       Zeroconf discovery in C++

# RSA license for the MD5 code which is based on the RSA licensed code
# see ACKNOWLEDGEMENTS.txt for details
# Automatically converted from old format: LGPLv3 and RSA - review is highly recommended.
License:       LGPL-3.0-only AND LicenseRef-RSA
URL:           https://github.com/HBPVIS/Servus
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/HBPVIS/Servus/issues/102
Source1:       https://github.com/Eyescale/CMake/archive/refs/tags/%{cmake_module_ver}.tar.gz
# https://github.com/HBPVIS/Servus/issues/106
Source2:       https://www.gnu.org/licenses/gpl-3.0.txt
Source3:       https://www.gnu.org/licenses/lgpl-3.0.txt
# https://github.com/HBPVIS/Servus/issues/107
Source4:       %{name}.desktop
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: avahi-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: sed
Provides:      bundled(eyescale-cmake-common) = %{cmake_module_ver}
# https://github.com/HBPVIS/Servus/pull/100
Patch:        servus-1.5.2-stdexcept-fix.patch
# https://github.com/HBPVIS/Servus/pull/96
Patch:        servus-1.5.2-copy-const-fix.patch
# https://github.com/Eyescale/CMake/pull/599
Patch:        servus-1.5.2-libdir-fix.patch
# https://github.com/HBPVIS/Servus/issues/116
# https://github.com/Eyescale/CMake/pull/606
Patch:        servus-1.5.2-cmake-4-fix.patch

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

# fix the strange versioning, asked upstream, what's the right version
# in the meantime I am going with the SONAME as the version
pushd %{buildroot}%{_libdir}
for f in libServus.so libServusQt.so;
do
# very simple API check
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

%check
%ctest

%files
%doc AUTHORS.txt LICENSE.txt README.md doc/Changelog.md
# https://github.com/HBPVIS/Servus/issues/103
%license COPYING COPYING.LESSER ACKNOWLEDGEMENTS.txt
%{_bindir}/servusBrowser
%{_libdir}/libServus{,Qt}.so.6*
%{_datadir}/applications/servus.desktop

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_datadir}/Servus

%changelog
%autochangelog
