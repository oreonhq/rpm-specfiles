Name:           cups-pk-helper
Version:        0.2.7
Release:        12%{?dist}
Summary:        A helper that makes system-config-printer use PolicyKit

License:        GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/cups-pk-helper/
Source0:        http://www.freedesktop.org/software/cups-pk-helper/releases/cups-pk-helper-%{version}.tar.xz

Patch0:         polkit_result.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  cups-devel >= 1.6
BuildRequires:  glib2-devel >= 2.36.0
BuildRequires:  polkit-devel >= 0.97
BuildRequires:  meson

Requires:       cups-libs%{?_isa} >= 1.6
Requires:       glib2%{?_isa} >= 2.36.0


%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_libexecdir}/cups-pk-helper-mechanism
%config(noreplace) %{_datadir}/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%{_datadir}/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%{_datadir}/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy
%doc AUTHORS COPYING NEWS


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.7-12
- Prepare for Oreon 11 (RP1)
