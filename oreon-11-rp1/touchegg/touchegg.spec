%global source0_hash 7cf0b9239f414d9484495f2a57a28c1c99b3d7a7ae5767d10f0464809ae32e0b
Name:           touchegg
Version:        2.0.18
Release:        1%{?dist}
Summary:        Multi-touch gesture recognizer
License:        GPL-3.0-or-later
URL:            https://github.com/JoseExposito/touchegg
Source0:        https://github.com/JoseExposito/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/953c4227253d91c73f5ce46f89947262ebf45b18.patch#/cmake.patch
ExcludeArch:    %{ix86}
# oreon:deps
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
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Touchégg is an app that runs in the background and transform the gestures you
make on your touchpad or touchscreen into visible actions in your desktop.

For example, you can swipe up with 3 fingers to maximize a window or swipe left
with 4 finger to switch to the next desktop.

Many more actions and gestures are available and everything is easily
configurable.

%prep
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
