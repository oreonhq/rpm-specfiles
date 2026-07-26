%global source0_hash e29a1f435be9bfbc639933f9e20247a2ff3d84d48415a0ce2478a2028bc04f85

%global copr_common_version 0.25.1~~dev0

Name:       copr-dist-git
Version:    1.3
Release:    4%{?dist}
Summary:    Copr services for Dist Git server

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch

BuildRequires: systemd
BuildRequires: python3-devel
BuildRequires: python3-munch
BuildRequires: python3-requests
BuildRequires: python3-rpkg >= 1.67-1
BuildRequires: python3-pytest
BuildRequires: python3-copr-common >= %copr_common_version
BuildRequires: python3-redis
BuildRequires: python3-setproctitle

Recommends: logrotate
Requires: systemd
Requires: httpd
Requires: coreutils
Requires: /usr/bin/crudini
# last bump for the remove_unused_sources script
Requires: dist-git >= 1.12
Requires: python3-copr-common >= %copr_common_version
Requires: python3-requests
Requires: python3-rpkg >= 1.67-4
Requires: python3-munch
Requires: python3-setproctitle
Requires: python3-daemon
Requires: python3-redis
Requires: findutils
Requires: (copr-selinux if selinux-policy-targeted)
Requires: crontabs
Requires: redis

Recommends: python3-copr

%{?fedora:Requires(post): policycoreutils-python-utils}
%{?rhel:Requires(post): policycoreutils-python}
%{?fedora:Requires(pre): group(apache)}

%description
COPR is lightweight build system. It allows you to create new project in WebUI
and submit new builds and COPR will create yum repository from latest builds.

This package contains Copr services for Dist Git server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

install -d %{buildroot}%{_datadir}/copr/dist_git
install -d %{buildroot}%{_sysconfdir}/copr
install -d %{buildroot}%{_sysconfdir}/logrotate.d/
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_var}/log/copr-dist-git
install -d %{buildroot}%{_tmpfilesdir}
install -d %{buildroot}%{_sharedstatedir}/copr-dist-git
install -d %{buildroot}%{_sysconfdir}/cron.monthly

install -p -m 755 conf/cron.monthly/copr-dist-git %{buildroot}%{_sysconfdir}/cron.monthly/copr-dist-git

cp -a conf/copr-dist-git.conf.example %{buildroot}%{_sysconfdir}/copr/copr-dist-git.conf
cp -a conf/httpd/copr-dist-git.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/copr-dist-git.conf
cp -a conf/tmpfiles.d/* %{buildroot}/%{_tmpfilesdir}
cp -a copr-dist-git.service %{buildroot}%{_unitdir}/

cp -a conf/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/copr-dist-git

# for ghost files
touch %{buildroot}%{_var}/log/copr-dist-git/main.log

install -m0644 -D conf/copr-dist-git.sysusers.conf %{buildroot}%{_sysusersdir}/copr-dist-git.conf

%check
./run_tests.sh -vv --no-cov

%post
%systemd_post copr-dist-git.service

%preun
%systemd_preun copr-dist-git.service

%postun
%systemd_postun_with_restart copr-dist-git.service

%files
%license LICENSE
%{python3_sitelib}/copr_dist_git
%{python3_sitelib}/copr_dist_git-*.dist-info/

%{_bindir}/*
%dir %{_datadir}/copr
%{_datadir}/copr/*
%dir %{_sysconfdir}/copr
%config(noreplace) %attr(0640, root, copr-dist-git) %{_sysconfdir}/copr/copr-dist-git.conf
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/httpd/conf.d/copr-dist-git.conf
%config(noreplace) %attr(0755, root, root) %{_sysconfdir}/cron.monthly/copr-dist-git

%dir %attr(0755, copr-dist-git, copr-dist-git) %{_sharedstatedir}/copr-dist-git/

%{_unitdir}/copr-dist-git.service

%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/copr-dist-git
%dir %attr(0755, copr-dist-git, copr-dist-git) %{_var}/log/copr-dist-git
%ghost %attr(0644, copr-dist-git, copr-dist-git) %{_var}/log/copr-dist-git/main.log
%{_tmpfilesdir}/copr-dist-git.conf
%{_sysusersdir}/copr-dist-git.conf

%changelog
%autochangelog
