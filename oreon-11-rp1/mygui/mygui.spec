%global source0_hash 33c91b531993047e77cace36d6fea73634b8c17bd0ed193d4cd12ac7c6328abd
Name:           mygui
Version:        3.4.3
Release:        1%{?dist}
Summary:        Fast, simple and flexible GUI library for games and 3D applications.
License:        MIT
URL:            http://mygui.info/
Source0:        https://github.com/MyGUI/mygui/archive/MyGUI%{version}/mygui-MyGUI%{version}.tar.gz
Source1:        resources.xml
Source2:        MyGUI-Tools
Source3:        mygui-layouteditor.desktop
Source4:        mygui-imageeditor.desktop
Source5:        mygui-fonteditor.desktop
Source6:        mygui-skineditor.desktop
Patch0:         mygui-add-missing-soname.patch
Requires:       dejavu-sans-fonts
# oreon:deps
BuildRequires:  SDL2_image-devel
BuildRequires:  cmake
BuildRequires:  cmake(SDL2)
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  graphviz
BuildRequires:  libX11-devel
BuildRequires:  libuuid-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  ninja-build
BuildRequires:  ois-devel
# /oreon:deps
%description
MyGUI is a cross-platform library for creating graphical user interfaces (GUIs) for games and 3D applications.

%package        devel
Summary:        Development files for MyGUI
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mesa-libGL-devel
Requires:       ois-devel
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Development documentation for MyGUI
BuildArch:      noarch
%description    devel-doc
The %{name}-devel-doc package contains reference documentation for
developing applications that use %{name}.

%package tools
Summary:        MyGUI tools 
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
This package contains the MyGUI tools, installed in %{_bindir}. 
LayoutEditor is an application for designing UIs using MyGUI library,
FontEditor, ImageEditor and SkinEditor are also provided. They are
renamed to be prefixed with mygui (ie mygui-LayoutEditor)

%prep

%setup -qn %{name}-MyGUI%{version}
%patch -P0 -p1 -b .orig

%build

%cmake -G Ninja \
   -DMYGUI_BUILD_DEMOS=FALSE \
   -DMYGUI_BUILD_DOCS=TRUE \
   -DMYGUI_BUILD_PLUGINS=OFF \
   -DMYGUI_BUILD_TOOLS=TRUE \
   -DMYGUI_DONT_USE_OBSOLETE=ON \
   -DMYGUI_INSTALL_DEMOS=FALSE \
   -DMYGUI_INSTALL_DOCS=TRUE \
   -DMYGUI_INSTALL_PDB=FALSE \
   -DMYGUI_INSTALL_TOOLS=TRUE \
   -DMYGUI_RENDERSYSTEM=4 \
   -DMYGUI_USE_SYSTEM_GLEW=TRUE
%cmake_build
cd %{_vpath_builddir}
pushd Docs
doxygen
popd
%install
%cmake_install
install -d %{buildroot}%{_datadir}/doc/mygui-devel-doc/html
install -d %{buildroot}%{_datadir}/MYGUI/Tools
install -D %{_vpath_builddir}/Docs/html/* %{buildroot}%{_datadir}/doc/mygui-devel-doc/html
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE6}
rm -f %{buildroot}%{_bindir}/resources.xml
install %{SOURCE1} %{buildroot}%{_datadir}/MYGUI/Tools/resources.xml
mv %{buildroot}%{_bindir}/ImageEditor %{buildroot}%{_datadir}/MYGUI/Tools/ImageEditor
mv %{buildroot}%{_bindir}/FontEditor %{buildroot}%{_datadir}/MYGUI/Tools/FontEditor
mv %{buildroot}%{_bindir}/LayoutEditor %{buildroot}%{_datadir}/MYGUI/Tools/LayoutEditor
mv %{buildroot}%{_bindir}/SkinEditor %{buildroot}%{_datadir}/MYGUI/Tools/SkinEditor
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/MyGUI-Tools
rm -rf %{buildroot}%{_datadir}/MYGUI/Media/UnitTests
rm -f %{buildroot}%{_datadir}/MYGUI/Media/CMakeLists.txt
ln -fs %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans.ttf \
  %{buildroot}%{_datadir}/MYGUI/Media/MyGUI_Media/DejaVuSans.ttf
ln -fs %{_datadir}/fonts/dejavu-sans-fonts/DejaVuSans-ExtraLight.ttf \
  %{buildroot}%{_datadir}/MYGUI/Media/MyGUI_Media/DejaVuSans-ExtraLight.ttf
for size in 16 24 32 48 96 256 ; do
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_FE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_fe.png
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_IE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_ie.png
  install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_SE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_se.png
done
for size in 16 24 48 96 256 ; do
    install -Dpm644 Media/Common/Sources/Icons/MyGUI_Icon_LE_${size}x${size}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/mygui_le.png
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n mygui-devel -f %{oreon_filedir}/mygui-devel.list
%files -n mygui-devel-doc -f %{oreon_filedir}/mygui-devel-doc.list
%files -n mygui-tools -f %{oreon_filedir}/mygui-tools.list

%changelog

%autochangelog
