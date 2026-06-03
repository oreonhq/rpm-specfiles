%global source0_hash ce98ad889b47dd8e57ca934f7f56210065596ef11a6973f872a6ec4efd44fcce

# For optional building of ostree-plugin sub package. Unrelated to systemd
# but the same versions apply at the moment.
%global has_ostree 0%{?suse_version} == 0
%global use_inotify 1

# Plugin for container (docker, podman) is not supported on RHEL
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global use_container_plugin 0
%else
%global use_container_plugin 1
%endif

%global dmidecode_arches %{ix86} x86_64 aarch64

%global completion_dir %{_datadir}/bash-completion/completions

%global run_dir /run

%global rhsm_plugins_dir  /usr/share/rhsm-plugins

%if 0%{?suse_version}
%global use_container_plugin 0
%global use_inotify 0
%endif

%global use_dnf (0%{?fedora} || (0%{?rhel}))
%global create_libdnf_rpm (0%{?fedora} || 0%{?rhel} > 8)

%global python_sitearch %python3_sitearch
%global python_sitelib %python3_sitelib
%global __python %__python3
%if 0%{?suse_version}
%global py_package_prefix python3
%else
%global py_package_prefix python%{python3_pkgversion}
%endif
%global rhsm_package_name %{py_package_prefix}-subscription-manager-rhsm

%global _hardened_build 1
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro -Wl,-z,now}

%if %{has_ostree}
%global install_ostree INSTALL_OSTREE_PLUGIN=true
%else
%global install_ostree INSTALL_OSTREE_PLUGIN=false
%endif

%if %{use_container_plugin}
%global install_container INSTALL_CONTAINER_PLUGIN=true
%else
%global install_container INSTALL_CONTAINER_PLUGIN=false
%endif

%if 0%{?suse_version}
%global install_zypper_plugins INSTALL_ZYPPER_PLUGINS=true
%else
%global install_zypper_plugins INSTALL_ZYPPER_PLUGINS=false
%endif

# makefile defaults to INSTALL_DNF_PLUGINS=false
%if %{use_dnf}
%global install_dnf_plugins INSTALL_DNF_PLUGINS=true
%else
%global install_dnf_plugins INSTALL_DNF_PLUGINS=false
%endif

# Build a list of python package to exclude from the build.
# This is necessary because we have multiple rpms which may or may not
# need to be built depending on the distro which are all in one source tree.
# Because the contents of these optional rpms is often a python package in the
# same source tree, if we choose not to build that package and don't tell
# setup.py to exclude those packages, we end up with files that get installed
# in the buildroot which are not packaged. This fails various
# rpm build / verify post steps, which in certain build systems causes the
# entire build to be considered a failure.
# The implementation of building a list iteratively in a spec file looks a bit
# weird. As we want the final value of the global named "exclude_packages" to
# be an environment variable definition it needs to begin with the following
# (less the single quotes): 'EXCLUDE_PACKAGES="'
# After that we can then make all of our checks to see whether certain items
# should be added to the comma separated list or not.
# In setup.py we are parsing the value of the env var as a string separated
# by commas ignoring empty values. That makes the comma at the end of
# each conditional addition to the list still valid.
%global exclude_packages EXCLUDE_PACKAGES="

# add new exclude packages items after me

%if !%{use_container_plugin}
%global exclude_packages %{exclude_packages}*.plugin.container,
%endif

# add new exclude_packages items before me

%global exclude_packages %{exclude_packages}"

Name: subscription-manager
Version: 1.30.5
Release: 6%{?dist}
Summary: Tools and libraries for subscription and repository management
%if 0%{?suse_version}
Group:   Productivity/Networking/System
License: GPL-2.0
%else
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
%endif
URL:     http://www.candlepinproject.org/

# How to create the source tarball:
#
# git clone https://github.com/candlepin/subscription-manager.git
# yum install tito
# tito build --tag subscription-manager-$VERSION-$RELEASE --tgz
Source0:        https://github.com/candlepin/subscription-manager/archive/%{version}/%{name}-%{version}.tar.gz

