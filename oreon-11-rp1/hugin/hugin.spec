%global source0_hash 7cf8eb33a6a8848cc7f816faf4bc88389228883d5513136dccb5cb243912ab79

Summary: A panoramic photo stitcher and more
Name: hugin
Version: 2025.0.1
Release: 2%{?dist}
License: GPL-2.0-or-later
Source: https://downloads.sourceforge.net/hugin/%{name}-%{version}.tar.bz2
URL: http://hugin.sourceforge.net/
Requires: shared-mime-info
Requires: webclient
Requires: %{name}-base = %{version}-%{release}
BuildRequires: gcc-c++
BuildRequires: libpano13-devel zlib-devel libtiff-devel libjpeg-devel
BuildRequires: libpng-devel gettext-devel wxGTK-devel boost-devel freeglut-devel
BuildRequires: cmake desktop-file-utils OpenEXR-devel exiv2-devel libepoxy-devel
BuildRequires: python3-devel swig perl-Image-ExifTool
BuildRequires: mesa-libGLU-devel libXmu-devel sqlite-devel vigra-devel
BuildRequires: perl-podlators fftw-devel lcms2-devel
# contains deprecated distutils
BuildRequires: python3-setuptools

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
# pyinstalldir is not configurable
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

# Merge applications into one software center item
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

%files -f %{name}.lang
%{_bindir}/PTBatcherGUI
%{_bindir}/hugin
%{_bindir}/hugin_stitch_project
%{_bindir}/icpfind
%{_bindir}/calibrate_lens_gui
%{_bindir}/hugin_executor
%{_bindir}/hugin_toolbox
%{_libdir}/%{name}/libhuginbasewx.so*
%{_libdir}/%{name}/libicpfindlib.so*
%{_datadir}/%{name}/xrc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/PTBatcherGUI.desktop
%{_datadir}/applications/calibrate_lens_gui.desktop
%{_datadir}/applications/pto_gen.desktop
%{_datadir}/applications/hugin_toolbox_gui.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/PTBatcherGUI.appdata.xml
%{_datadir}/metainfo/calibrate_lens_gui.appdata.xml
%{_datadir}/metainfo/hugin.appdata.xml
%{_datadir}/metainfo/hugin_toolbox.appdata.xml
%{_mandir}/man1/PTBatcherGUI.*
%{_mandir}/man1/calibrate_lens_gui.*
%{_mandir}/man1/hugin.*
%{_mandir}/man1/hugin_stitch_project.*
%{_mandir}/man1/icpfind.*
%{_mandir}/man1/hugin_executor.*
%{_mandir}/man1/hugin_stacker.*

%doc AUTHORS README TODO doc/nona.txt doc/fulla.html doc/executor_file_format.txt
%license COPYING.txt src/celeste/LICENCE_LIBSVM src/hugin1/hugin/xrc/data/help_en_EN/LICENCE.manual

%files base
%{_bindir}/align_image_stack
%{_bindir}/autooptimiser
%{_bindir}/celeste_standalone
%{_bindir}/fulla
%{_bindir}/hugin_hdrmerge
%{_bindir}/nona
%{_bindir}/tca_correct
%{_bindir}/vig_optimize
%{_bindir}/cpclean
%{_bindir}/deghosting_mask
%{_bindir}/pano_trafo
%{_bindir}/pano_modify
%{_bindir}/pto_merge
%{_bindir}/checkpto
%{_bindir}/cpfind
%{_bindir}/linefind
%{_bindir}/pto_gen
%{_bindir}/pto_lensstack
%{_bindir}/pto_var
%{_bindir}/geocpset
%{_bindir}/pto_mask
%{_bindir}/pto_move
%{_bindir}/pto_template
%{_bindir}/verdandi
%{_bindir}/hugin_lensdb
%{_bindir}/hugin_stacker

%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/libhuginbase.so*
%{_libdir}/%{name}/libceleste.so*
%{_libdir}/%{name}/liblocalfeatures.so*
%{_libdir}/%{name}/libhugin_python_interface.so*
%{python3_sitearch}/_hsi.so
%{python3_sitearch}/hsi.py*
%{python3_sitearch}/hpi.py*
%{python3_sitearch}/__pycache__/*

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/data

%{_mandir}/man1/align_image_stack.*
%{_mandir}/man1/autooptimiser.*
%{_mandir}/man1/cpclean.*
%{_mandir}/man1/celeste_standalone.*
%{_mandir}/man1/fulla.*
%{_mandir}/man1/hugin_hdrmerge.*
%{_mandir}/man1/nona.*
%{_mandir}/man1/tca_correct.*
%{_mandir}/man1/vig_optimize.*
%{_mandir}/man1/deghosting_mask.*
%{_mandir}/man1/pano_trafo.*
%{_mandir}/man1/pano_modify.*
%{_mandir}/man1/pto_merge.*
%{_mandir}/man1/checkpto.*
%{_mandir}/man1/cpfind.*
%{_mandir}/man1/linefind.*
%{_mandir}/man1/pto_gen.*
%{_mandir}/man1/pto_lensstack.*
%{_mandir}/man1/pto_var.*
%{_mandir}/man1/geocpset.*
%{_mandir}/man1/pto_mask.*
%{_mandir}/man1/pto_move.*
%{_mandir}/man1/pto_template.*
%{_mandir}/man1/verdandi.*
%{_mandir}/man1/hugin_lensdb.*

%changelog
%autochangelog
