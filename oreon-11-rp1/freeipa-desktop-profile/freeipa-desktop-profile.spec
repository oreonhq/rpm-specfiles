%global source0_hash 267011b8f779586ce5acb86db6fed45da52c355c222306d52f07e4ad2b1cc4ae

%global debug_package %{nil}
%global plugin_name desktop-profile

%global ipa_python3_sitelib %{python3_sitelib}

Name:           freeipa-%{plugin_name}
Version:        0.0.8
Release:        33%{?dist}
Summary:        FleetCommander integration with FreeIPA

BuildArch:      noarch

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/abbra/freeipa-desktop-profile
Source0:        freeipa-desktop-profile-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-ipaserver >= 4.6.0
Requires:      ipa-server-common >= 4.4.1

Requires(post): python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-server
Requires: python3-ipa-%{plugin_name}-client

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

%autosetup

%build
touch debugfiles.list

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %buildroot/%{_sysconfdir}/ipa
%__mkdir_p %buildroot/%_datadir/ipa/schema.d
%__mkdir_p %buildroot/%_datadir/ipa/updates
#%__mkdir_p %buildroot/%_datadir/ipa/ui/js/plugins/deskprofile

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

# Do not package web UI plugin yet
#for j in $(find plugin/ui/%{plugin_name} -name '*.js') ; do
#    %__cp $j %buildroot/%_datadir/ipa/js/plugins/%{plugin_name}
#done

%posttrans
python3 -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    # This must be run in posttrans so that updates from previous
    # execution that may no longer be shipped are not applied.
    /usr/sbin/ipa-server-upgrade --quiet >/dev/null || :

    # Restart IPA processes. This must be also run in postrans so that plugins
    # and software is in consistent state
    # NOTE: systemd specific section

    /bin/systemctl is-enabled ipa.service >/dev/null 2>&1
    if [  $? -eq 0 ]; then
        /bin/systemctl restart ipa.service >/dev/null 2>&1 || :
    fi
fi

%files
%license COPYING
%doc plugin/Feature.mediawiki
%_datadir/ipa/schema.d/*
%_datadir/ipa/updates/*
#_datadir/ipa/ui/js/plugins/deskprofile/*

%files -n freeipa-%{plugin_name}-common
%{_sysconfdir}/ipa/fleetcommander.conf

%files -n python3-ipa-%{plugin_name}-client
%ipa_python3_sitelib/ipaclient/plugins/*

%files -n python3-ipa-%{plugin_name}-server
%ipa_python3_sitelib/ipaserver/plugins/*

%changelog
%autochangelog
