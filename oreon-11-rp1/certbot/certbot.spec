%global source0_hash 4e4a0cf6a2a1212708a6535edef52e5db95f41705616764670e66ad07d9c8118

%global oldpkg letsencrypt

# build docs on Fedora but not on RHEL (not all sphinx packages available)
%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif
%bcond_without tests

%global         SPHINXBUILD sphinx-build-3

%global MODULES %{expand:certbot-dns-cloudflare certbot-dns-digitalocean certbot-dns-dnsimple certbot-dns-dnsmadeeasy certbot-dns-gehirn certbot-dns-linode certbot-dns-luadns certbot-dns-nsone certbot-dns-ovh certbot-dns-rfc2136 certbot-dns-route53 certbot-dns-sakuracloud}
%if 0%{?fedora} || 0%{?rhel} < 9
  %global MODULES %{expand:%MODULES certbot-dns-google}
%endif

Name:           certbot
Version:        5.2.2
Release:        3%{?dist}
Summary:        A free, automated certificate authority client

License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Source10:       certbot-renew-systemd.service
Source11:       certbot-renew-systemd.timer
Source12:       certbot-sysconfig-certbot
Source13:       certbot-cli.ini
Source14:       certbot-README.fedora
Source15:       certbot.logrotate

# disable one test which tries to access the network
# https://github.com/certbot/certbot/issues/10354
Patch1:         certbot-disable-test_lock_order-renew.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# "test" extras also needs "python3dist(types-mock)", "python3dist(types-pyrfc3339)"
# which are not available on Fedora. Just require "pytest" here.
BuildRequires:  python3-pytest
# for docs
%if 0%{?fedora}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

# For the systemd macros
%{?systemd_requires}
BuildRequires:  systemd

# Need to label the httpd rw stuff correctly until base selinux policy updated
Requires(post): %{_sbindir}/restorecon

Requires: python3-certbot = %{version}-%{release}

Obsoletes: %{oldpkg} < 0.6.0
Provides: %{oldpkg} = %{version}-%{release}

%define _description() \%description -n %1\
\%{summary}

%define _package() \%package -n %1\
Summary:    %2 plugin for certbot\
\%if 0\%{?fedora}\
Provides:      %2 = \%{version}-\%{release}\
# adding these as manual requires because we nuke them with sed for the loop\
# of installing buildreqs and these would cause blocking since they aren't built yet\
Requires:      python3-acme = \%{version}-\%{release}\
Requires:      python3-certbot = \%{version}-\%{release}\
\%endif

%define _package_doc() \%package -n %1\
Summary:    Documenation for %1 libraries
Requires:   font(fontawesome)

%define _files() \%files -n python3-certbot-dns-%1\
\%license certbot-dns-%1/LICENSE.txt\
\%doc certbot-dns-%1/README.rst\
\%{python3_sitelib}/certbot_dns_%1/\
\%{python3_sitelib}/certbot_dns_%1-\%{version}.dist-info/

%define _files_doc() \%files -n python-%1-doc\
\%license %1/LICENSE.txt\
\%doc %1/README.rst\
\%doc %1/docs/_build/html

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python3-certbot
Summary:    Python 3 libraries used by certbot
Requires:   python3-acme

%package -n python3-acme
Summary:    Python library for the ACME protocol

%package -n python3-certbot-apache
Summary:    The apache plugin for certbot
Requires:   mod_ssl
# adding these as manual requires because we nuke them with sed for the loop
# of installing buildreqs and these would cause blocking since they aren't built yet
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
# Provide the name users expect as a certbot plugin
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
Provides:   certbot-apache = %{version}-%{release}
%endif

%package -n python3-certbot-nginx
Summary:     The nginx plugin for certbot
# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:      certbot-nginx = %{version}-%{release}
%endif
# adding these as manual requires because we nuke them with sed for the loop
# of installing buildreqs and these would cause blocking since they aren't built yet
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
# Recommend the CLI as that will be the interface most use
Recommends:    certbot >= %{version}

