%global source0_hash 5911c63c465d23e8c27262b5702c2e708844b33fefb0f924855fa1a17158a089
%global         major_minor_version 5.13
%global         patch_version 0
Name:           cura
Epoch:          1
Version:        %{major_minor_version}.%{patch_version}
Release:        1%{?dist}
Summary:        3D printer / slicing GUI
License:        LGPL-3.0-or-later
URL:            https://ultimaker.com/en/products/cura-software
Source0:        https://github.com/Ultimaker/Cura/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        mod_bundled_packages_json.py
Source3:        CuraPluginInstall.cmake
Source4:        CuraTests.cmake
Source5:        com.ultimaker.cura.desktop.in
Source6:        CMakeLists.txt
Source7:        CuraVersion.py.in
Source8:        com.ultimaker.cura.appdata.xml
Patch:          028e7f7.patch
Patch:          https://github.com/Ultimaker/Cura/pull/16103.patch
Patch:          https://github.com/Ultimaker/Cura/pull/17642.patch
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       open-sans-fonts
Requires:       python3-certifi
Requires:       python3-keyring
Requires:       python3-numpy-stl
Requires:       python3-pyserial
Requires:       python3-pynest2d
Requires:       python3-requests
Requires:       python3-savitar >= 5.3.0
Requires:       python3-trimesh
Requires:       python3-uranium >= 5.4.0
Requires:       python3-zeroconf
Requires:       CuraEngine == %{epoch}:%{version}
Requires:       cura-fdm-materials >= %{major_minor_version}
Requires:       libglvnd-devel
Requires:       3dprinter-udev-rules
Recommends:     python3-trimesh
Recommends:     python3-certifi
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-keyring
BuildRequires:  python3-pip
BuildRequires:  python3-pynest2d
BuildRequires:  python3-pyserial
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-savitar
BuildRequires:  python3-uranium
BuildRequires:  python3-zeroconf
# /oreon:deps
%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

# see: https://github.com/Ultimaker/Cura/issues/5142
%define cura_cloud_api_root https://api.ultimaker.com
%define cura_cloud_api_version 1
%define cura_cloud_account_api_root https://account.ultimaker.com

%define reverse_dns_name com.ultimaker.%{name}

%prep

%autosetup -p1 -S git -n Cura-%{version}

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} cmake
rm -rf CMakeLists.txt
cp -a %{SOURCE5} %{SOURCE6} %{SOURCE8} .
cp -a %{SOURCE7} cura

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
sed -i '1s=^#!/usr/bin/\(python\|env python\)3*=#!%{python3}=' cura_app.py

%build

%cmake \
  -DCURA_VERSION:STRING=%{version} \
  -DCURA_BUILDTYPE="RPM %{version}"\
  -DCURA_CLOUD_API_ROOT:STRING=%{cura_cloud_api_root} \
  -DCURA_CLOUD_API_VERSION:STRING=%{cura_cloud_api_version} \
  -DCURA_CLOUD_ACCOUNT_API_ROOT:STRING=%{cura_cloud_account_api_root} \
  -DLIB_SUFFIX:STR=
%cmake_build
cd resources/i18n
rm *.pot
for DIR in *; do
  pushd $DIR
  for FILE in *.po; do
    msgfmt $FILE.po -o LC_MESSAGES/${FILE%po}mo || :
  done
  popd
done
cd -
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/resources/images/whats_new
mkdir -p %{buildroot}%{_datadir}/%{name}/resources/texts/whats_new
mkdir -p %{buildroot}%{_datadir}/%{name}/resources/scripts
pushd %{buildroot}%{_datadir}
mv cura/resources/i18n locale
ln -s ../../locale cura/resources/i18n
rm locale/*/*.po
popd
rm -rf %{buildroot}%{_datadir}/%{name}/resources/themes/cura-light/fonts/
ln -s %{_datadir}/fonts/open-sans/ %{buildroot}%{_datadir}/%{name}/resources/themes/cura-light/fonts
rm -r %{buildroot}%{_prefix}/lib/cura/plugins/{SentryLogger,UFPReader,UFPWriter}
%py_byte_compile %{python3} %{buildroot}%{_prefix}/lib/cura
%py3_shebang_fix %{buildroot}%{_bindir}/*
%find_lang cura
%find_lang fdmextruder.def.json
%find_lang fdmprinter.def.json
%oreon_autofiles main

%check

%{python3} -m pip freeze
%{python3} -m pytest -v
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reverse_dns_name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
