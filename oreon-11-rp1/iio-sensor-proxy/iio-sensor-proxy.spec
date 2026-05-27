%global source0_hash cdf9bdb6ef125d6189069d3f6dc9afb301ce5a17213971e65c5e20a57494593d

Name:           iio-sensor-proxy
Version:        3.8
Release:        %autorelease
Summary:        IIO accelerometer sensor to input device proxy

# tests/unittest_inspector.py is LGPL-2.1-or-later but it is not packaged
License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
Source0:        https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/archive/3.8/iio-sensor-proxy-3.8.tar.bz2

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  systemd
BuildRequires:  umockdev
BuildRequires:  python3-dbusmock
%{?systemd_requires}

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
License:        GFDL-1.1-or-later
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git_am

%build
%meson -Dgtk_doc=true -Dgtk-tests=false
%meson_build

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/monitor-sensor
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_datadir}/dbus-1/system.d/net.hadess.SensorProxy.conf
%{_datadir}/polkit-1/actions/net.hadess.SensorProxy.policy

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8-1
- Prepare for Oreon 11 (RP1)