%_package python3-certbot-dns-cloudflare certbot-dns-cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing deps for el9
%_package python3-certbot-dns-google certbot-dns-google
%endif
%_package python3-certbot-dns-digitalocean certbot-dns-digitalocean
%_package python3-certbot-dns-dnsimple certbot-dns-dnsimple
%_package python3-certbot-dns-dnsmadeeasy certbot-dns-dnsmadeeasy
%_package python3-certbot-dns-gehirn certbot-dns-gehirn
%_package python3-certbot-dns-linode certbot-dns-linode
%_package python3-certbot-dns-luadns certbot-dns-luadns
%_package python3-certbot-dns-nsone certbot-dns-nsone
%_package python3-certbot-dns-ovh certbot-dns-ovh
%_package python3-certbot-dns-rfc2136 certbot-dns-rfc2136
%_package python3-certbot-dns-route53 certbot-dns-route53
%_package python3-certbot-dns-sakuracloud certbot-dns-sakuracloud
%if 0%{?fedora}
%_package_doc python-acme-doc
%_package_doc python-certbot-doc
%_package_doc python-certbot-dns-cloudflare-doc
%_package_doc python-certbot-dns-digitalocean-doc
%_package_doc python-certbot-dns-dnsimple-doc
%_package_doc python-certbot-dns-dnsmadeeasy-doc
%_package_doc python-certbot-dns-gehirn-doc
%_package_doc python-certbot-dns-google-doc
%_package_doc python-certbot-dns-linode-doc
%_package_doc python-certbot-dns-luadns-doc
%_package_doc python-certbot-dns-nsone-doc
%_package_doc python-certbot-dns-ovh-doc
%_package_doc python-certbot-dns-rfc2136-doc
%_package_doc python-certbot-dns-route53-doc
%_package_doc python-certbot-dns-sakuracloud-doc
%endif

%description -n python3-certbot
The python3 libraries to interface with certbot

%description -n python3-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Let's Encrypt project.

%description -n python3-certbot-apache
Plugin for certbot that allows for automatic configuration of apache

%description -n python3-certbot-nginx
Plugin for certbot that allows for automatic configuration of ngnix

%_description python3-certbot-dns-cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing el9 deps
%_description python3-certbot-dns-google
%endif
%_description python3-certbot-dns-digitalocean
%_description python3-certbot-dns-dnsimple
%_description python3-certbot-dns-dnsmadeeasy
%_description python3-certbot-dns-gehirn
%_description python3-certbot-dns-linode
%_description python3-certbot-dns-luadns
%_description python3-certbot-dns-nsone
%_description python3-certbot-dns-ovh
%_description python3-certbot-dns-rfc2136
%_description python3-certbot-dns-route53
%_description python3-certbot-dns-sakuracloud
%if 0%{?fedora}
%_description python-acme-doc
%_description python-certbot-doc
%_description python-certbot-dns-cloudflare-doc
%_description python-certbot-dns-digitalocean-doc
%_description python-certbot-dns-dnsimple-doc
%_description python-certbot-dns-dnsmadeeasy-doc
%_description python-certbot-dns-gehirn-doc
%_description python-certbot-dns-google-doc
%_description python-certbot-dns-linode-doc
%_description python-certbot-dns-luadns-doc
%_description python-certbot-dns-nsone-doc
%_description python-certbot-dns-ovh-doc
%_description python-certbot-dns-rfc2136-doc
%_description python-certbot-dns-route53-doc
%_description python-certbot-dns-sakuracloud-doc
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info

%generate_buildrequires
for module in acme certbot %{MODULES} certbot-apache certbot-nginx
do
  cd $module
  sed -Ei '/(acme|certbot)>=\{version\}/d' setup.py
    %pyproject_buildrequires
  cd ..
done

%build
for module in acme certbot %{MODULES} certbot-apache certbot-nginx
do
  cd $module
    %pyproject_wheel
  cd ..
done

%install
%pyproject_install

%if 0%{?fedora}
# not all modules have docs
for module in acme certbot %{MODULES}
do
cd $module/docs && make html SPHINXBUILD=%{SPHINXBUILD}
rm -rf docs/_build/html/{.buildinfo,man,_sources}
cd ../..
done
%endif

mv %{buildroot}%{_bindir}/certbot{,-3}

