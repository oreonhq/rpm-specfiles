%global source0_hash f2fa96bb5bf934156b329d03f5df9cef2376c2121b73c6ed9fc0fa0d4bbb4b36
%global version 1.1.1
%global min_required_version_django 3.2
%global psycopg_pkg python3-psycopg3
Name:           osh
Version:        %{version}
Release:        1%{?dist}
License:        GPL-3.0-or-later
Summary:        Static and Dynamic Analysis as a Service
URL:            https://github.com/openscanhub/openscanhub/
Source0:        https://github.com/openscanhub/openscanhub/archive/refs/tags/%{name}-%{version}.tar.gz
BuildArch:      noarch
%{!?bash_completions_dir: %global bash_completions_dir %{_datadir}/bash-completion/completions}
%{!?zsh_completions_dir: %global zsh_completions_dir %{_datadir}/zsh/site-functions}
# oreon:deps
BuildRequires:  koji
BuildRequires:  python3-csdiff
BuildRequires:  python3-devel
BuildRequires:  python3-kobo-client
BuildRequires:  python3-kobo-django
BuildRequires:  python3-kobo-hub
BuildRequires:  python3-kobo-rpmlib
BuildRequires:  python3-psycopg3
BuildRequires:  python3-qpid-proton
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3dist(django)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
OpenScanHub is a service for static and dynamic analysis of RPM packages.
It consists of central hub, workers and cli client.

%package client
Summary: OpenScanHub CLI client
Requires: koji
Requires: python3-kobo-client >= 0.15.1-100
Requires: %{name}-common = %{version}-%{release}
Provides: osh-cli = %{version}-%{release}
Provides: covscan-client = %{version}
Obsoletes: covscan-client < %{version}
%description client
OpenScanHub CLI client.
It is used to submit, query and download scans.

%package common
Summary: OpenScanHub shared files for client, hub and worker
Obsoletes: covscan-common < %{version}
%description common
OpenScanHub shared files for client, hub and worker.

%package worker
Summary: OpenScanHub worker
Requires: csmock
Requires: file
Requires: koji
Requires: python3-kobo-client
Requires: python3-kobo-rpmlib
Requires: python3-kobo-worker >= 0.36.1
Requires: %{name}-common = %{version}-%{release}
Recommends: osh-worker-conf
Obsoletes: covscan-worker < %{version}
%description worker
OpenScanHub worker.
It is used to process tasks submitted to the hub.

%package hub
Summary: OpenScanHub xml-rpc interface and web application
Requires: httpd
Requires: mod_auth_gssapi
Requires: mod_ssl
Requires: python3dist(django) >= %{min_required_version_django}
Requires: python3-kobo-client
Requires: python3-kobo-django >= 0.35.0
Requires: python3-kobo-hub >= 0.35.0
Requires: python3-kobo-rpmlib
Requires: python3-mod_wsgi
Requires: %{psycopg_pkg}
Requires: gzip
Requires: python3-qpid-proton
Requires: koji
Requires: xz
Requires: csdiff
Requires: python3-bugzilla
Requires: python3-csdiff
Requires: python3-jira
%if 0%{?fedora} < 40 && 0%{?rhel} < 10 && 0%{?oreon} < 11
Requires(post): postgresql < 16
%else
Requires(post): postgresql
%endif
Requires: %{name}-common = %{version}-%{release}
Recommends: osh-hub-conf
Obsoletes: covscan-hub < %{version}
%description hub
OpenScanHub xml-rpc interface and web application.

%package worker-manager
Summary: OpenScanHub worker manager
Requires: %{name}-hub = %{version}-%{release}
Requires: openssh-clients
%description worker-manager
OpenScanHub worker manager to dynamically create and destroy workers.

%package hub-conf-devel
Summary: OpenScanHub hub devel configuration
Provides: osh-hub-conf = %{version}-%{release}
Conflicts: osh-hub-conf
Requires: httpd-filesystem
Requires: osh-hub
%description hub-conf-devel
OpenScanHub hub devel configurations.

