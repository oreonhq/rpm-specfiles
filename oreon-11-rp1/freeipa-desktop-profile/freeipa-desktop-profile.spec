%global source0_hash 267011b8f779586ce5acb86db6fed45da52c355c222306d52f07e4ad2b1cc4ae
%global debug_package %{nil}
%global plugin_name desktop-profile
%global ipa_python3_sitelib %{python3_sitelib}
Name:           freeipa-%{plugin_name}
Version:        0.0.8
Release:        1%{?dist}
Summary:        FleetCommander integration with FreeIPA
BuildArch:      noarch
License:        GPL-3.0-or-later
URL:            https://github.com/abbra/freeipa-desktop-profile
Source0:        freeipa-desktop-profile-%{version}.tar.gz
Requires:      ipa-server-common >= 4.4.1
Requires(post): python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-client
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-ipaserver
# /oreon:deps
%description
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander.

%package -n freeipa-%{plugin_name}-common
Summary: Common package for client side FleetCommander integration with FreeIPA
%description  -n freeipa-%{plugin_name}-common
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds common files needed by client-side packages

%package -n python3-ipa-%{plugin_name}-server
Summary: Server side of FleetCommander integration with FreeIPA for Python 3
Requires: python3-ipaserver
%description  -n python3-ipa-%{plugin_name}-server
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds server-side support for Python 3
version of FreeIPA

%package -n python3-ipa-%{plugin_name}-client
Summary: Client side of FleetCommander integration with FreeIPA for Python 3
Requires: python3-ipaclient
Requires: freeipa-%{plugin_name}-common
%description  -n python3-ipa-%{plugin_name}-client
A module for FreeIPA to allow managing desktop profiles defined
by the FleetCommander. This package adds client-side support for Python 3
version of FreeIPA

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

touch debugfiles.list
%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %buildroot/%{_sysconfdir}/ipa
%__mkdir_p %buildroot/%_datadir/ipa/schema.d
%__mkdir_p %buildroot/%_datadir/ipa/updates
%__cp plugin/etc/ipa/fleetcommander.conf %buildroot/%{_sysconfdir}/ipa/
for s in ipaclient ipaserver; do
    %__mkdir_p %{buildroot}%{ipa_python3_sitelib}/$s/plugins
    for j in $(find plugin/$s/plugins -name '*.py') ; do
        %__cp $j %{buildroot}%{ipa_python3_sitelib}/$s/plugins
    done
done
for j in $(find plugin/schema.d -name '*.ldif') ; do
    %__cp $j %buildroot/%_datadir/ipa/schema.d
done
for j in $(find plugin/updates -name '*.update') ; do
    %__cp $j %buildroot/%_datadir/ipa/updates
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%posttrans

python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1
if [ $? -eq 0 ]; then
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :
    /bin/systemctl is-enabled ipa.service >/dev/null 2>&1
    if [  $? -eq 0 ]; then
        /bin/systemctl restart ipa.service >/dev/null 2>&1 || :
    fi
fi
%files -f %{oreon_filedir}/main.list
%files -n freeipa-desktop-profile-common -f %{oreon_filedir}/freeipa-desktop-profile-common.list
%files -n python3-ipa-desktop-profile-server -f %{oreon_filedir}/python3-ipa-desktop-profile-server.list
%files -n python3-ipa-desktop-profile-client -f %{oreon_filedir}/python3-ipa-desktop-profile-client.list

%changelog

%autochangelog
