%global source0_hash ac3556d2e263d0586f28e35ff9821646e81189ace66029319b9ef389e863f47f
%global forgeurl https://gitlab.com/CalcProgrammer1/OpenRGB
%global commit 74cbdcce55711f57b3ca4439d3136f5bb7068db7
ExcludeArch: %{ix86}
Name:           openrgb
Version:        1.0~rc2
%forgemeta
Release:        1%{?dist}
Summary:        Open source RGB lighting control
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://openrgb.org
Source0:        %{forgeurl}/-/archive/%{commit}/OpenRGB-%{commit}.tar.bz2
Requires:       %{name}-udev-rules = %{version}-%{release}
Requires:       hicolor-icon-theme
Provides:       bundled(hueplusplus) = 1.2.0
Provides:       bundled(libcmmk)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
One of the biggest complaints about RGB is the software ecosystem surrounding
it.  Every manufacturer has their own app, their own brand, their own style.  If
you want to mix and match devices, you end up with a ton of conflicting,
functionally identical apps competing for your background resources.  On top of
that, these apps are proprietary and Windows-only.  Some even require online
accounts.  What if there was a way to control all of your RGB devices from a
single app, on Windows, Linux, and MacOS, without any nonsense?  That is what
OpenRGB sets out to achieve.  One app to rule them all.

# Separate Udev rules package is useful for Flatpak package and others
%package        udev-rules
Summary:        Udev rules for %{name}
BuildArch:      noarch
Requires:       systemd-udev
Suggests:       %{name} = %{version}-%{release}
%description    udev-rules
Udev rules for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Remove some bundled libs
pushd dependencies
rm -rf       \
  hidapi     \
  hidapi-win \
  libusb-*   \
  mbedtls-*  \
  %{nil}
popd

%build

%qmake_qt5 \
    .      \
    %{nil}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%post -n %{name}-udev-rules

if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n openrgb-udev-rules -f %{oreon_filedir}/openrgb-udev-rules.list

%changelog

%autochangelog