# Especially for the OpenSuse Build Service we need to have another lint config
%if 0%{?suse_version}
Source2: subscription-manager-rpmlintrc
%endif

# The following macro examples are preceeded by '%' to stop macro expansion
# in the comments. (See https://bugzilla.redhat.com/show_bug.cgi?id=1224660 for
# why this is necessary)
# A note about the %%{?foo:bar} %%{!?foo:quux} convention.  The %%{?foo:bar}
# syntax evaluates foo and if it is **defined**, it expands to "bar" otherwise it
# expands to nothing.  The %%{!?foo:quux} syntax similarily only the expansion
# occurs when foo is **undefined**.  Since one and only one of the expressions will
# expand we can more concisely handle when a dependency has different names in
# SUSE versus RHEL.  The traditional if syntax gets extremely confusing when
# nesting is required since RPM requires the various preamble directives to be
# at the start of a line making meaningful indentation impossible.

Requires:  iproute
Requires:  %{py_package_prefix}-iniparse
Requires:  %{py_package_prefix}-decorator
Requires:  virt-what
Requires:  %{rhsm_package_name} = %{version}
Requires: subscription-manager-rhsm-certificates
%ifarch %{dmidecode_arches}
Requires: dmidecode
%endif

%if 0%{?suse_version}
Requires: %{py_package_prefix}-python-dateutil
Requires: %{py_package_prefix}-dbus-python
Requires: logrotate
Requires: cron
Requires: %{py_package_prefix}-gobject2
Requires: libzypp
Requires: %{py_package_prefix}-zypp-plugin
%else
Requires: %{py_package_prefix}-dateutil
Requires: %{py_package_prefix}-dbus
Requires: python3-gobject-base
%endif

# rhel 8 has different naming for setuptools going forward
# on newer rhels and Fedora setuptools is not needed on runtime at all
%if (0%{?rhel} && 0%{?rhel} == 8) || (0%{?oreon} >= 11)
Requires:  platform-python-setuptools
%endif

%if %{use_dnf}
%if %{create_libdnf_rpm}
Requires: python3-dnf
Requires: python3-dnf-plugins-core
Requires: python3-librepo
%else
Requires: dnf-plugin-subscription-manager = %{version}
%endif
%endif

%if %use_inotify
Requires:  %{py_package_prefix}-inotify
%endif

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires: python3-cloud-what = %{version}-%{release}

BuildRequires: %{py_package_prefix}-devel
BuildRequires: openssl-devel
BuildRequires: gcc
BuildRequires: %{py_package_prefix}-setuptools
BuildRequires: gettext
BuildRequires: glib2-devel

%if 0%{?suse_version}
BuildRequires: distribution-release
BuildRequires: libzypp
BuildRequires: systemd-rpm-macros
BuildRequires: python3-rpm-macros
BuildRequires: %{py_package_prefix}-python-dateutil
%else
BuildRequires: system-release
BuildRequires: %{py_package_prefix}-dateutil
%endif

BuildRequires: systemd

Obsoletes: subscription-manager-migration <= %{version}-%{release}

Obsoletes: subscription-manager-initial-setup-addon <= %{version}-%{release}

Obsoletes: rhsm-gtk <= %{version}-%{release}

%if !%{use_container_plugin}
Obsoletes: subscription-manager-plugin-container <= %{version}
%endif

%if %{use_dnf}
%if %{create_libdnf_rpm}
# The libdnf plugin is in separate RPM, but shubscription-manager should be dependent
# on this RPM, because somebody can install microdnf on host and installing of product
# certs would not work as expected without libdnf plugin
Requires: libdnf-plugin-subscription-manager = %{version}
# The dnf plugin is now part of subscription-manager
Obsoletes: dnf-plugin-subscription-manager < 1.29.0
%endif
%endif

Obsoletes: %{py_package_prefix}-syspurpose <= %{version}

%description
The Subscription Manager package provides programs and libraries to allow users
to manage subscriptions and yum repositories from the Red Hat entitlement
platform.


