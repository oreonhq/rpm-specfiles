%global source0_hash 541eddc8cc427d1aeb749bc455911fccc87f64a7784bd4bbc35ecb7b56c03ad5

Name:           imhex
Version:        1.37.4
Release:        3%{?dist}
Summary:        A hex editor for reverse engineers and programmers

License:        GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
# imhex is gplv2.  capstone is custom.
# see license dir for full breakdown
URL:            https://imhex.werwolv.net/
# We need the archive with deps bundled
Source0:        https://github.com/WerWolv/%{name}/releases/download/v%{version}/Full.Sources.tar.gz#/%{name}-%{version}.tar.gz
# default to including the same-version patterns as a suggested package
Source1:        https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v%{version}.tar.gz#/%{name}-patterns-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dbus-devel
BuildRequires:  file-devel
BuildRequires:  freetype-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  glfw-devel
BuildRequires:  json-devel
BuildRequires:  libcurl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
BuildRequires:  llvm-devel
BuildRequires:  mbedtls-devel
BuildRequires:  yara-devel
BuildRequires:  nativefiledialog-extended-devel
BuildRequires:  lz4-devel
%if 0%{?rhel} == 9
BuildRequires:  gcc-toolset-13
%endif
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  capstone-devel
%endif
BuildRequires:  lunasvg-devel

Recommends:     imhex-patterns = %{version}-%{release}

Provides:       bundled(gnulib)
%if 0%{?rhel} == 10
Provides:       bundled(capstone) = 5.0.1
%endif
Provides:       bundled(imgui) = 1.90.8
Provides:       bundled(libromfs)
Provides:       bundled(microtar)
Provides:       bundled(libpl) = %{version}
Provides:       bundled(xdgpp)
# working on packaging this, bundling for now as to now delay updates
Provides:       bundled(miniaudio) = 0.11.11

# [7:02 PM] WerWolv: We're not supporting 32 bit anyways soooo
# [11:38 AM] WerWolv: Officially supported are x86_64 and aarch64
ExclusiveArch:  x86_64 %{arm64}

# https://github.com/WerWolv/ImHex/commit/cc772b8581bcc7e161f085385dc527a117e4e940
Patch:          0001-backport-metainfo-update-from-upstream.patch

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
%if 0%{?fedora} || 0%{?rhel} > 9
rm -rf lib/third_party/capstone
%endif

# the cmake scripts look for patterns to be in ImHex-Patterns
mkdir -p ImHex-Patterns && tar -xf %{SOURCE1} -C ImHex-Patterns --strip-components=1

# convert this to IMHEX_BUILD_HARDENING=OFF build flag in > 1.37.4
# rhel buildroots already set fortify_source, doing it twice results in build errors
%if 0%{?rhel}
sed -i '/_FORTIFY_SOURCE/d' cmake/build_helpers.cmake
%endif

# rhel 9 doesn't support all of the new appstream metainfo tags
%if 0%{?rhel} && 0%{?rhel} < 10
sed -i -e '/url type="vcs-browser"/d' \
	-e '/url type="contribute"/d' \
	dist/net.werwolv.ImHex.metainfo.xml
%endif

%build
%if 0%{?rhel} == 9
. /opt/rh/gcc-toolset-13/enable
%set_build_flags
CXXFLAGS+=" -std=gnu++2b"
%endif
# should be removable in > 1.37.4 (fixed upstream)
CXXFLAGS+=" -Wno-error=deprecated-declarations"
%cmake \
 -D CMAKE_BUILD_TYPE=Release             \
 -D IMHEX_STRIP_RELEASE=OFF              \
 -D IMHEX_OFFLINE_BUILD=ON               \
 -D USE_SYSTEM_NLOHMANN_JSON=ON          \
 -D USE_SYSTEM_FMT=ON                    \
 -D USE_SYSTEM_CURL=ON                   \
%if 0%{?fedora} || 0%{?rhel} > 9
 -D USE_SYSTEM_LLVM=ON                   \
 -D USE_SYSTEM_CAPSTONE=ON               \
%endif
 -D USE_SYSTEM_LUNASVG=ON                \
 -D USE_SYSTEM_YARA=ON                   \
 -D USE_SYSTEM_NFD=ON                    \
 -D IMHEX_ENABLE_UNIT_TESTS=ON           \
%if 0%{?rhel}
 -D IMHEX_BUILD_HARDENING=OFF
%endif
# disable built-in build hardening because it is already
# done in rhel buildroots.  adding the flags again from
# upstream generates build errors

%cmake_build

%check
# build binaries required for tests
%cmake_build --target unit_tests
%ctest --exclude-regex '(Helpers/StoreAPI|Helpers/TipsAPI|Helpers/ContentAPI)'
# Helpers/*API exclude tests that require network access

%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# this is a symlink for the old appdata name that we don't need
rm -f %{buildroot}%{_metainfodir}/net.werwolv.ImHex.appdata.xml

# AppData
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/net.werwolv.ImHex.metainfo.xml

# install licenses
%if 0%{?rhel} == 9
cp -a lib/third_party/capstone/LICENSE.TXT                           %{buildroot}%{_datadir}/licenses/%{name}/capstone-LICENSE
cp -a lib/third_party/capstone/suite/regress/LICENSE                 %{buildroot}%{_datadir}/licenses/%{name}/capstone-regress-LICENSE
%endif
cp -a lib/third_party/microtar/LICENSE                               %{buildroot}%{_datadir}/licenses/%{name}/microtar-LICENSE
cp -a lib/third_party/xdgpp/LICENSE                                  %{buildroot}%{_datadir}/licenses/%{name}/xdgpp-LICENSE

# remove when all paths are added to the cmake file
# https://github.com/WerWolv/ImHex/blob/master/cmake/build_helpers.cmake#L477
for i in nodes plugins scripts themes yara;
do
    cp -ra ImHex-Patterns/$i %{buildroot}%{_datadir}/imhex/$i
done

%files
%license %{_datadir}/licenses/%{name}/
%doc README.md
%{_bindir}/imhex
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libimhex.so.*
%{_libdir}/%{name}/
%{_metainfodir}/net.werwolv.ImHex.metainfo.xml
%exclude %{_bindir}/imhex-updater
%{_datadir}/mime/packages/%{name}.xml

%files patterns
%license ImHex-Patterns/LICENSE
%{_datadir}/%{name}/{constants,encodings,includes,magic,nodes,patterns,plugins,scripts,themes,yara}/

%files devel
%{_libdir}/libimhex.so
%{_datadir}/%{name}/sdk/

%changelog
%autochangelog
