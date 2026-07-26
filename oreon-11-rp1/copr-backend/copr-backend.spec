%global source0_hash 3e59d1c09620b1b7e8e54a6bdf28c02d615f11ca2ddc6f096b94b29c0f486f2d

%global prunerepo_version 1.20
%global tests_version 5
%global tests_tar test-data-copr-backend

%global copr_common_version 1.2.1

Name:       copr-backend
Version:    2.11.hotfix
Release:    3%{?dist}
Summary:    Backend for Copr

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %{name}-%{version}.tar.gz
Source1:    https://github.com/fedora-copr/%{tests_tar}/archive/v%{tests_version}/%{tests_tar}-%{tests_version}.tar.gz

BuildArch:  noarch
BuildRequires: asciidoc
BuildRequires: argparse-manpage
BuildRequires: createrepo_c >= 0.16.1
BuildRequires: libappstream-glib-builder
BuildRequires: libxslt
BuildRequires: make
BuildRequires: redis
BuildRequires: rsync
BuildRequires: systemd
BuildRequires: util-linux

BuildRequires: python3-devel

BuildRequires: python3-copr
BuildRequires: python3-copr-common >= %copr_common_version
BuildRequires: python3-daemon
BuildRequires: python3-dateutil
BuildRequires: python3-distro
BuildRequires: python3-gobject
BuildRequires: python3-httpretty
BuildRequires: python3-humanize
BuildRequires: python3-munch
BuildRequires: python3-netaddr
BuildRequires: python3-packaging
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: python3-resalloc
BuildRequires: python3-retask
BuildRequires: python3-setproctitle
BuildRequires: python3-sphinx
BuildRequires: python3-tabulate
BuildRequires: python3-zstandard
BuildRequires: python3-cachetools
BuildRequires: python3-libdnf5
BuildRequires: prunerepo >= %prunerepo_version
BuildRequires: resalloc-server
BuildRequires: dnf

Requires:   (copr-selinux if selinux-policy-targeted)
Requires:   ansible
Suggests:   awscli
Requires:   createrepo_c >= 0.16.1
Requires:   crontabs
Requires:   gawk
Requires:   libappstream-glib-builder
Requires:   lighttpd
Recommends: logrotate
Requires:   mock
Requires:   obs-signd
Requires:   openssh-clients
Requires:   prunerepo >= %prunerepo_version
Requires:   python3-copr
Requires:   python3-copr-common >= %copr_common_version
Recommends: python3-copr-messaging
Requires:   python3-daemon
Requires:   python3-dateutil
Recommends: python3-fedmsg
Requires:   python3-gobject
Requires:   python3-humanize
Requires:   python3-jinja2
Requires:   python3-munch
Requires:   python3-netaddr
Requires:   python3-packaging
Requires:   python3-requests
Requires:   python3-resalloc >= 3.0
Requires:   python3-retask
Requires:   python3-setproctitle
Requires:   python3-tabulate
Requires:   python3-boto3
Requires:   python3-cachetools
Requires:   redis
Requires:   rpm-sign
Requires:   rsync
Requires:   python3-libdnf5
Recommends: util-linux-core
Requires:   zstd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%{?fedora:Requires(pre): lighttpd-filesystem}

%generate_buildrequires
%pyproject_buildrequires

%description
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latest builds.

This package contains backend.

%package doc
Summary:    Code documentation for COPR backend

%description doc
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latests builds.

This package include documentation for COPR code. Mostly useful for developers
only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1

%build
make -C docs %{?_smp_mflags} html
%pyproject_wheel

PYTHONPATH=`pwd` argparse-manpage --pyfile run/copr-backend-resultdir-cleaner \
    --function _get_arg_parser > copr-backend-resultdir-cleaner.1

%install
%pyproject_install

install -d %{buildroot}%{_sharedstatedir}/copr/public_html/results
install -d %{buildroot}%{_pkgdocdir}/lighttpd/
install -d %{buildroot}%{_sysconfdir}/copr
install -d %{buildroot}%{_sysconfdir}/logrotate.d/
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}/%{_var}/log/copr-backend
install -d %{buildroot}/%{_var}/run/copr-backend/
install -d %{buildroot}/%{_tmpfilesdir}
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -d %{buildroot}%{_sysconfdir}/cron.weekly
install -d %{buildroot}%{_sysconfdir}/sudoers.d
install -d %{buildroot}%{_bindir}/

