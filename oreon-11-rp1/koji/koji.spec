%global source0_hash eb5c2f6bfd8ac0f173ba9170272b00201c73b4082734350430d6edf68fb15f22

# This package depends on selective manual byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 0

%define __python %{__python3}

# If the definition isn't available for python3_pkgversion, define it
%{?!python3_pkgversion:%global python3_pkgversion 3}

Name: koji
Version: 1.35.3
Release: 9%{?dist}
# the included arch lib from yum's rpmUtils is GPLv2+
License: LGPL-2.1-only AND GPL-2.0-or-later
Summary: Build system tools
URL: https://pagure.io/koji/
Source0: https://releases.pagure.org/koji/koji-%{version}.tar.bz2

# https://pagure.io/koji/pull-request/4342
# download-build: allow fallback to unsigned with --key
Patch0: 0001-download-build-allow-fallback-to-unsigned-with-key.patch
Patch1: 0002-Fix-flake8-and-unit-test.patch

# Not upstreamable
Patch100: fedora-config.patch

BuildArch: noarch
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-libcomps
Requires: python3-libcomps
BuildRequires: systemd
BuildRequires: pkgconfig
BuildRequires: sed

%description
Koji is a system for building and tracking RPMS.  The base package
contains shared libraries and the command-line interface.

%package -n python%{python3_pkgversion}-%{name}
Summary: Build system tools python library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: make
BuildRequires: python3-pip
BuildRequires: python3-wheel
Requires: python%{python3_pkgversion}-rpm
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-requests-gssapi
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-defusedxml

%description -n python%{python3_pkgversion}-%{name}
Koji is a system for building and tracking RPMS.
This subpackage provides python functions and libraries.

%package -n python%{python3_pkgversion}-%{name}-cli-plugins
Summary: Koji client plugins
License: LGPL-2.1-only
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-cli-plugins
Plugins to the koji command-line interface

%package hub
Summary: Koji XMLRPC interface
License: LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
Requires: %{name}-hub-code
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-hub
Suggests: python%{python3_pkgversion}-%{name}-hub-plugins
%endif

%description hub
koji-hub is the XMLRPC interface to the koji database

%package -n python%{python3_pkgversion}-%{name}-hub
Summary: Koji XMLRPC interface
License: LGPL-2.1-only
# rpmdiff lib (from rpmlint) is GPLv2 (only)
Requires: httpd
Requires: python%{python3_pkgversion}-mod_wsgi
Requires: mod_auth_gssapi
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Provides: %{name}-hub-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-hub
koji-hub is the XMLRPC interface to the koji database

%package hub-plugins
Summary: Koji hub plugins
License: LGPL-2.1-only
Requires: %{name}-hub-plugins-code = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-hub-plugins
%endif

%description hub-plugins
Plugins to the koji XMLRPC interface

%package -n python%{python3_pkgversion}-%{name}-hub-plugins
Summary: Koji hub plugins
License: LGPL-2.1-only
Requires: python%{python3_pkgversion}-%{name}-hub = %{version}-%{release}
Requires: python%{python3_pkgversion}-qpid-proton
Requires: cpio
Provides: %{name}-hub-plugins-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-hub-plugins
Plugins to the koji XMLRPC interface

%package builder-plugins
Summary: Koji builder plugins
License: LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
Requires: %{name}-builder = %{version}-%{release}

%description builder-plugins
Plugins for the koji build daemon

%package builder
Summary: Koji RPM builder daemon
License: LGPL-2.1-only
Requires: mock >= 0.9.14
Requires: squashfs-tools
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: /usr/bin/svn
Requires: /usr/bin/git
Requires: createrepo_c >= 0.10.0
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-librepo
Requires: python%{python3_pkgversion}-multilib
Requires: python%{python3_pkgversion}-cheetah
Requires: python%{python3_pkgversion}-pycdio

%description builder
koji-builder is the daemon that runs on build machines and executes
tasks that come through the Koji system.

%package vm
Summary: Koji virtual machine management daemon
License: LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: python%{python3_pkgversion}-libvirt
Requires: python%{python3_pkgversion}-libxml2
Requires: /usr/bin/virt-clone
Requires: qemu-img

%description vm
koji-vm contains a supplemental build daemon that executes certain tasks in a
virtual machine. This package is not required for most installations.

%package utils
Summary: Koji Utilities
License: LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-psycopg2
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description utils
Utilities for the Koji system

%package web
Summary: Koji Web UI
License: LGPL-2.1-only
Requires: %{name} = %{version}-%{release}
Requires: %{name}-web-code = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-web
%endif

%description web
koji-web is a web UI to the Koji system.

%package -n python%{python3_pkgversion}-%{name}-web
Summary: Koji Web UI
License: LGPL-2.1-only
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-web}
Requires: httpd
Requires: python%{python3_pkgversion}-mod_wsgi
Requires: mod_auth_gssapi
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-cheetah
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Provides: %{name}-web-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-web
koji-web is a web UI to the Koji system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# we'll be packaging these separately and don't want them registered
# to the wheel we will produce.
sed -e '/util\/koji/g' -e '/koji_cli_plugins/g' -i setup.py

%if 0%{?fedora} > 42 || 0%{?rhel} >= 10
# Create a sysusers.d config file
cat >koji.sysusers.conf <<EOF
u kojibuilder - - /builddir /bin/bash
m kojibuilder mock
EOF
%endif

%build
%py3_build_wheel

