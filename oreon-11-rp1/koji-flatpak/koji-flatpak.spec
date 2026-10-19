%global source0_hash 1200a8a28ad032245bc1472ed1defb4bfd82bf431d539ebedb5991b9b00d5887
%global project_version 0.7
%global flatpak_module_tools_min_version 1.1
Name:           koji-flatpak
Version:        %{project_version}
Release:        1%{?dist}
Summary:        Koji plugins for building Flatpaks
License:        LGPL-2.1-only
URL:            https://pagure.io/koji-flatpak
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
koji-flatpak adds the ability to build Flatpak containers to Koji. It has
plugins for the XMLRPC hub, the builder nodes, and for the Koji command
line.

%package common
Summary: Common files for Flatpak plugins for Koji
%description common
Common files for Flatpak plugins for Koji.

%package hub
Summary: Flatpak plugin for the Koji XMLRPC hub
Requires: %{name}-common = %{version}-%{release}
Requires: koji-hub
%description hub
koji-flatpak adds the ability to build Flatpak containers to Koji.
This is the plugin for the Koji XMLRPC hub.

%package builder
Summary: Flatpak plugin for the Koji builder nodes
Requires: %{name}-common = %{version}-%{release}
Requires: koji-builder
Requires: python3-flatpak-module-tools >= %{flatpak_module_tools_min_version}
Requires: skopeo
%description -n %{name}-builder
koji-flatpak adds the ability to build Flatpak containers to Koji.
This is the Flatpak plugin for the Koji builder nodes.

%package cli
Summary: Flatpak plugin for the Koji command line
Requires: %{name}-common = %{version}-%{release}
Requires: koji
%description cli
koji-flatpak adds the ability to build Flatpak containers to Koji.
This is the Flatpak plugin for the Koji command line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{project_version}

%build

%install
install -d %{buildroot}/%{_prefix}/lib/koji-hub-plugins
install -p -m 0755 koji_flatpak/plugins/flatpak_hub_plugin.py %{buildroot}/%{_prefix}/lib/koji-hub-plugins/flatpak.py
%py_byte_compile %{__python3} %{buildroot}/%{_prefix}/lib/koji-hub-plugins/flatpak.py
install -d %{buildroot}/%{_prefix}/lib/koji-builder-plugins
install -p -m 0755 koji_flatpak/plugins/flatpak_builder_plugin.py %{buildroot}/%{_prefix}/lib/koji-builder-plugins/flatpak.py
%py_byte_compile %{__python3} %{buildroot}/%{_prefix}/lib/koji-builder-plugins/flatpak.py
install -d %{buildroot}%{python3_sitelib}/koji_cli_plugins
install -p -m 0644 koji_flatpak/plugins/flatpak_cli_plugin.py %{buildroot}%{python3_sitelib}/koji_cli_plugins/flatpak.py
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/koji_cli_plugins/flatpak.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n koji-flatpak-common -f %{oreon_filedir}/koji-flatpak-common.list
%files -n koji-flatpak-hub -f %{oreon_filedir}/koji-flatpak-hub.list
%files -n koji-flatpak-builder -f %{oreon_filedir}/koji-flatpak-builder.list
%files -n koji-flatpak-cli -f %{oreon_filedir}/koji-flatpak-cli.list

%changelog

%autochangelog
