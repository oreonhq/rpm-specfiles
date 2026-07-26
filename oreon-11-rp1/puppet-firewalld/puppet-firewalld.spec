%global source0_hash 030657668cd1a0c356d4de6b0d347058b70626dba89f170e8b0b210fd3186137

Name:		puppet-firewalld
Version:	0.2.2
Release:	24%{?dist}
Summary:	A Puppet module for FirewallD
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/jpopelka/puppet-firewalld

Source0:	https://github.com/jpopelka/puppet-firewalld/archive/v%{version}.tar.gz

BuildArch:	noarch

Requires:	puppet

%description
A Puppet module used for installing, configuring and managing FirewallD.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn puppet-firewalld-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/puppet/modules/firewalld/
cp -rp manifests/ %{buildroot}%{_datadir}/puppet/modules/firewalld/manifests/
cp -rp templates/ %{buildroot}%{_datadir}/puppet/modules/firewalld/templates/
cp -p metadata.json %{buildroot}%{_datadir}/puppet/modules/firewalld/metadata.json

%files
%doc LICENSE README examples
%{_datadir}/puppet/modules/firewalld

%changelog
%autochangelog
