%global source0_hash 6771dc468a65e2b5d236591def6dd2ca5c29c040148e2a315395848af2d3cb6a

%global forgeurl  https://gitlab.freedesktop.org/monado/demos/openxr-simple-playground
%global commit    c5c6096a027d81a20beee1380be78db24e181ecd
%global date      20250903
%forgemeta

Name:           openxr-simple-playground
Version:        0
Release:        %autorelease
Summary:        OpenXR C Playground

License:        BSL-1.0 AND MIT AND Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)

# external/openxr_headers/*.h Apache-2.0
Provides:       bundled(openxr)
# external/math_3d/math_3d.h MIT
Provides:       bundled(math3d)

%description
This example exercises many areas of the OpenXR API. Some 
parts of the API are abstracted, though the abstractions 
are intentionally kept simple for simple editing.

Note: Currently this application only supports the 
XrGraphicsBindingOpenGLXlibKHR (glx) graphics binding.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
mv external/math_3d/LICENSE LICENSE.MIT
mv external/openxr_headers/LICENSE LICENSE.Apache-2.0

%build
# W: no-manual-page-for-binary openxr-playground
%cmake 
%cmake_build

%install
%cmake_install

%files
%doc Readme.md
%license LICENSE LICENSE.MIT LICENSE.Apache-2.0
%{_bindir}/openxr-playground

%changelog
%autochangelog