%install
%define make_with_dirs make DESTDIR=$RPM_BUILD_ROOT SBINDIR=%{_sbindir}

%py3_install_wheel %{name}-%{version}-py3-none-any.whl
mkdir -p %{buildroot}/etc/koji.conf.d
cp cli/koji.conf %{buildroot}/etc/koji.conf
for D in kojihub builder plugins util www vm schemas ; do
    pushd $D
    %{make_with_dirs} PYTHON=%{__python3} install
    popd
done

# alter python interpreter in koji CLI
scripts='%{_bindir}/koji %{_sbindir}/kojid %{_sbindir}/kojira %{_sbindir}/koji-shadow
         %{_sbindir}/koji-gc %{_sbindir}/kojivmd %{_sbindir}/koji-sweep-db
         %{_sbindir}/koji-sidetag-cleanup'
for fn in $scripts ; do
    sed -i 's|#!/usr/bin/python2|#!/usr/bin/python3|' $RPM_BUILD_ROOT$fn
done

# handle extra byte compilation
extra_dirs='
    %{_prefix}/lib/koji-builder-plugins
    %{_prefix}/koji-hub-plugins
    %{_datadir}/koji-hub
    %{_datadir}/koji-web/lib/kojiweb
    %{_datadir}/koji-web/scripts'
for fn in $extra_dirs ; do
    %py_byte_compile %{__python3} %{buildroot}$fn
done

%if 0%{?fedora} > 42 || 0%{?rhel} >= 10
install -m0644 -D koji.sysusers.conf %{buildroot}%{_sysusersdir}/koji.conf
%endif

%files
%{_bindir}/koji
%{_datadir}/koji
%config(noreplace) /etc/koji.conf
%dir /etc/koji.conf.d
%doc docs Authors COPYING LGPL

%files -n python%{python3_pkgversion}-koji
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.*-info
%{python3_sitelib}/koji_cli

%files -n python%{python3_pkgversion}-%{name}-cli-plugins
%{python3_sitelib}/koji_cli_plugins
# we don't have config files for default plugins yet
#%%dir %%{_sysconfdir}/koji/plugins
#%%config(noreplace) %%{_sysconfdir}/koji/plugins/*.conf

%files hub
%config(noreplace) /etc/httpd/conf.d/kojihub.conf
%dir /etc/koji-hub
%config(noreplace) /etc/koji-hub/hub.conf
%dir /etc/koji-hub/hub.conf.d
%{_sbindir}/koji-sweep-db
%{_unitdir}/koji-sweep-db.service
%{_unitdir}/koji-sweep-db.timer

%files -n python%{python3_pkgversion}-%{name}-hub
%{_datadir}/koji-hub/*.py
%{_datadir}/koji-hub/__pycache__
%{python3_sitelib}/kojihub

%files hub-plugins
%dir /etc/koji-hub/plugins
%config(noreplace) /etc/koji-hub/plugins/*.conf

%files -n python%{python3_pkgversion}-%{name}-hub-plugins
%{_prefix}/lib/koji-hub-plugins/*.py
%{_prefix}/lib/koji-hub-plugins/__pycache__

%files builder-plugins
%dir /etc/kojid/plugins
%config(noreplace) /etc/kojid/plugins/*.conf
%dir %{_prefix}/lib/koji-builder-plugins
%{_prefix}/lib/koji-builder-plugins/*.py*
%{_prefix}/lib/koji-builder-plugins/__pycache__

%files utils
%{_sbindir}/kojira
%{_unitdir}/koji-gc.service
%{_unitdir}/koji-gc.timer
%{_unitdir}/kojira.service
%dir /etc/kojira
%config(noreplace) /etc/kojira/kojira.conf
%{_sbindir}/koji-gc
%dir /etc/koji-gc
%config(noreplace) /etc/koji-gc/koji-gc.conf
%config(noreplace) /etc/koji-gc/email.tpl
%{_sbindir}/koji-shadow
%dir /etc/koji-shadow
%{_sbindir}/koji-sidetag-cleanup
%config(noreplace) /etc/koji-shadow/koji-shadow.conf

%files web
%dir /etc/kojiweb
%config(noreplace) /etc/kojiweb/web.conf
%config(noreplace) /etc/httpd/conf.d/kojiweb.conf
%dir /etc/kojiweb/web.conf.d

%files -n python%{python3_pkgversion}-%{name}-web
%{_datadir}/koji-web

%files builder
%{_sbindir}/kojid
%{_unitdir}/kojid.service
%dir /etc/kojid
%config(noreplace) /etc/kojid/kojid.conf
%attr(-,kojibuilder,kojibuilder) /etc/mock/koji
%if 0%{?fedora} > 42 || 0%{?rhel} >= 10
%{_sysusersdir}/koji.conf
%endif

%post builder
%systemd_post kojid.service

%preun builder
%systemd_preun kojid.service

%postun builder
%systemd_postun kojid.service

%files vm
%{_sbindir}/kojivmd
#dir %%{_datadir}/kojivmd
%{_datadir}/kojivmd/kojikamid
%{_unitdir}/kojivmd.service
%dir /etc/kojivmd
%config(noreplace) /etc/kojivmd/kojivmd.conf

%post vm
%systemd_post kojivmd.service

%preun vm
%systemd_preun kojivmd.service

%postun vm
%systemd_postun kojivmd.service

%post utils
%systemd_post kojira.service

%preun utils
%systemd_preun kojira.service

%postun utils
%systemd_postun kojira.service

%changelog
%autochangelog
