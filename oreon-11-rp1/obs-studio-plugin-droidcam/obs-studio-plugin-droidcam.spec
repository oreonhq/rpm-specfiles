%global source0_hash fd72d7e2a5911b3820c5e4690c681b92cdd3755dd1a624b6cd7ae063452a3082

Name:           obs-studio-plugin-droidcam
Version:        2.4.3
Release:        %autorelease
Summary:        Use your phone as a camera in OBS Studio

# Public Domain File
# src/mdns.h
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://droidcam.app/obs
Source0:        https://github.com/dev47apps/droidcam-obs-plugin/archive/%{version}/droidcam-obs-plugin-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libusbmuxd-2.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)

Requires:       obs-studio%{?_isa}
Enhances:       obs-studio%{?_isa}

%description
Use your phone as a camera directly in OBS.
You can add as many devices as you want,
either using WiFi or USB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n droidcam-obs-plugin-%{version} -p1

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

%files
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/droidcam-obs.so
%{_datadir}/obs/obs-plugins/droidcam-obs/

%changelog
%autochangelog
