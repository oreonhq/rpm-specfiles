%global source1_hash 3aae4c0970bc1b85bf4dc566bdf31de33c7dce593375645600549643ce6f9841
%global source0_hash cd3531066a41dde1f0751e5d3146a936897df35ad5ba1fa49a9f3ace88e6901d
Name:           imhex
Version:        1.38.1
Release:        1%{?dist}
Summary:        A hex editor for reverse engineers and programmers
License:        GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
URL:            https://imhex.werwolv.net/
Source0:        https://github.com/WerWolv/%{name}/releases/download/v%{version}/Full.Sources.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v%{version}.tar.gz#/%{name}-patterns-%{version}.tar.gz
Recommends:     imhex-patterns = %{version}-%{release}
Provides:       bundled(gnulib)
Provides:       bundled(imgui) = 1.90.8
Provides:       bundled(libromfs)
Provides:       bundled(microtar)
Provides:       bundled(libpl) = %{version}
Provides:       bundled(xdgpp)
Provides:       bundled(miniaudio) = 0.11.11
ExclusiveArch:  x86_64 %{arm64}
Patch:          0001-backport-metainfo-update-from-upstream.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glfw-devel
BuildRequires:  json-devel
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm-devel
BuildRequires:  lunasvg-devel
BuildRequires:  lz4-devel
BuildRequires:  mbedtls-devel
BuildRequires:  nativefiledialog-extended-devel
BuildRequires:  xz-devel
BuildRequires:  yara-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
ImHex is a Hex Editor, a tool to display, decode and analyze binary data to
reverse engineer their format, extract informations or patch values in them.

What makes ImHex special is that it has many advanced features that can often
only be found in paid applications. Such features are a completely custom binary
template and pattern language to decode and highlight structures in the data, a
graphical node-based data processor to pre-process values before they're
displayed, a disassembler, diffing support, bookmarks and much much more. At the
same time ImHex is completely free and open source under the GPLv2 language.

%package patterns
Summary:        Hex patterns, include patterns and magic files for the use with the ImHex Hex Editor
License:        GPL-2.0-only
Requires:       imhex >= %{version}-%{release}
%description patterns
Hex patterns, include patterns and magic files for the use with
the ImHex Hex Editor

%package devel
Summary:        Development files for %{name}
License:        GPL-2.0-only
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ImHex -p1
# remove bundled libs we aren't using
rm -rf lib/third_party/{curl,fmt,llvm,nlohmann_json,yara}

# the cmake scripts look for patterns to be in ImHex-Patterns
mkdir -p ImHex-Patterns && tar -xf %{SOURCE1} -C ImHex-Patterns --strip-components=1

# convert this to IMHEX_BUILD_HARDENING=OFF build flag in > 1.38.1
# rhel buildroots already set fortify_source, doing it twice results in build errors

# rhel 9 doesn't support all of the new appstream metainfo tags

%build

CXXFLAGS+=" -Wno-error=deprecated-declarations"
%cmake \
 -D CMAKE_BUILD_TYPE=Release             \
 -D IMHEX_STRIP_RELEASE=OFF              \
 -D IMHEX_OFFLINE_BUILD=ON               \
 -D USE_SYSTEM_NLOHMANN_JSON=ON          \
 -D USE_SYSTEM_FMT=ON                    \
 -D USE_SYSTEM_CURL=ON                   \
 -D USE_SYSTEM_LUNASVG=ON                \
 -D USE_SYSTEM_YARA=ON                   \
 -D USE_SYSTEM_NFD=ON                    \
 -D IMHEX_ENABLE_UNIT_TESTS=ON           \
%cmake_build
%check

%cmake_build --target unit_tests
%ctest --exclude-regex '(Helpers/StoreAPI|Helpers/TipsAPI|Helpers/ContentAPI)'
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -f %{buildroot}%{_metainfodir}/net.werwolv.ImHex.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/net.werwolv.ImHex.metainfo.xml
cp -a lib/third_party/microtar/LICENSE                               %{buildroot}%{_datadir}/licenses/%{name}/microtar-LICENSE
cp -a lib/third_party/xdgpp/LICENSE                                  %{buildroot}%{_datadir}/licenses/%{name}/xdgpp-LICENSE
for i in nodes plugins scripts themes yara;
do
    cp -ra ImHex-Patterns/$i %{buildroot}%{_datadir}/imhex/$i
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n imhex-patterns -f %{oreon_filedir}/imhex-patterns.list
%files -n imhex-devel -f %{oreon_filedir}/imhex-devel.list

%changelog

%autochangelog
