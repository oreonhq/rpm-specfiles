%global source0_hash cb49823074f05e33ba868ab159fc445e4ef1b34d61644903b899450ba90cd240
Name:           classification-banner
Version:        1.7.2
Release:        1%{?dist}
Summary:        Displays Classification Banner for a Graphical Session
License:        GPL-2.0-or-later
URL:            https://github.com/SecurityCentral/classification-banner
Source0:        https://github.com/SecurityCentral/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       xrandr
Requires:       python3-gobject
Requires:       gtk3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-classification-banner = %{version}-%{release}
# /oreon:deps
%description
Classification Banner is a python script that will display the
classification level banner of a session with a variety of
configuration options on the primary screen.  This script can
help government and possibly private customers display a 
notification that sensitive material is being displayed - for 
example PII or SECRET Material being processed in a graphical
session. The script has been tested on a variety of graphical
environments such as GNOME2, GNOME3, KDE, twm, icewm, and Cinnamon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -d -m755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m755 %{buildroot}%{_sysconfdir}/xdg/autostart/
install -pm644 contrib/banner.conf %{buildroot}%{_sysconfdir}/%{name}/banner.conf
desktop-file-install \
--dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
contrib/%{name}.desktop
%oreon_autofiles main

%check

export DISPLAY=":0.0"
%pyproject_check_import
%files

%changelog

%autochangelog