%if %{use_container_plugin}
%package -n subscription-manager-plugin-container
Summary: A plugin for handling container content
Requires: %{name} = %{version}-%{release}

%description -n subscription-manager-plugin-container
Enables handling of content of type 'containerImage' in any certificates
from the server. Populates /etc/docker/certs.d appropriately.
%endif

%if %{use_dnf}

# RPM containing libdnf plugin
%if %{create_libdnf_rpm}
%package -n libdnf-plugin-subscription-manager
Summary: Subscription Manager plugin for libdnf
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: json-c-devel
BuildRequires: libdnf-devel >= 0.22.5

Obsoletes: dnf-plugin-subscription-manager < 1.29.0

%description -n libdnf-plugin-subscription-manager
This package provides a plugin to interact with repositories from the Red Hat
entitlement platform; contains only one product-id binary plugin used by
e.g. microdnf.

%else

# RPM containing DNF plugin
%package -n dnf-plugin-subscription-manager
Summary: Subscription Manager plugins for DNF

%if (0%{?fedora} || 0%{?rhel}) || (0%{?oreon} >= 11)
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: json-c-devel
BuildRequires: libdnf-devel >= 0.22.5
Requires: json-c
Requires: libdnf >= 0.22.5
%endif

Requires: python3-dnf-plugins-core
Requires: python3-librepo

Requires: dnf >= 1.0.0
%description -n dnf-plugin-subscription-manager
This package provides plugins to interact with repositories and subscriptions
from the Red Hat entitlement platform; contains subscription-manager and
product-id plugins.
%endif

# This redefinition of debuginfo package has to be here, because we
# need to solve the issue described in this BZ:
# https://bugzilla.redhat.com/show_bug.cgi?id=1920568
# We need to obsolete old dnf-sub-man-plugin-debuginfo RPM
%package -n libdnf-plugin-subscription-manager-debuginfo
Summary: Debug information for package libdnf-plugin-subscription-manager
Obsoletes: dnf-plugin-subscription-manager-debuginfo < 1.29.0
%description -n libdnf-plugin-subscription-manager-debuginfo
This package provides debug information for package libdnf-plugin-subscription-manager.
Debug information is useful when developing applications that use this
package or when debugging this package.

%endif


%if %has_ostree
%package -n subscription-manager-plugin-ostree
Summary: A plugin for handling OSTree content.

Requires: %{py_package_prefix}-gobject-base
# plugin needs a slightly newer version of python-iniparse for 'tidy'
Requires:  %{py_package_prefix}-iniparse >= 0.4
Requires: %{name} = %{version}-%{release}

%description -n subscription-manager-plugin-ostree
Enables handling of content of type 'ostree' in any certificates
from the server. Populates /ostree/repo/config as well as updates
the remote in the currently deployed .origin file.
%endif


%package -n %{rhsm_package_name}
Summary: A Python library to communicate with a Red Hat Unified Entitlement Platform
%if 0%{?suse_version}
Group: Development/Libraries/Python
%endif


%if 0%{?suse_version}
Requires:  %{py_package_prefix}-python-dateutil
%else
Requires: %{py_package_prefix}-dateutil
%endif
Requires: %{py_package_prefix}-iniparse
Requires: subscription-manager-rhsm-certificates
# Required by Fedora packaging guidelines
%{?python_provide:%python_provide %{py_package_prefix}-rhsm}
Requires: python3-cloud-what = %{version}-%{release}
Requires: python3-rpm
Provides: python3-rhsm = %{version}-%{release}
Obsoletes: python3-rhsm <= 1.20.3-1
Provides: python-rhsm = %{version}-%{release}
Obsoletes: python-rhsm <= 1.20.3-1

%description -n %{rhsm_package_name}
A small library for communicating with the REST interface of a Red Hat Unified
Entitlement Platform. This interface is used for the management of system
entitlements, certificates, and access to content.



%package -n python3-cloud-what
Summary: Python package for detection of public cloud provider
%if 0%{?suse_version}
Group: Productivity/Networking/System
%endif
Requires: python3-requests
%ifarch %{dmidecode_arches}
Requires: dmidecode
%endif

