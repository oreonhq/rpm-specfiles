%global source0_hash b410a49db085fcb01e56cd80478dd54e76e5a9a457712d82f4d214f56a7b9c17
Name:           rpi-imager
Version:        2.0.11.1
Release:        1%{?dist}
Summary:        Graphical user-interface to write disk images and format SD cards
License:        Apache-2.0
URL:            https://github.com/raspberrypi/rpi-imager
Source0:        https://github.com/raspberrypi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://gitlab.archlinux.org/archlinux/packaging/packages/rpi-imager/-/raw/main/remove-vendoring.patch
ExcludeArch:    s390x
Requires:       hicolor-icon-theme
Requires:       dosfstools
Requires:       util-linux
Recommends:     udisks2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libzstd-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Graphical user-interface to download and write Raspberry Pi disk images, or
write custom disk images and format SD cards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

pushd src
%cmake -GNinja \
    -DBUILD_SHARED_LIBS=OFF \
    -DENABLE_CHECK_VERSION=OFF \
    -DENABLE_TELEMETRY=OFF \
    -DGENERATE_TIMEZONES_FROM_IANA=OFF
%cmake_build
popd
%install
pushd src
%cmake_install
popd
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
