%global source0_hash 4cadbb5c71047ccd8647c4bbbba57bde0c1b6ca70e6b9c166847a66e12a473d6

%global         extension  screen-rotate
%global         srcname    screen-autorotate
%global         uuid       %{extension}@shyzus.github.io

Name:           gnome-shell-extension-%{srcname}
Version:        28
Release:        %autorelease
Summary:        Dynamic Screen rotation for GNOME Shell

License:        GPL-3.0-only
URL:            https://github.com/shyzus/gnome-shell-extension-%{srcname}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gnome-shell-rpm-generators
Requires:       iio-sensor-proxy
Provides:       %{extension} = %{version}-%{release}

%description
A GNOME extension to enable screen rotation regardless of touch mode.
This extension uses Mutter's D-Bus API, so it works on both X11 and Wayland.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
# nothing to build

%install
# install extension files
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
cp -r %{uuid} %{buildroot}%{_datadir}/gnome-shell/extensions

%files
%license LICENSE.md
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
%autochangelog
