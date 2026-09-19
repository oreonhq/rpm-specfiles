%global source0_hash 6ee01b81c43816170b18709c6045b6245cecc2953f01cecc9e98f82b49ea4f73

# %global gitcommit_full a34e143c22ca99107c4b4efac0ce266f5e93d79a
# %global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
# %global date 20200117

Name:           svt-vp9
Version:        0.3.0
Release:        17%{?dist}
Summary:        Scalable Video Technology for VP9 Encoder

# ISC license for Source/Lib/ASM_SSE2/x86inc.asm
License:        BSD-2-Clause-Patent and ISC
URL:            https://github.com/OpenVisualCloud/SVT-VP9
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0:        %url/tarball/%{gitcommit_full}
# https://github.com/OpenVisualCloud/SVT-VP9/pull/133
Patch0:         cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

ExclusiveArch:  x86_64

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
# TODO: Please submit an issue to upstream (rhbz#2380809)
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

%files
%doc Docs/svt-vp9_encoder_user_guide.md
%{_bindir}/SvtVp9EncApp

%files libs
%license LICENSE.md
%doc README.md
%{_libdir}/libSvtVp9Enc.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/libSvtVp9Enc.so
%{_libdir}/pkgconfig/*.pc

%files -n gstreamer1-%{name}
%{_libdir}/gstreamer-1.0/libgstsvtvp9enc.so

%changelog
%autochangelog
