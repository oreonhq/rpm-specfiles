%global source0_hash 4246939528dac37bbcd368c8169001027437fdd1023cd84fdac81dbc3601f6ef
%bcond_with kde
%global gitdate       20260119
%global commit        3127a2d211b124ad4fcf853d01e6df9323bdfdc3
%global short_commit  %(c="%{commit}"; echo ${c:0:7})
Name:           qimgv
Version:        1.0.3^%{gitdate}git%{short_commit}
Release:        1%{?dist}
Summary:        Image viewer. Fast, easy to use. Optional video support
License:        GPL-3.0-or-later
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/%{name}/archive/%{commit}/%{name}-%{short_commit}.tar.gz
%if %{with kde}
%endif
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(mpv)
# /oreon:deps
%description
Image viewer. Fast, easy to use. Optional video support.

Key features:

  * Simple UI
  * Fast
  * Easy to use
  * Fully configurable, including themes, shortcuts
  * High quality scaling
  * Basic image editing: Crop, Rotate and Resize
  * Ability to quickly copy / move images to different folders
  * Experimental video playback via libmpv
  * Folder view mode
  * Ability to run shell scripts

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -G Ninja \
    -DEXIV2=ON \
    -DVIDEO_SUPPORT=ON \
    -DOPENCV_SUPPORT=ON \
    -DKDE_SUPPORT:BOOL=%{?with_kde:ON}%{!?with_kde:OFF} \
    -DUSE_QT5=OFF
%cmake_build
%install
%cmake_install
%find_lang qimgv --with-qt --all-name
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
