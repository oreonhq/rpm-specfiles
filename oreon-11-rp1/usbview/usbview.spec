%global source0_hash 362cee689e11f7d36ebedccd188c3f777791c7b9c18a9d0bdb74bf69f5a08358

Name:           usbview
Version:        3.1
Release:        7%{?dist}
Summary:        USB topology and device viewer
License:        GPL-2.0-only
URL:            http://www.kroah.com/linux-usb/
Source0:        http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  libappstream-glib
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
Requires:       gdk-pixbuf2-modules-extra
%endif
Requires:       hicolor-icon-theme

%description
Display information about the topology of the devices connected to the USB bus
on a Linux machine. It also displays detailed information on the individual
devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.kroah.usbview.metainfo.xml

%files
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/usbview*
%{_mandir}/man8/usbview*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*%{name}.desktop
%{_metainfodir}/com.kroah.usbview.metainfo.xml

%changelog
%autochangelog
