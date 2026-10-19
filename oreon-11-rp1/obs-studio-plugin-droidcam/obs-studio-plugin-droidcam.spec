%global source0_hash f02dc570c0dfc3c83124d3b9758555c9b0f93d76633d2c19537154e74ddf1d2f
Name:           obs-studio-plugin-droidcam
Version:        2.5.1
Release:        1%{?dist}
Summary:        Use your phone as a camera in OBS Studio
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://droidcam.app/obs
Source0:        https://github.com/dev47apps/droidcam-obs-plugin/archive/%{version}/droidcam-obs-plugin-%{version}.tar.gz
Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libusbmuxd-2.0)
# /oreon:deps
%description
Use your phone as a camera directly in OBS.
You can add as many devices as you want,
either using WiFi or USB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir droidcam-obs-plugin-%{version}
%oreon_prep
%build

mkdir -p build
%make_build \
    LIBUSBMUXD=libusbmuxd-2.0 \
    LIBIMOBILEDEV=libimobiledevice-1.0 \
    ALLOW_STATIC=no \
    ENABLE_GUI=yes
%install
mkdir -p %{buildroot}%{_libdir}/obs-plugins
install -pm 0755 build/droidcam-obs.so %{buildroot}%{_libdir}/obs-plugins
mkdir -p %{buildroot}%{_datadir}/obs/obs-plugins/droidcam-obs
cp -r data/* %{buildroot}%{_datadir}/obs/obs-plugins/droidcam-obs
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