%description -n python3-cloud-what
This package contains a Python module for detection and collection of public
cloud metadata and signatures.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
make -f Makefile VERSION=%{version}-%{release} CFLAGS="%{optflags}" \
    LDFLAGS="%{__global_ldflags}" OS_DIST="%{dist}" PYTHON="%{__python}" \
    %{?subpackages} %{exclude_packages}

%if %{use_dnf}
pushd src/plugins/libdnf
%cmake -DCMAKE_BUILD_TYPE="Release"
%if (0%{?rhel} && 0%{?rhel} <= 8) || (0%{?oreon} >= 11)
%make_build
%else
%cmake_build
%endif
popd
%endif

%install
make -f Makefile install VERSION=%{version}-%{release} \
    PYTHON=%{__python} PREFIX=%{_prefix} \
    DESTDIR=%{buildroot} PYTHON_SITELIB=%{python_sitearch} \
    OS_VERSION=%{?fedora}%{?rhel}%{?suse_version} OS_DIST=%{dist} \
    COMPLETION_DIR=%{completion_dir} \
    RUN_DIR=%{run_dir} \
    SBIN_DIR=%{_sbindir} \
    %{?install_ostree} %{?install_container} \
    %{?install_dnf_plugins} \
    %{?install_zypper_plugins} \
    %{?subpackages} \
    %{?exclude_packages}

%if %{use_dnf}
pushd src/plugins/libdnf
mkdir -p %{buildroot}%{_libdir}/libdnf/plugins
%if (0%{?rhel} && 0%{?rhel} <= 8) || (0%{?oreon} >= 11)
%make_install
%else
%cmake_install
%endif
popd
%endif

%find_lang rhsm

# fake out the redhat.repo file
%if %{use_dnf}
    mkdir %{buildroot}%{_sysconfdir}/yum.repos.d
    touch %{buildroot}%{_sysconfdir}/yum.repos.d/redhat.repo
%endif

# fake out the certificate directories
mkdir -p %{buildroot}%{_sysconfdir}/pki/consumer
mkdir -p %{buildroot}%{_sysconfdir}/pki/entitlement

%if %{use_container_plugin}
# Setup cert directories for the container plugin:
mkdir -p %{buildroot}%{_sysconfdir}/docker/certs.d/
mkdir %{buildroot}%{_sysconfdir}/docker/certs.d/cdn.redhat.com
install -m 644 %{_builddir}/%{buildsubdir}/src/content_plugins/redhat-entitlement-authority.pem %{buildroot}%{_sysconfdir}/docker/certs.d/cdn.redhat.com/redhat-entitlement-authority.crt
%endif

# fix timestamps on our byte compiled files so they match across arches
find %{buildroot} -name \*.py* -exec touch -r %{SOURCE0} '{}' \;

%if !0%{?suse_version}
%py_byte_compile %{__python3} %{buildroot}%{rhsm_plugins_dir}/
%endif

# symlink services to /usr/sbin/ when building for SUSE distributions
%if 0%{?suse_version}
    ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrhsm
    ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrhsm-facts
    ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrhsmcertd
%endif

# base/cli tools use the gettext domain 'rhsm', while the
# gnome-help tools use domain 'subscription-manager'
%files -f rhsm.lang
%defattr(-,root,root,-)

# Make some unusual directories and files for suse part of subscription-manager
%if 0%{?suse_version}

%dir %{_sysconfdir}/pki
%dir %{_prefix}/share/polkit-1
%dir %{_prefix}/share/polkit-1/actions
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%attr(755,root,root) %dir %{_sysconfdir}/rhsm/zypper.repos.d
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/rhsm/zypper.conf
# zypper plugin
%{_prefix}/lib/zypp/plugins/services/rhsm
# links to /usr/sbin/service
%{_sbindir}/rcrhsm
%{_sbindir}/rcrhsm-facts
%{_sbindir}/rcrhsmcertd

%endif