%package worker-conf-devel
Summary: OpenScanHub worker devel configuration
Provides: osh-worker-conf = %{version}-%{release}
Conflicts: osh-worker-conf
%description worker-conf-devel
OpenScanHub worker devel configurations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir openscanhub-%{name}-%{version}
%oreon_prep
%build

%py3_shebang_fix osh/client/osh-cli
PYTHONPATH=. osh/hub/manage.py collectstatic --noinput
sed 's|@PYTHON3_SITELIB@|%{python3_sitelib}|' osh/hub/osh-hub-httpd.conf.in > osh/hub/osh-hub-httpd.conf
%py3_build
%install
%py3_install
cp -a {,%{buildroot}%{python3_sitelib}/}osh/hub/static/
ln -s osh-cli %{buildroot}%{_bindir}/covscan
%if "%{_bindir}" != "%{_sbindir}"
mkdir -p %{buildroot}%{_sbindir}
ln -s ../bin/osh-worker %{buildroot}%{_sbindir}/osh-worker
%endif
mkdir -p %{buildroot}%{_sysconfdir}/osh/hub/secrets
mkdir -p %{buildroot}%{_sysconfdir}/osh/worker-manager
mkdir -p %{buildroot}%{_sharedstatedir}/osh/hub/{tasks,upload,worker}
mkdir -p %{buildroot}%{_localstatedir}/log/osh/hub
touch %{buildroot}%{_localstatedir}/log/osh/hub/hub.log
cp -a osh/hub/scripts/checker_groups.txt %{buildroot}%{python3_sitelib}/osh/hub/scripts/
chmod 0755 %{buildroot}%{python3_sitelib}/osh/hub/manage.py
rm -rf %{buildroot}%{python3_sitelib}/scripts
install -D {osh/hub,%{buildroot}%{_sysconfdir}/httpd/conf.d}/osh-hub-httpd.conf
mv %{buildroot}%{python3_sitelib}/osh/hub/settings_local.py %{buildroot}%{_sysconfdir}/osh/hub
ln -s %{_sysconfdir}/osh/hub/settings_local.py %{buildroot}%{python3_sitelib}/osh/hub/settings_local.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post client

if test -f %{_sysconfdir}/covscan/covscan.conf; then
    mv %{_sysconfdir}/covscan/covscan.conf %{_sysconfdir}/osh/client.conf
fi
%post worker

%systemd_post osh-worker.service
%preun worker

%systemd_preun osh-worker.service
%postun worker

if [ $1 -ge 1 ]; then
    systemctl reload osh-worker.service || :
fi
%post hub

exec &>> %{_localstatedir}/log/osh/hub/post-install-%{name}-%{version}-%{release}.log
echo -n '>>> '
date -R
set -x
umask 0026
if ! test -e %{_sharedstatedir}/osh/hub/secret_key; then
    %{__python3} -c "from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())" > %{_sharedstatedir}/osh/hub/secret_key
    chgrp apache %{_sharedstatedir}/osh/hub/secret_key
fi
if pg_isready -h localhost; then
    runuser -u apache -- %{python3_sitelib}/osh/hub/manage.py migrate
fi
%systemd_post osh-{retention,stats}.{service,timer}
%preun hub

%systemd_preun osh-{retention,stats}.{service,timer}
%postun hub

%systemd_postun osh-{retention,stats}.{service,timer}
%files -f %{oreon_filedir}/main.list
%files -n osh-client -f %{oreon_filedir}/osh-client.list
%files -n osh-common -f %{oreon_filedir}/osh-common.list
%files -n osh-worker -f %{oreon_filedir}/osh-worker.list
%files -n osh-hub -f %{oreon_filedir}/osh-hub.list
%files -n osh-worker-manager -f %{oreon_filedir}/osh-worker-manager.list
%files -n osh-hub-conf-devel -f %{oreon_filedir}/osh-hub-conf-devel.list
%files -n osh-worker-conf-devel -f %{oreon_filedir}/osh-worker-conf-devel.list

%changelog

%autochangelog
