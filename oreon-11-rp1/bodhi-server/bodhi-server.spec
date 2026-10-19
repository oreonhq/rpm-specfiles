%global source0_hash 6297adc1ba1d9e30710591490bcced437f6503f1358ad20d53857960d9b9310b
%global pypi_name bodhi-server
%global src_name bodhi_server
%global pypi_version 26.4.0
Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Bodhi server
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source0:        https://files.pythonhosted.org/packages/source/b/bodhi_server/bodhi_server-%{version}.tar.gz
BuildArch:      noarch
Requires: bodhi-client >= 25.11.3
Requires: python3-bodhi-messages >= 8.1.1
Requires: fedora-messaging
Requires: git
Requires: httpd
Requires: intltool
Requires: python3-librepo
Requires: python3-mod_wsgi
%{?sysusers_requires_compat}
Provides:  bundled(chrissimpkins-hack-fonts)
Provides:  bundled(fedora-bootstrap) = 5.3.3-0
Provides:  bundled(fontawesome-fonts-web) = 4.6.3
Provides:  bundled(js-chart) = 3.8.0
Provides:  bundled(js-jquery) = 3.6.0
Provides:  bundled(js-messenger) = 1.4.1
Provides:  bundled(js-moment) = 2.8.3
Provides:  bundled(js-selectize) = 0.15.2
Provides:  bundled(js-typeahead.js) = 1.1.1
Provides:  bundled(open-sans-fonts)
%py_provides python3-bodhi-server
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-bodhi-server = %{version}-%{release}
# /oreon:deps
%description
Bodhi is a modular framework that facilitates the process of publishing
updates for a software distribution.

%package -n bodhi-composer
Summary: Bodhi composer backend
Requires: %{py3_dist jinja2}
Requires: bodhi-server == %{version}-%{release}
Requires: pungi >= 4.1.20
Requires: python3-createrepo_c >= 1.0.0
Requires: skopeo
Requires: python3dist(libdnf5)
%description -n bodhi-composer
The Bodhi composer is the component that publishes Bodhi artifacts to
repositories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{src_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%pyproject_wheel
make %{?_smp_mflags} -C docs man
%install
%pyproject_install
%{__mkdir_p} %{buildroot}/var/lib/bodhi
%{__mkdir_p} %{buildroot}/var/cache/bodhi
%{__mkdir_p} %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bodhi
%{__mkdir_p} %{buildroot}%{_datadir}/bodhi
%{__mkdir_p} -m 0755 %{buildroot}/%{_localstatedir}/log/bodhi
install -m 644 apache/bodhi.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
sed -i -s 's/BODHI_VERSION/%{version}/g' %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
sed -i -s 's/python3.7/python%{python3_version}/g' %{buildroot}%{_sysconfdir}/httpd/conf.d/bodhi.conf
install -m 640 production.ini %{buildroot}%{_sysconfdir}/bodhi/production.ini
install -m 640 alembic.ini %{buildroot}%{_sysconfdir}/bodhi/alembic.ini
install apache/bodhi.wsgi %{buildroot}%{_datadir}/bodhi/bodhi.wsgi
install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/*.1 %{buildroot}%{_mandir}/man1/
install -p -D -m 0644 %{name}.conf %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles bodhi-composer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export BODHI_CONFIG=$(pwd)/tests/testing.ini
%{pytest} -v -k 'not sanity_check and not TestSanityCheckRepodata'
%pre -n %{pypi_name}

%sysusers_create_compat %{name}.conf
%files
%files -n bodhi-composer -f %{oreon_filedir}/bodhi-composer.list

%changelog

%autochangelog
