%global source0_hash 6ee01b81c43816170b18709c6045b6245cecc2953f01cecc9e98f82b49ea4f73
Name:           svt-vp9
Version:        0.3.0
Release:        1%{?dist}
Summary:        Scalable Video Technology for VP9 Encoder
License:        BSD-2-Clause-Patent and ISC
URL:            https://github.com/OpenVisualCloud/SVT-VP9
Source0:        https://github.com/OpenVisualCloud/SVT-VP9/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         cmake.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  meson
BuildRequires:  nasm
# /oreon:deps
%description
The Scalable Video Technology for VP9 Encoder (SVT-VP9 Encoder)
is a VP9-compliant encoder library core. The SVT-VP9 Encoder development
is a work-in-progress targeting performance levels applicable to both VOD
and Live encoding/transcoding video applications.

%package        libs
Summary:        Libraries for svt-hevc
%description    libs
Libraries for development svt-hevc.

%package        devel
Summary:        Include files and mandatory libraries for development svt-vp9
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Include files and mandatory libraries for development svt-vp9.

%package -n     gstreamer1-%{name}
Summary:        GStreamer 1.0 %{name}-based plug-in
Requires:       gstreamer1-plugins-base%{?_isa}
%description -n gstreamer1-%{name}
This package provides %{name}-based GStreamer plug-in.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n SVT-VP9-%{version}
#-n OpenVisualCloud-SVT-VP9-%{gitcommit}
# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtVp9Enc',|" \
-e "/svtvp9enc_dep =/d" -e 's|, svtvp9enc_dep||' -e "s|svtvp9enc_dep.found()|true|" -i gstreamer-plugin/meson.build

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -G Ninja \
    -DCMAKE_SKIP_BUILD_RPATH=TRUE
%cmake_build
pushd gstreamer-plugin
    export LIBRARY_PATH="$PWD/../Bin/Release:$LIBRARY_PATH"
    %meson
    %meson_build
popd
%install
%cmake_install
pushd gstreamer-plugin
    %meson_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n svt-vp9-libs -f %{oreon_filedir}/svt-vp9-libs.list
%files -n svt-vp9-devel -f %{oreon_filedir}/svt-vp9-devel.list
%files -n gstreamer1-svt-vp9 -f %{oreon_filedir}/gstreamer1-svt-vp9.list

%changelog

%autochangelog