# Add compatibility symlink as requested by upstream conference call
ln -s certbot %{buildroot}/usr/bin/%{oldpkg}
# Put the man pages in place
# install -pD -t %%{buildroot}%%{_mandir}/man1 docs/_build/man/*1*
# Use python3 for F26+ or if python2 is disabled
ln -s certbot-3 %{buildroot}%{_bindir}/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE10} %{buildroot}%{_unitdir}/certbot-renew.service
install -Dm 0644 --preserve-timestamps %{SOURCE11} %{buildroot}%{_unitdir}/certbot-renew.timer
install -Dm 0644 --preserve-timestamps %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE13} %{buildroot}%{_sysconfdir}/letsencrypt/cli.ini
install -Dm 0644 --preserve-timestamps %{SOURCE15} %{buildroot}%{_sysconfdir}/logrotate.d/certbot
cp -a %{SOURCE14} %{_builddir}/%{name}-%{version}/README.fedora

# project uses old letsencrypt dir for compatibility
install -dm 0755 %{buildroot}%{_sysconfdir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_sharedstatedir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_localstatedir}/log/letsencrypt

%if %{with tests}
%check
for module in acme certbot %{MODULES} certbot-apache certbot-nginx; do
pushd $module
%pytest -v -W ignore::DeprecationWarning
popd
done
%endif

# The base selinux policies don't handle the certbot directories yet so set them up manually
%post
%if 0%{?rhel} && 0%{?rhel} <= 7
semanage fcontext -a -t cert_t '%{_sysconfdir}/(letsencrypt|certbot)/(live|archive)(/.*)?'
%endif
restorecon -R %{_sysconfdir}/letsencrypt || :
%systemd_post certbot-renew.timer

# Remind users to start certbot-renew.timer if they need certbot to automatically renew certs
if [ "$1" -eq 1 ] ; then
  echo ""
  echo "Certbot auto renewal timer is not started by default."
  echo "Run 'systemctl start certbot-renew.timer' to enable automatic renewals."
fi

%preun
%systemd_preun certbot-renew.timer

%postun
%systemd_postun certbot-renew.timer

%files -n certbot
%license LICENSE.txt
%doc certbot/README.rst README.fedora certbot/CHANGELOG.md
%{_bindir}/certbot
%{_bindir}/%{oldpkg}
%dir %{_sysconfdir}/%{oldpkg}
%dir %{_sharedstatedir}/%{oldpkg}
%dir %{_localstatedir}/log/letsencrypt
%config(noreplace) %{_sysconfdir}/%{oldpkg}/cli.ini
%config(noreplace) %{_sysconfdir}/sysconfig/certbot
%config(noreplace) %{_sysconfdir}/logrotate.d/certbot
%{_unitdir}/certbot-renew.service
%{_unitdir}/certbot-renew.timer

%files -n python3-certbot
%license certbot/LICENSE.txt
%doc certbot/README.rst certbot/CHANGELOG.md
%{_bindir}/certbot-3
%{python3_sitelib}/certbot/
%{python3_sitelib}/certbot-%{version}.dist-info/

%files -n python3-acme
%license acme/LICENSE.txt
%doc acme/README.rst
%{python3_sitelib}/acme/
%{python3_sitelib}/acme-%{version}.dist-info/

%files -n python3-certbot-apache
%license certbot-apache/LICENSE.txt
%doc certbot-apache/README.rst
%{python3_sitelib}/certbot_apache/
%{python3_sitelib}/certbot_apache-%{version}.dist-info/

%files -n python3-certbot-nginx
%license certbot-nginx/LICENSE.txt
%doc certbot-nginx/README.rst
%{python3_sitelib}/certbot_nginx/
%{python3_sitelib}/certbot_nginx-%{version}.dist-info/

%_files cloudflare
%if 0%{?fedora} || 0%{?rhel} < 9
# missing el9 deps
%_files google
%endif
%_files digitalocean
%_files dnsimple
%_files dnsmadeeasy
%_files gehirn
%_files linode
%_files luadns
%_files nsone
%_files ovh
%_files rfc2136
%_files route53
%_files sakuracloud
%if 0%{?fedora}
%_files_doc acme
%_files_doc certbot
%_files_doc certbot-dns-cloudflare
%_files_doc certbot-dns-digitalocean
%_files_doc certbot-dns-dnsimple
%_files_doc certbot-dns-dnsmadeeasy
%_files_doc certbot-dns-gehirn
%_files_doc certbot-dns-google
%_files_doc certbot-dns-linode
%_files_doc certbot-dns-luadns
%_files_doc certbot-dns-nsone
%_files_doc certbot-dns-ovh
%_files_doc certbot-dns-rfc2136
%_files_doc certbot-dns-route53
%_files_doc certbot-dns-sakuracloud
%endif

%changelog
%autochangelog