cp -a copr-backend-service %{buildroot}/%{_bindir}/
cp -a run/* %{buildroot}%{_bindir}/
cp -a conf/copr-be.conf.example %{buildroot}%{_sysconfdir}/copr/copr-be.conf

install -p -m 755 conf/crontab/daily %{buildroot}%{_sysconfdir}/cron.daily/copr-backend
install -p -m 755 conf/crontab/weekly  %{buildroot}%{_sysconfdir}/cron.weekly/copr-backend

cp -a conf/lighttpd/* %{buildroot}%{_pkgdocdir}/lighttpd/
cp -a conf/logrotate/* %{buildroot}%{_sysconfdir}/logrotate.d/
cp -a conf/tmpfiles.d/* %{buildroot}/%{_tmpfilesdir}

# for ghost files
touch %{buildroot}%{_var}/log/copr-backend/copr.log
touch %{buildroot}%{_var}/log/copr-backend/prune_old.log

cp -a units/*.{target,service} %{buildroot}/%{_unitdir}/
install -m 0644 conf/copr.sudoers.d %{buildroot}%{_sysconfdir}/sudoers.d/copr

install -d %{buildroot}%{_sysconfdir}/logstash.d

install -d %{buildroot}%{_datadir}/logstash/patterns/
cp -a conf/logstash/lighttpd.pattern %{buildroot}%{_datadir}/logstash/patterns/lighttpd.pattern

install -d %{buildroot}%{_pkgdocdir}/examples/%{_sysconfdir}/logstash.d
cp -a conf/logstash/copr_backend.conf %{buildroot}%{_pkgdocdir}/examples/%{_sysconfdir}/logstash.d/copr_backend.conf

cp -a docs/build/html %{buildroot}%{_pkgdocdir}/

install -d %{buildroot}%{_mandir}/man1
install -p -m 644 copr-backend-resultdir-cleaner.1 %{buildroot}/%{_mandir}/man1/

install -m0644 -D conf/copr-backend.sysusers.conf %{buildroot}%{_sysusersdir}/copr-backend.conf

%check
./run_tests.sh -vv --no-cov

%post
%systemd_post copr-backend.target

%preun
%systemd_preun copr-backend.target

%postun
%systemd_postun_with_restart copr-backend-log.service
%systemd_postun_with_restart copr-backend-build.service
%systemd_postun_with_restart copr-backend-action.service

%files
%license LICENSE
%python3_sitelib/copr_backend
%{python3_sitelib}/copr_backend-*.dist-info/

%dir %{_sharedstatedir}/copr
%dir %attr(0755, copr, copr) %{_sharedstatedir}/copr/public_html/
%dir %attr(0755, copr, copr) %{_sharedstatedir}/copr/public_html/results
%dir %attr(0755, copr, copr) %{_var}/run/copr-backend
%dir %attr(0755, copr, copr) %{_var}/log/copr-backend

%ghost %{_var}/log/copr-backend/*.log

%config(noreplace) %{_sysconfdir}/logrotate.d/copr-backend
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/lighttpd
%dir %{_sysconfdir}/copr
%config(noreplace) %attr(0640, root, copr) %{_sysconfdir}/copr/copr-be.conf
%{_unitdir}/*.service
%{_unitdir}/*.target
%{_tmpfilesdir}/copr-backend.conf
%{_bindir}/*

%config(noreplace) %{_sysconfdir}/cron.daily/copr-backend
%config(noreplace) %{_sysconfdir}/cron.weekly/copr-backend
%{_datadir}/logstash/patterns/lighttpd.pattern

%config(noreplace) %attr(0600, root, root)  %{_sysconfdir}/sudoers.d/copr

%{_mandir}/man1/copr-backend*.1*

%{_sysusersdir}/copr-backend.conf

%files doc
%license LICENSE
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/lighttpd

%changelog
%autochangelog