%dir %{python_sitearch}/rhsmlib/candlepin
%dir %{python_sitearch}/rhsmlib/dbus
%dir %{python_sitearch}/rhsmlib/dbus/facts
%dir %{python_sitearch}/rhsmlib/dbus/objects
%dir %{python_sitearch}/rhsmlib/facts
%dir %{python_sitearch}/rhsmlib/services
%dir %{python_sitearch}/subscription_manager-%{version}-*.egg-info
%dir %{python_sitearch}/subscription_manager/api
%dir %{python_sitearch}/subscription_manager/branding
%dir %{python_sitearch}/subscription_manager/cli_command
%dir %{python_sitearch}/subscription_manager/model
%dir %{python_sitearch}/subscription_manager/plugin
%dir %{python_sitearch}/subscription_manager/scripts
%dir %{_var}/spool/rhsm

%attr(755,root,root) %{_sbindir}/subscription-manager

%attr(755,root,root) %{_bindir}/rhsmcertd
%attr(755,root,root) %{_libexecdir}/rhsmcertd-worker
%attr(755,root,root) %{_libexecdir}/rhsm-package-profile-uploader


# our config dirs and files
%attr(755,root,root) %dir %{_sysconfdir}/pki/consumer
%attr(755,root,root) %dir %{_sysconfdir}/pki/entitlement
%attr(755,root,root) %dir %{_sysconfdir}/rhsm/facts

%attr(755,root,root) %dir %{_sysconfdir}/rhsm/syspurpose
%attr(644,root,root) %{_sysconfdir}/rhsm/syspurpose/valid_fields.json

%attr(644,root,root) %config(noreplace) %{_sysconfdir}/rhsm/rhsm.conf

%if %{use_dnf}
    %ghost %{_sysconfdir}/yum.repos.d/redhat.repo
%endif

# dnf plugin config
%if %{use_dnf}
    # remove the repo file when we are deleted
    %config(noreplace) %attr(644,root,root) %{_sysconfdir}/dnf/plugins/subscription-manager.conf
    %config(noreplace) %attr(644,root,root) %{_sysconfdir}/dnf/plugins/product-id.conf
%endif

# misc system config
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/subscription-manager

%attr(755,root,root) %dir %{_var}/log/rhsm
%attr(755,root,root) %dir %{_var}/spool/rhsm/debug
%ghost %attr(755,root,root) %dir %{run_dir}/rhsm
%attr(750,root,root) %dir %{_var}/lib/rhsm
%attr(750,root,root) %dir %{_var}/lib/rhsm/facts
%attr(750,root,root) %dir %{_var}/lib/rhsm/packages
%attr(750,root,root) %dir %{_var}/lib/rhsm/cache
%attr(750,root,root) %dir %{_var}/lib/rhsm/repo_server_val

%{completion_dir}/subscription-manager
%{completion_dir}/rct
%{completion_dir}/rhsm-debug
%{completion_dir}/rhsmcertd

%{_sysusersdir}/rhsm.conf

%dir %{python_sitearch}/subscription_manager

