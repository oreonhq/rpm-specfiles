%global source2_hash 246897a365febf2748628c25e3d8bfc4c69d93cadfd85ef17ee9096241799769
%global source1_hash 853730be80666e2820268a379232b897cfff4a9d1b031bbff401da94e2a72389
%global source0_hash 39b6ffab20848c91a97de32c9c5a2f35d58bffaff0fc61e4a09365170d953736
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit 8ac191ceb64476b50cd8e16dce7c971fb791af95
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20241204
%global core_commit 277792824801495e868580ca86f6e7a1b53e4779
%global core_shortcommit %(c=%{core_commit}; echo ${c:0:7})
%global kddw_commit 8d2d0a5764f8393cc148a2296d511276a8ffe559
%global kddw_shortcommit %(c=%{kddw_commit}; echo ${c:0:7})
%endif
%global unique_name org.olivevideoeditor.Olive
%global appl_name application-vnd.olive-project
Name:           olive
%if 0%{?usesnapshot}
Version:        0.2.0^%{gitdate}git%{shortcommit}
%else
Version:        0.2.0
%endif
Release:        1%{?dist}
Summary:        A free non-linear video editor
License:        GPL-3.0-or-later AND BSD-3-Clause AND ( GPL-2.0-only OR GPL-3.0-only )
Url:            https://www.olivevideoeditor.org
%if 0%{?usesnapshot}
Source0:        https://github.com/%{name}-editor/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/olive-editor/core/archive/%{core_commit}/libolivecore-%{core_shortcommit}.tar.gz
Source2:        https://github.com/olive-editor/KDDockWidgets/archive/%{kddw_commit}/KDDockWidgets-%{kddw_shortcommit}.tar.gz
Patch0:         %{name}-qt6.patch
Patch1:         %{name}-ocio-2.3.patch
Patch2:         %{name}-ffmpeg-7.patch
Patch3:         %{name}-oiio-3.0.patch
Patch4:         %{name}-ffmpeg-8.patch
Patch5:         0001-fix-qt6-arg-format.patch
Patch6:         0002-fix-qt6-arg-sampleformat.patch
%else
%endif
Patch10:        olive-fix-build-against-qt-6-10.patch
%ifarch aarch64
%endif
Requires:       hicolor-icon-theme
Provides:       bundled(KDDockWidgets) = 1.6.95
Provides:       bundled(libolivecore) = 1.0.0
ExcludeArch:    i686
# oreon:deps
BuildRequires:  OpenColorIO-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  portaudio-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttranslations
# /oreon:deps
%description
%{name} is a free non-linear video editor with completely configurable render
pipeline and open source codebase designed to provide users with as much
control as possible over both their work and their workflow.

Olive's key feature is its render pipeline. Every step can be modified,
rearranged, or augmented to achieve whatever results the user desires. Control
is provided through a node-based compositor, which is the gold standard for
compositing workflows in the visual effects industry. By adding and connecting
nodes together, users "visually program" how their video and audio is generated
and processed. Compared to traditional "layer-based" workflows, this provides
much more freedom in what can be created, and requires far fewer steps to
achieve the same results.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
%autosetup -N -n %{name}-%{commit}
pushd ext
rmdir core
tar xzf %{S:1}
mv core{-%{core_commit},}
rmdir KDDockWidgets
tar xzf %{S:2}
mv KDDockWidgets{-%{kddw_commit},}
popd
%autopatch -p1
%else
%autosetup -p1 -n %{name}-%{version}
%endif
%ifarch aarch64
# use system sse2neon
rm -v ext/core/include/olive/core/util/sse2neon.h
%endif

%build

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_QT6=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_TESTS=ON \
  -DKDDockWidgets_EXAMPLES=OFF \
  -DOLIVECORE_BUILD_TESTS=ON \
  -DUSE_WERROR=OFF \
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{unique_name}.appdata.xml
%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
