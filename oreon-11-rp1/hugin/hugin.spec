%global source0_hash 7cf8eb33a6a8848cc7f816faf4bc88389228883d5513136dccb5cb243912ab79
Summary:        A panoramic photo stitcher and more
Name: hugin
Version: 2025.0.1
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
URL: http://hugin.sourceforge.net/
Requires: shared-mime-info
Requires: webclient
Requires: %{name}-base = %{version}-%{release}
# oreon:deps
BuildRequires:  OpenEXR-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel
BuildRequires:  fftw-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  lcms2-devel
BuildRequires:  libXmu-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpano13-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  perl-Image-ExifTool
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sqlite-devel
BuildRequires:  swig
BuildRequires:  vigra-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
hugin can be used to stitch multiple images together. The resulting image can
span 360 degrees. Another common use is the creation of very high resolution
pictures by combining multiple images. It uses the Panorama Tools as back-end
to create high quality images

%package base
Summary: Command-line tools and libraries required by hugin
Requires: enblend perl-Image-ExifTool
%description base
Command-line tools used to generate panoramic images, install this package
separately from hugin if you want to batch-process hugin projects on a machine
without a GUI environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's^/usr/bin/env python3^/usr/bin/python3^' \
src/hugin_script_interface/plugins-dev/*.py \
src/hugin_script_interface/*.py \
src/hugin_script_interface/plugins/*.py

%build

%cmake \
  -DBUILD_HSI=1 \
  -DUSE_GDKBACKEND_X11=ON \
  -DBUILD_WITH_EPOXY=ON
%cmake_build
%install
%cmake_install
%if 0%{?flatpak}
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_usr}/%{_lib}/python%{python3_version}/site-packages/* %{buildroot}%{python3_sitearch}
%endif
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/PTBatcherGUI.desktop
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/pto_gen.desktop
desktop-file-install --vendor="" --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/hugin_toolbox_gui.desktop
%find_lang %{name}
mkdir -p %{buildroot}/%{_datadir}/metainfo
cat > %{buildroot}/%{_datadir}/metainfo/calibrate_lens_gui.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>calibrate_lens_gui.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">hugin.desktop</value>
  </metadata>
</component>
EOF
%ldconfig_scriptlets base
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hugin-base -f %{oreon_filedir}/hugin-base.list

%changelog

%autochangelog
