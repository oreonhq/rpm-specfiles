%global source0_hash 0aeba1848304e2fedaea09e01a549cab9201b48941de21004f29a56435ae39ec
%global plugin_name fas
%global ipa_version 4.8.2
%global freeipa_prefix freeipa
%global freeipa_altprefix ipa
Name:           freeipa-%{plugin_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Fedora Account System extension for FreeIPA
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-infra/freeipa-%{plugin_name}
Source0:        https://github.com/fedora-infra/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A module for FreeIPA with extensions for Fedora Account System.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n freeipa-%{plugin_name}-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{python3_sitelib}/ipaserver/plugins
for j in $(find ipaserver/plugins -name '*.py') ; do
    cp -a $j %{buildroot}%{python3_sitelib}/ipaserver/plugins
done
mkdir -p %{buildroot}/%{_datadir}/ipa/schema.d
for j in $(find schema.d/ -name '*.ldif') ; do
    cp -a $j %{buildroot}/%{_datadir}/ipa/schema.d/
done
mkdir -p %{buildroot}/%{_datadir}/ipa/updates
for j in $(find updates/ -name '*.update') ; do
    cp -a $j %{buildroot}/%{_datadir}/ipa/updates/
done
mkdir -p %{buildroot}/%{_datadir}/ipa/ui/js/plugins
for j in $(find ui/ -name '*.js') ; do
    destdir=%{buildroot}/%{_datadir}/ipa/ui/js/plugins/$(basename ${j%%.js})
    mkdir -p $destdir
    cp -a $j $destdir/
done
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 create-agreement.py %{buildroot}/%{_bindir}/ipa-create-agreement
%oreon_autofiles main

%posttrans -n %{freeipa_prefix}-%{plugin_name}

%python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :
    /bin/systemctl try-restart ipa.service >/dev/null 2>&1 || :
fi
%license COPYING
%doc README.md CONTRIBUTORS.md
%{python3_sitelib}/ipaserver/plugins/*.py
%{python3_sitelib}/ipaserver/plugins/__pycache__/*.pyc
%{_datadir}/ipa/schema.d/*.ldif
%{_datadir}/ipa/updates/*.update
%{_datadir}/ipa/ui/js/plugins/*
%{_bindir}/ipa-create-agreement
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
