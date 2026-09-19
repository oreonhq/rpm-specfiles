%global source0_hash 4364d8b25b23d2ef4856d19724fd6c67de9a2d3c1b3833f7a5441145fd39dcb7

%global relver 1.2

Name:       lightdm-gtk-greeter-settings
Version:    %{relver}.2
Release:    32%{?dist}
Summary:    Settings editor for LightDM GTK+ Greeter

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:    GPL-3.0-only
URL:        https://launchpad.net/lightdm-gtk-greeter-settings
Source0:    https://launchpad.net/%{name}/%{relver}/%{version}/+download/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools

Requires:  lightdm-gtk
Requires:  python3-gobject

%description
Just a small dialog to make it easier for users to modify the settings
of lightdm-gtk-greeter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
rm -f PKG-INFO

# Rename the ubuntu references to fedora
sed -i -e 's@com.ubuntu.pkexec@com.fedora.pkexec@g' com.ubuntu.pkexec.lightdm-gtk-greeter-settings.policy.in \
 po/*
mv com.ubuntu.pkexec.lightdm-gtk-greeter-settings.policy.in com.fedora.pkexec.lightdm-gtk-greeter-settings.policy.in

%build
%py3_build

%install
# %%py3_install des not work properly here.
%{__python3} setup.py install --root=$RPM_BUILD_ROOT --optimize=1

# Remove shebang from files
for lib in %{buildroot}%{python3_sitelib}/lightdm_gtk_greeter_settings/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/lightdm-gtk-greeter-settings
%{_bindir}/lightdm-gtk-greeter-settings-pkexec
%{python3_sitelib}/lightdm_gtk_greeter_settings-%{version}-py*.egg-info
%{python3_sitelib}/lightdm_gtk_greeter_settings/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/lightdm-gtk-greeter-settings*
%{_datadir}/lightdm-gtk-greeter-settings/
%{_datadir}/polkit-1/actions/com.fedora.pkexec.lightdm-gtk-greeter-settings.policy

%changelog
%autochangelog
