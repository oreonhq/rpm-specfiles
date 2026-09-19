%global source0_hash none

Name:           touchegg
Version:        2.0.18
Release:        4%{?dist}
Summary:        Multi-touch gesture recognizer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/JoseExposito/touchegg
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/953c4227253d91c73f5ce46f89947262ebf45b18.patch#/cmake.patch

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%description
Touchégg is an app that runs in the background and transform the gestures you
make on your touchpad or touchscreen into visible actions in your desktop.

For example, you can swipe up with 3 fingers to maximize a window or swipe left
with 4 finger to switch to the next desktop.

Many more actions and gestures are available and everything is easily
configurable.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
# We cannot restart the service on update, because it breaks clients.
# https://github.com/JoseExposito/touchegg/issues/453
%systemd_postun %{name}.service

%files
%license COPYING COPYRIGHT
%doc README.md CHANGELOG.md
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service

%changelog
%autochangelog
