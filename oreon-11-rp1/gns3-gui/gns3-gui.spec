%global source0_hash 3357dfeb76d01d2bf8e72aa201f39061b7ceae9d6002c0d1c2a6283434a9a1b2
%global git_tag %{version}
Name:           gns3-gui
Version:        3.0.6
Release:        1%{?dist}
Summary:        GNS3 graphical user interface
License:        GPL-3.0-or-later
URL:            http://gns3.com
Source0:        https://github.com/GNS3/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source3:        %{name}.appdata.xml
BuildArch:      noarch
Requires: telnet 
Requires: socat
Requires: python3-jsonschema 
Requires: python3-psutil 
Requires: python3-pyqt6
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

This package contains the client graphical user interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{git_tag}

# Relax strict reqs
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r 's/sentry-sdk.*//g' requirements.txt
sed -i -r 's/truststore.*//g' requirements.txt
# Lower psutil>=5.8.0
sed -i -r 's/psutil>=7.2.2/psutil>=5.8.0/' requirements.txt
sed -i -r 's/distro>=1.9.*/distro>=1.5.0/' requirements.txt
sed -i -r 's/jsonschema>=4.26.0,<4.27.*/jsonschema>=3.2.0/' requirements.txt
sed -i -r '/jsonschema>=4.25.1/d' requirements.txt

# Disable update alerts
sed -i 's/"check_for_update": True,/"check_for_update": False,/' gns3/settings.py

%build

%py3_build
%install
%py3_install
for lib in `find %{buildroot}/%{python3_sitelib}/ -name '*.py'`; do
 echo $lib
 sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done
find %{buildroot}/%{python3_sitelib}/ -name '.keep' -type f -delete
find %{buildroot}/%{python3_sitelib}/ -type f -exec chmod -x {} \;
mkdir -p %{buildroot}/%{_datadir}/appdata/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/appdata/
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/gns3*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