# code, python modules and packages
%{python_sitearch}/subscription_manager-*.egg-info/*
%{python_sitearch}/subscription_manager/*.py*
%{python_sitearch}/subscription_manager/api/*.py*
%{python_sitearch}/subscription_manager/branding/*.py*
%{python_sitearch}/subscription_manager/cli_command/*.py*
%{python_sitearch}/subscription_manager/model/*.py*
%{python_sitearch}/subscription_manager/plugin/__init__.py*
%{python_sitearch}/subscription_manager/scripts/*.py*
%{python_sitearch}/subscription_manager/__pycache__
%{python_sitearch}/subscription_manager/api/__pycache__
%{python_sitearch}/subscription_manager/branding/__pycache__
%{python_sitearch}/subscription_manager/cli_command/__pycache__
%{python_sitearch}/subscription_manager/model/__pycache__
%{python_sitearch}/subscription_manager/plugin/__pycache__
%{python_sitearch}/subscription_manager/scripts/__pycache__

# subscription-manager plugins
%dir %{rhsm_plugins_dir}
%dir %{_sysconfdir}/rhsm/pluginconf.d

# When libdnf rpm is created, then dnf plugin is part of subscription-manager rpm
%if %{create_libdnf_rpm}
%{python_sitelib}/dnf-plugins/*
%endif

# rhsmlib
%dir %{python_sitearch}/rhsmlib
%{python_sitearch}/rhsmlib/*.py*
%{python_sitearch}/rhsmlib/candlepin/*.py*
%{python_sitearch}/rhsmlib/facts/*.py*
%{python_sitearch}/rhsmlib/services/*.py*
%{python_sitearch}/rhsmlib/dbus/*.py*
%{python_sitearch}/rhsmlib/dbus/facts/*.py*
%{python_sitearch}/rhsmlib/dbus/objects/*.py*
%{python_sitearch}/rhsmlib/__pycache__
%{python_sitearch}/rhsmlib/candlepin/__pycache__
%{python_sitearch}/rhsmlib/dbus/__pycache__
%{python_sitearch}/rhsmlib/dbus/facts/__pycache__
%{python_sitearch}/rhsmlib/dbus/objects/__pycache__
%{python_sitearch}/rhsmlib/facts/__pycache__
%{python_sitearch}/rhsmlib/services/__pycache__

# syspurpose
%dir %{python_sitearch}/syspurpose
%{python_sitearch}/syspurpose/*.py*
%{python_sitearch}/syspurpose/__pycache__

%{_datadir}/polkit-1/actions/com.redhat.*.policy
%{_datadir}/dbus-1/system-services/com.redhat.*.service
%attr(755,root,root) %{_libexecdir}/rhsm*-service

# Despite the name similarity dbus-1/system.d has nothing to do with systemd
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.redhat.*.conf
%attr(644,root,root) %{_unitdir}/*.service
%attr(644,root,root) %{_tmpfilesdir}/%{name}.conf

# Incude rt CLI tool
%dir %{python_sitearch}/rct
%{python_sitearch}/rct/*.py*
%{python_sitearch}/rct/__pycache__
%attr(755,root,root) %{_bindir}/rct

# Include consumer debug CLI tool
%dir %{python_sitearch}/rhsm_debug
%{python_sitearch}/rhsm_debug/*.py*
%{python_sitearch}/rhsm_debug/__pycache__
%attr(755,root,root) %{_bindir}/rhsm-debug

%doc
%{_mandir}/man8/subscription-manager.8*
%{_mandir}/man8/rhsmcertd.8*
%{_mandir}/man8/rct.8*
%{_mandir}/man8/rhsm-debug.8*
%{_mandir}/man5/rhsm.conf.5*
%doc LICENSE

%if %{use_container_plugin}
%files -n subscription-manager-plugin-container
%defattr(-,root,root,-)
%{_sysconfdir}/rhsm/pluginconf.d/container_content.ContainerContentPlugin.conf
%{rhsm_plugins_dir}/container_content.py*
%{rhsm_plugins_dir}/__pycache__/*container*
%{python_sitearch}/subscription_manager/plugin/container/__pycache__
%{python_sitearch}/subscription_manager/plugin/container/*.py*

# Copying Red Hat CA cert into each directory:
%attr(755,root,root) %dir %{_sysconfdir}/docker/certs.d/cdn.redhat.com
%attr(644,root,root) %{_sysconfdir}/docker/certs.d/cdn.redhat.com/redhat-entitlement-authority.crt
%endif

%if %has_ostree
%files -n subscription-manager-plugin-ostree
%defattr(-,root,root,-)
%{_sysconfdir}/rhsm/pluginconf.d/ostree_content.OstreeContentPlugin.conf
%{rhsm_plugins_dir}/ostree_content.py*
%{python_sitearch}/subscription_manager/plugin/ostree/*.py*
%{python_sitearch}/subscription_manager/plugin/ostree/__pycache__
%{rhsm_plugins_dir}/__pycache__/*ostree*
%endif


%if %{use_dnf}
# libdnf RPM
%if %{create_libdnf_rpm}
%files -n libdnf-plugin-subscription-manager
%defattr(-,root,root,-)
%{_libdir}/libdnf/plugins/product-id.so
%else
# DNF RPM
%files -n dnf-plugin-subscription-manager
%defattr(-,root,root,-)
%{python_sitelib}/dnf-plugins/*
%{_libdir}/libdnf/plugins/product-id.so
%endif
%endif


%files -n %{rhsm_package_name}
%defattr(-,root,root,-)
%dir %{python_sitearch}/rhsm
%{python_sitearch}/rhsm/*

%files -n python3-cloud-what
%defattr(-,root,root,-)
%attr(750,root,root) %dir %{_var}/cache/cloud-what
%dir %{python_sitearch}/cloud_what
%dir %{python_sitearch}/cloud_what/providers
%{python_sitearch}/cloud_what/*.py*
%{python_sitearch}/cloud_what/providers/*.py*
%{python_sitearch}/cloud_what/__pycache__
%{python_sitearch}/cloud_what/providers/__pycache__

%pre


%if 0%{?suse_version}
    %service_add_pre rhsm.service
    %service_add_pre rhsm-facts.service
    %service_add_pre rhsmcertd.service
%endif

%post
%if 0%{?suse_version}
    %service_add_post rhsmcertd.service
    %service_add_post rhsm.service
    %service_add_post rhsm-facts.service
    %tmpfiles_create %{_tmpfilesdir}/subscription-manager.conf
%else
    %systemd_post rhsmcertd.service
%endif

# When subscription-manager is upgraded on RHEL 8 (from RHEL 8.2 to RHEL 8.3), then kill
# instance of rhsmd, because it is not necessary anymore and it can cause issues.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1840364
%if ( 0%{?rhel} || 0%{?fedora} ) || (0%{?oreon} >= 11)
if [ "$1" = "2" ] ; then
    killall rhsmd 2> /dev/null || true
fi
%endif

# Make all consumer certificates and keys readable by group rhsm
find /etc/pki/consumer -mindepth 1 -maxdepth 1 -name '*.pem' | xargs --no-run-if-empty chgrp rhsm
find /etc/pki/consumer -mindepth 1 -maxdepth 1 -name '*.pem' | xargs --no-run-if-empty chmod g+r

# Make all entitlement certificates and keys files readable by group and other
find /etc/pki/entitlement -mindepth 1 -maxdepth 1 -name '*.pem' | xargs --no-run-if-empty chmod go+r

if [ -x /bin/dbus-send ] ; then
    dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig > /dev/null 2>&1 || :
fi


%if %{use_container_plugin}
%post -n subscription-manager-plugin-container
%{__python} %{rhsm_plugins_dir}/container_content.py || :
%endif

%preun
if [ $1 -eq 0 ] ; then
    %if 0%{?suse_version}
        %service_del_preun rhsm.service
        %service_del_preun rhsm-facts.service
        %service_del_preun rhsmcertd.service
    %else
        %systemd_preun rhsmcertd.service
    %endif

    if [ -x /bin/dbus-send ] ; then
        dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig > /dev/null 2>&1 || :
    fi
fi

%postun
%if 0%{?suse_version}
    %service_del_postun rhsmcertd.service
    %service_del_postun rhsm.service
    %service_del_postun rhsm-facts.service
%else
    %systemd_postun_with_restart rhsmcertd.service
%endif

%posttrans
%systemd_posttrans_with_restart rhsm.service
# Remove old *.egg-info empty directories not removed be previous versions of RPMs
# due to this BZ: https://bugzilla.redhat.com/show_bug.cgi?id=1927245
rmdir %{python_sitearch}/subscription_manager-*-*.egg-info --ignore-fail-on-non-empty
# Remove old cache files
# The -f flag ensures that exit code 0 will be returned even if the file does not exist.
rm -f /var/lib/rhsm/cache/rhsm_icon.json
rm -f /var/lib/rhsm/cache/content_access_mode.json

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30.5-6
- Import
