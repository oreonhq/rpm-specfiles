%global source0_hash 0f70cbc665217a747e8a098e1a881239e96df270930f47c262ab2ecff290e428
%bcond  tests   1
Name:           swayimg
Version:        5.6
Release:        1%{?dist}
Summary:        Lightweight image viewer for Wayland display servers
License:        MIT
URL:            https://github.com/artemsen/%{name}
Source0:        https://github.com/artemsen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86} riscv64 ppc64 ppc64le
%if %{with tests}
%endif
%if %{with tests}
%endif
Requires:       hicolor-icon-theme
Provides:       bundled(json) = 3.12.0
Provides:       bundled(luabridge) = 3.0~rc4^20240929g713c1f5
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glibc-langpack-en
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
Swayimg is a lightweight image viewer for Wayland display servers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dexr=disabled \
    -Dlicense=false \
    -Dtests=%[%{with tests}?"enabled":"disabled"] \
    -Dversion=%{version}
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/swayimg.desktop
%if %{with tests}
%ifarch s390x
%global gtest_exclude ImageLoadTest.*
%else
%global gtest_exclude ImageLoadTest.heif
%endif
export LANG=en_US.UTF-8 # ImageListTest.SortAlphaUnicode fails with LANG=C
%meson_test --test-args='--gtest_filter=-%{gtest_exclude}'
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
