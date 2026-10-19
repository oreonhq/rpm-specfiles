%global source0_hash 84eed9f149b6dd9f43174b4c2cfaf93105a74b58b0eadc82946b65edfde8045b
%global oldpkg letsencrypt
%bcond_with docs
%bcond_without tests
%global         SPHINXBUILD sphinx-build-3
%global MODULES %{expand:certbot-dns-cloudflare certbot-dns-digitalocean certbot-dns-dnsimple certbot-dns-dnsmadeeasy certbot-dns-gehirn certbot-dns-linode certbot-dns-luadns certbot-dns-nsone certbot-dns-ovh certbot-dns-rfc2136 certbot-dns-route53 certbot-dns-sakuracloud}
Name:           certbot
Version:        5.8.0
Release:        1%{?dist}
Summary:        A free, automated certificate authority client
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       certbot-renew-systemd.service
Source11:       certbot-renew-systemd.timer
Source12:       certbot-sysconfig-certbot
Source13:       certbot-cli.ini
Source14:       certbot-README.fedora
Source15:       certbot.logrotate
Patch1:         certbot-disable-test_lock_order-renew.patch
BuildArch:      noarch
%{?systemd_requires}
Requires(post): %{_sbindir}/restorecon
Requires: python3-certbot = %{version}-%{release}
Obsoletes: %{oldpkg} < 0.6.0
Provides: %{oldpkg} = %{version}-%{release}
%define _description() \%description -n %1\
\%{summary}
%define _package() \%package -n %1\
Summary:        A free, automated certificate authority client
\%if 0\%{?fedora}\
Provides:      %2 = \%{version}-\%{release}\
Requires:      python3-acme = \%{version}-\%{release}\
Requires:      python3-certbot = \%{version}-\%{release}\
\%endif
%define _package_doc() \%package -n %1\
Summary:        A free, automated certificate authority client
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
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-certbot = %{version}-%{release}
# /oreon:deps
%package -n       python3-certbot+docs
Summary:        Metapackage for python3-certbot docs extras
Requires:       python3-certbot = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.0
Provides:       python3dist(certbot[docs]) = %{version}-%{release}

%description -n python3-certbot+docs
Metapackage for python3-certbot docs extras.

%package -n       python3-certbot+test
Summary:        Metapackage for python3-certbot test extras
Requires:       python3-certbot = %{version}-%{release}
Provides:       python3dist(certbot[test]) = %{version}-%{release}

%description -n python3-certbot+test
Metapackage for python3-certbot test extras.

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python3-certbot
Summary:    Python 3 libraries used by certbot
Requires:   python3-acme
# oreon:reqs
Requires:       python3dist(cryptography) >= 47.0.0
Requires:       python3dist(josepy) >= 2.0.0
Requires:       python3dist(pyopenssl) >= 25.0.0
Requires:       python3dist(requests) >= 2.25.1
# /oreon:reqs
%package -n python3-acme
Summary:    Python library for the ACME protocol
%package -n python3-certbot-apache
Summary:    The apache plugin for certbot
Requires:   mod_ssl
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
%package -n python3-certbot-nginx
Summary:     The nginx plugin for certbot
Requires: python3-acme = %{version}-%{release}
Requires: python3-certbot = %{version}-%{release}
Recommends:    certbot >= %{version}
%_package python3-certbot-dns-cloudflare certbot-dns-cloudflare
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build

for module in acme certbot %{MODULES} certbot-apache certbot-nginx
do
  cd $module
    %pyproject_wheel
  cd ..
done
%install
%pyproject_install
mv %{buildroot}%{_bindir}/certbot{,-3}
ln -s certbot %{buildroot}/usr/bin/%{oldpkg}
ln -s certbot-3 %{buildroot}%{_bindir}/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE10} %{buildroot}%{_unitdir}/certbot-renew.service
install -Dm 0644 --preserve-timestamps %{SOURCE11} %{buildroot}%{_unitdir}/certbot-renew.timer
install -Dm 0644 --preserve-timestamps %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/certbot
install -Dm 0644 --preserve-timestamps %{SOURCE13} %{buildroot}%{_sysconfdir}/letsencrypt/cli.ini
install -Dm 0644 --preserve-timestamps %{SOURCE15} %{buildroot}%{_sysconfdir}/logrotate.d/certbot
cp -a %{SOURCE14} %{_builddir}/%{name}-%{version}/README.fedora
install -dm 0755 %{buildroot}%{_sysconfdir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_sharedstatedir}/%{oldpkg}
install -dm 0755 %{buildroot}%{_localstatedir}/log/letsencrypt
%oreon_autofiles python3-certbot usr/lib/python3*/site-packages/certbot* usr/lib64/python3*/site-packages/certbot* usr/bin/*
%oreon_autofiles python3-acme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-certbot-apache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-certbot-nginx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/certbot* usr/lib64/python3*/site-packages/certbot* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

for module in acme certbot %{MODULES} certbot-apache certbot-nginx; do
pushd $module
%pytest -v -W ignore::DeprecationWarning
popd
done
%endif
%post

restorecon -R %{_sysconfdir}/letsencrypt || :
%systemd_post certbot-renew.timer
if [ "$1" -eq 1 ] ; then
  echo ""
  echo "Certbot auto renewal timer is not started by default."
  echo "Run 'systemctl start certbot-renew.timer' to enable automatic renewals."
fi
%preun

%systemd_preun certbot-renew.timer
%postun

%systemd_postun certbot-renew.timer
%files
%files -n python3-certbot -f %{oreon_filedir}/python3-certbot.list
%files -n python3-acme -f %{oreon_filedir}/python3-acme.list
%files -n python3-certbot-apache -f %{oreon_filedir}/python3-certbot-apache.list
%files -n python3-certbot-nginx -f %{oreon_filedir}/python3-certbot-nginx.list
%files -n python3-certbot-dns-cloudflare -f %{oreon_filedir}/python3-certbot-dns-cloudflare.list
%files -n python3-certbot-dns-digitalocean -f %{oreon_filedir}/python3-certbot-dns-digitalocean.list
%files -n python3-certbot-dns-dnsimple -f %{oreon_filedir}/python3-certbot-dns-dnsimple.list
%files -n python3-certbot-dns-dnsmadeeasy -f %{oreon_filedir}/python3-certbot-dns-dnsmadeeasy.list
%files -n python3-certbot-dns-gehirn -f %{oreon_filedir}/python3-certbot-dns-gehirn.list
%files -n python3-certbot-dns-linode -f %{oreon_filedir}/python3-certbot-dns-linode.list
%files -n python3-certbot-dns-luadns -f %{oreon_filedir}/python3-certbot-dns-luadns.list
%files -n python3-certbot-dns-nsone -f %{oreon_filedir}/python3-certbot-dns-nsone.list
%files -n python3-certbot-dns-ovh -f %{oreon_filedir}/python3-certbot-dns-ovh.list
%files -n python3-certbot-dns-rfc2136 -f %{oreon_filedir}/python3-certbot-dns-rfc2136.list
%files -n python3-certbot-dns-route53 -f %{oreon_filedir}/python3-certbot-dns-route53.list
%files -n python3-certbot-dns-sakuracloud -f %{oreon_filedir}/python3-certbot-dns-sakuracloud.list

%changelog

%autochangelog
