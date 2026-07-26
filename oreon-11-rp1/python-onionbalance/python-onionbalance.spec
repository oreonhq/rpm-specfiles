%global source0_hash 3421e5fdef24674432021c605164c790ff7f66ec2c111f3e610b212c058b33ea

%global pypi_name OnionBalance
%global pkgname onionbalance
%global sum Load-balancing for Tor onion services

%global toruser toranon

Name:           python-%{pkgname}
Version:        0.2.1
Release:        21%{?dist}
Summary:        %{sum}

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://onionbalance.readthedocs.io
Source0:        %pypi_source
Source1:        onionbalance.service
Source2:        onionbalance.tmpfiles
Source3:        onionbalance.logrotate
Source5:        onionbalance.torrc.example
Source6:        README.fedora

Patch0:         python-onionbalance-fix-versioneer.patch
# Drop dependency on future
# Proposed upstream: https://github.com/torproject/onionbalance/pull/50
Patch1:         drop-dependency-on-future.patch

BuildArch: noarch

BuildRequires: systemd-units

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-stem >= 1.8
BuildRequires:  python3-PyYAML >= 4.2b1
BuildRequires:  python3-cryptography >= 2.5
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-setproctitle >= 1.1.9

BuildRequires: systemd

%global _description %{expand:
OnionBalance provides load-balancing and redundancy for Tor
onion services by distributing requests to multiple back-end
Tor instances.}

%description %_description

%package -n python3-%{pkgname}
Summary:   %{sum}
Requires:  python3-setuptools
Requires:  python3-stem >= 1.8
Requires:  python3-PyYAML >= 4.2b1
Requires:  python3-cryptography >= 2.5
Requires:  python3-pycryptodomex
Requires:  python3-setproctitle >= 1.1.9
%{?python_provide:%python_provide python3-%{pkgname}}
Requires: tor
Requires: logrotate
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description -n python3-%{pkgname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

# Create a sysusers.d config file
cat >python-onionbalance.sysusers.conf <<EOF
u onionbalance -:%{toruser} '%{pkgname} daemon user' %{_localstatedir}/lib/%{pkgname} -
EOF

%build
%py3_build

%install
%py3_install

install -d        %{buildroot}/etc/logrotate.d
install -d        %{buildroot}/%{_sysconfdir}/%{pkgname}
install -d        %{buildroot}/%{_localstatedir}/log/%{pkgname}
install -d        %{buildroot}/%{_localstatedir}/lib/%{pkgname}
install -d -m 755 %{buildroot}/%{_unitdir}
install -d -m 755 %{buildroot}/%{_tmpfilesdir}

install -p -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{pkgname}.service
install -p -m 644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{pkgname}.conf
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{pkgname}.conf
%if 0%{?with_docs}
install -d -m 755 %{buildroot}/%{_mandir}/man1
cp docs/_build/man/%{pkgname}* %{buildroot}/%{_mandir}/man1/
%endif

install -p -m 644 %{SOURCE5} .
install -p -m 644 %{SOURCE6} .

install -m0644 -D python-onionbalance.sysusers.conf %{buildroot}%{_sysusersdir}/python-onionbalance.conf

%post -n python3-%{pkgname}
%systemd_post onionbalance.service

%preun -n python3-%{pkgname}
%systemd_preun onionbalance.service

%postun -n python3-%{pkgname}
%systemd_postun_with_restart onionbalance.service

%files -n python3-%{pkgname}
%doc README.rst
%doc README.fedora
%doc onionbalance.torrc.example
%license COPYING
%if 0%{?with_docs}
%doc docs/_build/html
%doc %attr(0644,root,root) %{_mandir}/man1/%{pkgname}*
%endif
%if 0%{?for_el7}
%{python2_sitelib}/*
%else
%{python3_sitelib}/*
%endif
%{_bindir}/%{pkgname}
%{_bindir}/%{pkgname}-config
%{_unitdir}/%{pkgname}.service
%{_tmpfilesdir}/%{pkgname}.conf
%dir %attr(0750,root,%{toruser}) %{_sysconfdir}/%{pkgname}
%dir %attr(0750,%{pkgname},%{toruser}) %{_localstatedir}/log/%{pkgname}
%dir %attr(0750,%{pkgname},%{toruser}) %{_localstatedir}/lib/%{pkgname}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{pkgname}.conf
%{_sysusersdir}/python-onionbalance.conf

%changelog
%autochangelog
