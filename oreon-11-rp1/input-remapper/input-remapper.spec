%global source0_hash 6ad3d58829e29f2943cbc874b910a94e699428547240f3e5b2a4acbd34e62d2f
Name:           input-remapper
Version:        2.2.1
Release:        1%{?dist}
Summary:        An easy to use tool to change the behaviour of your input devices
License:        GPL-3.0-or-later
URL:            https://github.com/sezanzeb/%{name}
Source0:        https://github.com/sezanzeb/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        README.Fedora
BuildArch:      noarch
Requires:       /usr/bin/pgrep
Requires:       %{py3_dist pycairo}
Requires:       %{py3_dist psutil}
Requires:       gobject-introspection
Requires:       gtk3
Requires:       gtksourceview4
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-input-remapper = %{version}-%{release}
# /oreon:deps
%description
An easy to use tool to change the mapping of your input device buttons. 
Supports mice, keyboards, gamepads, X11, Wayland, combined buttons and 
programmable macros. Allows mapping non-keyboard events (click, joystick, 
wheel) to keys of keyboard devices.
The program works at the evdev interface level, by filtering and redirecting 
the output of physical devices to that of virtual ones.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
cp %{SOURCE1} ./
#Fix rpmlint errors
find inputremapper/injection/macros/ -iname "*.py" -type f -print0 | xargs -0 sed -i -e 's+\s*#\s*!/usr/bin/env python3++'

%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{python3_sitelib}/etc %{buildroot}/etc
mv %{buildroot}%{python3_sitelib}/usr/bin %{buildroot}/usr/bin
mv %{buildroot}%{python3_sitelib}/usr/lib/systemd %{buildroot}/usr/lib/systemd
mv %{buildroot}%{python3_sitelib}/usr/lib/udev %{buildroot}/usr/lib/udev
mv %{buildroot}%{python3_sitelib}/usr/share %{buildroot}/usr/share
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
rm %{buildroot}%{_datadir}/%{name}/inputremapper.Control.conf
rm %{buildroot}%{_datadir}/%{name}/io.github.sezanzeb.input_remapper.metainfo.xml
rm %{buildroot}%{_datadir}/%{name}/%{name}-gtk.desktop
rm %{buildroot}%{_datadir}/%{name}/%{name}.policy
rm %{buildroot}%{_datadir}/%{name}/%{name}.svg
%oreon_autofiles main

%post -n %{name}

%systemd_post %{name}.service
%preun -n %{name}

%systemd_preun %{name}.service
%postun -n %{name}

%systemd_postun_with_restart %{name}.service
%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-gtk.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
export DATA_DIR='%{buildroot}%{_datadir}/%{name}'
%pyproject_check_import -e inputremapper.bin.*
%files

%changelog

%autochangelog
