%global source0_hash 5dfee927ff64c88fd17cef1c6426a56dfc5d834aff07318741f7fa73f5246e92
%global uname hacluster
%global gname haclient
%global pcmk_docdir %{_docdir}/%{name}
%global github_owner ClusterLabs
%global ocf_root %{_prefix}/lib/ocf
%global pcmkversion 3.0.3
%global baserelease 15
%global commit 16e74fc4da93a08514e1ec320fa9530b6c3d9fd5
%global commit_abbrev 9
%bcond_with linuxha
%bcond_without cibsecrets
%bcond_with nls
%bcond_with profiling
%bcond_without doc
%bcond_without sbd_sync
%bcond_with pre_release
%bcond_without hardening
%define archive_version %(c=%{commit}; echo ${c:0:%{commit_abbrev}})
%define archive_github_url %{archive_version}#/%{name}-%{archive_version}.tar.gz
%if %{with pre_release}
%define pcmk_release 0.%{baserelease}
%else
%define pcmk_release %{baserelease}
%endif
%define gnutls_priorities %{?pcmk_gnutls_priorities}%{!?pcmk_gnutls_priorities:@SYSTEM}
%global pkgname_libtool_devel libtool-ltdl-devel
%global pkgname_libtool_devel_arch libtool-ltdl-devel%{?_isa}
%global pkgname_bzip2_devel bzip2-devel
%global pkgname_docbook_xsl docbook-style-xsl
%global pkgname_gettext gettext-devel
%global pkgname_shadow_utils shadow-utils
%global pkgname_procps procps-ng
%global pkgname_glue_libs cluster-glue-libs
%global pkgname_pcmk_libs %{name}-libs
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global resource_stickiness --with-resource-stickiness-default=1
%endif
%if %{defined _python_bytecompile_extra}
%global _python_bytecompile_extra 0
%else
%global __os_install_post %(echo '%{__os_install_post}' | {
                            sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g'; })
%endif
%if %{defined __python3}
%global python_name python3
%global python_path %{__python3}
%define python_site %{?python3_sitelib}%{!?python3_sitelib:%(
  %{python_path} -c 'from distutils.sysconfig import get_python_lib as gpl; print(gpl(1))' 2>/dev/null)}
%else
%if %{defined python_version}
%global python_name python%(echo %{python_version} | cut -d'.' -f1)
%define python_path %{?__python}%{!?__python:/usr/bin/%{python_name}}
%else
%global python_name python
%global python_path %{?__python}%{!?__python:/usr/bin/python%{?python_pkgversion}}
%endif
%define python_site %{?python_sitelib}%{!?python_sitelib:%(
  %{python_name} -c 'from distutils.sysconfig import get_python_lib as gpl; print(gpl(1))' 2>/dev/null)}
%endif
%if %{with profiling}
%define debug_package %{nil}
%endif
Name:          pacemaker
Summary:        Scalable High-Availability cluster resource manager
Version:       %{pcmkversion}
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Url:           https://www.clusterlabs.org/
Source0:        https://codeload.github.com/%{github_owner}/%{name}/tar.gz/%{archive_version}#/%{name}-%{archive_version}.tar.gz
Source1:       pacemaker.sysusers
Patch0:        0001-Low-various-Use-const-for-a-few-string-pointer-varia.patch
Patch1:        0002-Fix-build-Handle-CMocka-deprecations.patch
Requires:      resource-agents
Requires:      %{pkgname_pcmk_libs}%{?_isa} = %{version}-%{release}
Requires:      %{name}-cluster-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-cli = %{version}-%{release}
%{?systemd_requires}
Requires:      %{python_path}
Requires:      libqb >= 1.0.1
%if %{defined pkgname_libtool_devel}
%endif
Requires:      corosync >= 2.0.0
%if %{with linuxha}
%endif
%if %{with doc}
%endif
Provides:      pacemaker-ticket-support = 2.0
Provides:      pcmk-cluster-manager = %{version}-%{release}
Provides:      pcmk-cluster-manager%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  corosync-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  grep
BuildRequires:  help2man
BuildRequires:  libcmocka-devel
BuildRequires:  libqb-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3-devel
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

It supports more than 16 node clusters with significant capabilities
for managing resources and dependencies.

It will run scripts at initialization, when machines go up or down,
when related resources fail and can be configured to periodically check
resource health.

Available rpmbuild rebuild options:
  --with(out) : cibsecrets hardening linuxha nls pre_release profiling

%package cli
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Command line tools for controlling Pacemaker clusters
Requires:      %{pkgname_pcmk_libs}%{?_isa} = %{version}-%{release}
Recommends:    pcmk-cluster-manager = %{version}-%{release}
Recommends:    tar
Recommends:    bzip2
Requires:      perl-TimeDate
Requires:      %{pkgname_procps}
Requires:      psmisc
Requires:      %{python_name}-psutil
Requires(post):coreutils
%description cli
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-cli package contains command line tools that can be used
to query and control the cluster from machines that may, or may not,
be part of the cluster.

%package -n %{pkgname_pcmk_libs}
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Core Pacemaker libraries
Requires(pre): %{pkgname_shadow_utils}
Requires:      %{name}-schemas = %{version}-%{release}
Conflicts:     sbd < 1.5.0
Conflicts:     pcs < 0.11
%description -n %{pkgname_pcmk_libs}
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{pkgname_pcmk_libs} package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package cluster-libs
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Cluster Libraries used by Pacemaker
Requires:      %{pkgname_pcmk_libs}%{?_isa} = %{version}-%{release}
%description cluster-libs
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-cluster-libs package contains cluster-aware shared
libraries needed for nodes that will form part of the cluster nodes.

%package -n %{python_name}-%{name}
License:       LGPL-2.1-or-later
Summary:       Python libraries for Pacemaker
Requires:      %{python_path}
Requires:      %{pkgname_pcmk_libs} = %{version}-%{release}
BuildArch:     noarch
%description -n %{python_name}-%{name}
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{python_name}-%{name} package contains a Python library that can be used
to interface with Pacemaker.

%package remote
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Pacemaker remote executor daemon for non-cluster nodes
Requires:      %{pkgname_pcmk_libs}%{?_isa} = %{version}-%{release}
Requires:      %{name}-cli = %{version}-%{release}
Requires:      %{python_name}-%{name} = %{version}-%{release}
Requires:      resource-agents
%{?systemd_requires}
Provides:      pcmk-cluster-manager = %{version}-%{release}
Provides:      pcmk-cluster-manager%{?_isa} = %{version}-%{release}
%description remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package -n %{pkgname_pcmk_libs}-devel
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Pacemaker development package
Requires:      %{pkgname_pcmk_libs}%{?_isa} = %{version}-%{release}
Requires:      %{name}-cluster-libs%{?_isa} = %{version}-%{release}
Requires:      %{pkgname_bzip2_devel}%{?_isa}
Requires:      corosync-devel >= 2.0.0
Requires:      glib2-devel%{?_isa}
Requires:      libqb-devel%{?_isa} >= 1.0.1
%if %{defined pkgname_libtool_devel_arch}
Requires:      %{?pkgname_libtool_devel_arch}
%endif
Requires:      libuuid-devel%{?_isa}
Requires:      libxml2-devel%{?_isa} >= 2.9.2
Requires:      libxslt-devel%{?_isa}
%description -n %{pkgname_pcmk_libs}-devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{pkgname_pcmk_libs}-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package       cts
License:       GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Test framework for cluster-related technologies like Pacemaker
Requires:      %{python_path}
Requires:      %{pkgname_pcmk_libs} = %{version}-%{release}
Requires:      %{name}-cli = %{version}-%{release}
Requires:      %{pkgname_procps}
Requires:      psmisc
BuildArch:     noarch
Requires:      %{python_name}-systemd
%description   cts
Test framework for cluster-related technologies like Pacemaker

%package       doc
License:       CC-BY-SA-4.0
Summary:       Documentation for Pacemaker
BuildArch:     noarch
Conflicts:     %{name}-libs > %{version}-%{release}
Conflicts:     %{name}-libs < %{version}-%{release}
%description   doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

%package       schemas
License:       GPL-2.0-or-later
Summary:       Schemas and upgrade stylesheets for Pacemaker
BuildArch:     noarch
%description   schemas
Schemas and upgrade stylesheets for Pacemaker

Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{archive_version} -S git_am -p 1
# in f33 s390x complains but shouldn't hurt globally
# as configure.ac is checking for support
sed -i configure.ac -e "s/-Wall/-Wall -Wno-format-truncation/"

%build

export systemdsystemunitdir=%{?_unitdir}
%if %{with hardening}
export CFLAGS_HARDENED_EXE="%{?_hardening_cflags}"
export CFLAGS_HARDENED_LIB="%{?_hardening_cflags}"
export LDFLAGS_HARDENED_EXE="%{?_hardening_ldflags}"
export LDFLAGS_HARDENED_LIB="%{?_hardening_ldflags}"
%endif
./autogen.sh
%{configure}                                                                    \
        PYTHON=%{python_path}                                                   \
        %{!?with_hardening:    --disable-hardening}                             \
        %{?with_profiling:     --with-profiling}                                \
        %{?with_cibsecrets:    --with-cibsecrets}                               \
        %{?with_nls:           --enable-nls}                                    \
        %{?with_sbd_sync:      --with-sbd-sync-default="true"}                  \
        %{?gnutls_priorities:  --with-gnutls-priorities="%{gnutls_priorities}"} \
        %{?bug_url:            --with-bug-url=%{bug_url}}                       \
        %{?ocf_root:           --with-ocfdir=%{ocf_root}}                       \
        %{?resource_stickiness}                                                 \
        --disable-static                                                        \
        --with-initdir=%{_initrddir}                                            \
        --with-runstatedir=%{_rundir}                                           \
        --localstatedir=%{_var}                                                 \
        --with-version=%{version}-%{release}
make %{_smp_mflags} V=1
pushd python
%py3_build
popd
%check

make %{_smp_mflags} check
{ cts/cts-scheduler --run load-stopped-loop \
  && cts/cts-cli -V \
  && touch .CHECKED
} 2>&1 | sed 's/[fF]ail/faiil/g'  # prevent false positives in rpmlint
[ -f .CHECKED ] && rm -f -- .CHECKED
%install
make install \
  DESTDIR=%{buildroot} V=1 docdir=%{pcmk_docdir} \
  %{?_python_bytecompile_extra:%{?py_byte_compile:am__py_compile=true}}
pushd python
%py3_install
popd
mkdir -p %{buildroot}%{_datadir}/pacemaker/nagios/plugins-metadata
for file in $(find %{nagios_name}-%{nagios_hash}/metadata -type f); do
    install -m 644 $file %{buildroot}%{_datadir}/pacemaker/nagios/plugins-metadata
done
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/lib/rpm-state/%{name}
find %{buildroot} -name '*.la' -type f -print0 | xargs -0 rm -f
rm -f %{buildroot}/%{_sbindir}/fence_legacy
rm -f %{buildroot}/%{_mandir}/man8/fence_legacy.*
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/pacemaker.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post pacemaker.service
%preun

%systemd_preun pacemaker.service
%postun

%systemd_postun_with_restart pacemaker.service
%pre remote

systemctl --quiet is-active pacemaker_remote
if [ $? -eq 0 ] ; then
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    touch %{_localstatedir}/lib/rpm-state/%{name}/restart_pacemaker_remote
    systemctl stop pacemaker_remote >/dev/null 2>&1
else
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/restart_pacemaker_remote
fi
%post remote

%systemd_post pacemaker_remote.service
%preun remote

%systemd_preun pacemaker_remote.service
%postun remote

%systemd_postun_with_restart pacemaker_remote.service
if [ "$1" -eq 0 ] ; then
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/restart_pacemaker_remote
fi
%posttrans remote

if [ -e %{_localstatedir}/lib/rpm-state/%{name}/restart_pacemaker_remote ] ; then
    systemctl start pacemaker_remote >/dev/null 2>&1
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/restart_pacemaker_remote
fi
%post cli

%systemd_post crm_mon.service
if [ "$1" -eq 2 ]; then
    { mv -fbS.rpmsave %{_var}/log/pacemaker.log* %{_var}/log/pacemaker \
      || mv -f %{_var}/log/pacemaker.log* %{_var}/log/pacemaker
    } >/dev/null 2>/dev/null || :
fi
%preun cli

%systemd_preun crm_mon.service
%postun cli

%systemd_postun_with_restart crm_mon.service
%ldconfig_scriptlets -n %{pkgname_pcmk_libs}
%ldconfig_scriptlets cluster-libs
%files -f %{oreon_filedir}/main.list
%files -n pacemaker-cli -f %{oreon_filedir}/pacemaker-cli.list
%files -n pacemaker-libs -f %{oreon_filedir}/pacemaker-libs.list
%files -n pacemaker-cluster-libs -f %{oreon_filedir}/pacemaker-cluster-libs.list
%files -n python3-pacemaker -f %{oreon_filedir}/python3-pacemaker.list
%files -n pacemaker-remote -f %{oreon_filedir}/pacemaker-remote.list
%files -n pacemaker-libs-devel -f %{oreon_filedir}/pacemaker-libs-devel.list
%files -n pacemaker-cts -f %{oreon_filedir}/pacemaker-cts.list
%files -n pacemaker-doc -f %{oreon_filedir}/pacemaker-doc.list
%files -n pacemaker-schemas -f %{oreon_filedir}/pacemaker-schemas.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{pcmkversion}-1
- Prepare for Oreon 11 (RP1)
