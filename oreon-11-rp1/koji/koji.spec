%global source0_hash ec41dfa317964b266c40f26db9a5439b765aee95109ba4d16924a5a1c795a35c
%global _python_bytecompile_extra 0
%define __python %{__python3}
%{?!python3_pkgversion:%global python3_pkgversion 3}
Name: koji
Version: 1.36.1
Release:        1%{?dist}
License: LGPL-2.1-only AND GPL-2.0-or-later
Summary:        Build system tools
URL: https://pagure.io/koji/
Source0:        https://forge.fedoraproject.org/koji/koji/releases/download/koji-%{version}/koji-%{version}.tar.bz2
Patch100: fedora-config.patch
BuildArch: noarch
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-libcomps
Requires: python3-libcomps
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
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
%description hub
koji-hub is the XMLRPC interface to the koji database

%package -n python%{python3_pkgversion}-%{name}-hub
Summary: Koji XMLRPC interface
License: LGPL-2.1-only
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
scripts='%{_bindir}/koji %{_sbindir}/kojid %{_sbindir}/kojira %{_sbindir}/koji-shadow
         %{_sbindir}/koji-gc %{_sbindir}/kojivmd %{_sbindir}/koji-sweep-db
         %{_sbindir}/koji-sidetag-cleanup'
for fn in $scripts ; do
    sed -i 's|#!/usr/bin/python2|#!/usr/bin/python3|' $RPM_BUILD_ROOT$fn
done
extra_dirs='
    %{_prefix}/lib/koji-builder-plugins
    %{_prefix}/koji-hub-plugins
    %{_datadir}/koji-hub
    %{_datadir}/koji-web/lib/kojiweb
    %{_datadir}/koji-web/scripts'
for fn in $extra_dirs ; do
    %py_byte_compile %{__python3} %{buildroot}$fn
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post builder

%systemd_post kojid.service
%preun builder

%systemd_preun kojid.service
%postun builder

%systemd_postun kojid.service
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
%files -f %{oreon_filedir}/main.list
%files -n python3-koji -f %{oreon_filedir}/python3-koji.list
%files -n python3-koji-cli-plugins -f %{oreon_filedir}/python3-koji-cli-plugins.list
%files -n koji-hub -f %{oreon_filedir}/koji-hub.list
%files -n python3-koji-hub -f %{oreon_filedir}/python3-koji-hub.list
%files -n koji-hub-plugins -f %{oreon_filedir}/koji-hub-plugins.list
%files -n python3-koji-hub-plugins -f %{oreon_filedir}/python3-koji-hub-plugins.list
%files -n koji-builder-plugins -f %{oreon_filedir}/koji-builder-plugins.list
%files -n koji-builder -f %{oreon_filedir}/koji-builder.list
%files -n koji-vm -f %{oreon_filedir}/koji-vm.list
%files -n koji-utils -f %{oreon_filedir}/koji-utils.list
%files -n koji-web -f %{oreon_filedir}/koji-web.list
%files -n python3-koji-web -f %{oreon_filedir}/python3-koji-web.list

%changelog

%autochangelog
