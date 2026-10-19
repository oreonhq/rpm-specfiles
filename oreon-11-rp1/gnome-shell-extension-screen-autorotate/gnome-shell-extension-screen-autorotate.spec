%global source0_hash 1aa9c6e5609ca15079aaef5a224cb824a8667e851263ea46780b278dddb5f686
%global         extension  screen-rotate
%global         srcname    screen-autorotate
%global         uuid       %{extension}@shyzus.github.io
Name:           gnome-shell-extension-%{srcname}
Version:        29
Release:        1%{?dist}
Summary:        Dynamic Screen rotation for GNOME Shell
License:        GPL-3.0-only
URL:            https://github.com/shyzus/gnome-shell-extension-%{srcname}
Source0:        https://github.com/shyzus/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       iio-sensor-proxy
Provides:       %{extension} = %{version}-%{release}
# oreon:deps
BuildRequires:  gnome-shell-rpm-generators
# /oreon:deps
%description
A GNOME extension to enable screen rotation regardless of touch mode.
This extension uses Mutter's D-Bus API, so it works on both X11 and Wayland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -r %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
