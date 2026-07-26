%global source0_hash b3bab42db961fc40256306d9dd3c8a11dc5992cdec8377064fee3db6da4f4de8

%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})

# unfortunately, radicale major version upgrades are breakable updates, therefore
# Fedora >= 31: introduce radicale3
#
# Note: this is the simplified spec file for Fedora

### supports following defines during RPM build:
#
### specific git commit on upstream (EXAMPLE)
## build SRPMS
# fedpkg srpm --define "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" -- --undefine=_disable_source_fetch
#
## build RPMS local
# fedpkg local --define "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" -- --undefine=_disable_source_fetch
#
## rebuild SRPMS on a different system using
# rpmbuild --rebuild --define "gitcommit 49d0ad5b18a3867925e2ffd1d8cec21d99e13b3e" radicale3-<VERSION>-<RELEASE>.YYYYMMDDgitSHORTHASH.DIST.src.rpm

%define radicale_major  3

%define radicale_version  3.6.1
%define radicale_release  1
#define gitcommit 8e9fdf391acb79d3fb1cb6e6b8f882f8999192cf

%define radicale_name  radicale

%define radicale_package_name  radicale3

%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif

Name:           radicale
Version:        %{radicale_version}
Release:        %{radicale_release}%{?gittag}%{?dist}.1
Summary:        A simple CalDAV (calendar) and CardDAV (contact) server
License:        GPL-3.0-or-later
URL:            https://radicale.org

%if 0%{?gitcommit:1}
Source0:        https://github.com/Kozea/Radicale/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
%else
Source0:        https://github.com/Kozea/Radicale/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

%define infcloud_version  0.13.1

Source1:          %{name}.service
Source4:          %{name}.te
Source5:          %{name}.fc
Source6:          %{name}.if
Source7:          %{name}-tmpfiles.conf
Source8:          %{name}.sysconfig

Source50:         %{name}-test-example.ics
Source51:         %{name}-test-example.vcf

Source60:         https://inf-it.com/open-source/download/InfCloud_%{infcloud_version}.zip

BuildArch:        noarch

BuildRequires:    python3-devel
%generate_buildrequires
%pyproject_buildrequires

%package -n %{radicale_package_name}
Summary:          %{summary}

BuildRequires:    systemd
BuildRequires:    checkpolicy
BuildRequires:    selinux-policy-devel
BuildRequires:    hardlink

# for 'make check'
BuildRequires:    python3-defusedxml >= 0.7.1
BuildRequires:    python3-passlib >= 1.7.4
BuildRequires:    python3-vobject >= 0.9.6
BuildRequires:    python3-packaging

Conflicts:        radicale < 3.0.0
Conflicts:        radicale2

Requires:         python3-%{radicale_package_name} = %{version}-%{release}
%if (0%{?rhel} < 11) || (0%{?fedora} < 43)
Requires(pre):    shadow-utils
%endif
%{?systemd_requires}
Suggests:         %{radicale_package_name}-selinux = %{version}-%{release}

%description
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

%description -n %{radicale_package_name}
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

THIS IS MAJOR VERSION %{?radicale_major}

UPGRADE BETWEEN MAJOR VERSIONS IS NOT SUPPORTED
        -> deinstall old major version
        -> install new version
        -> follow migration hints
Upgrade hints from major version 2 -> 3 can be found here:
 https://github.com/Kozea/Radicale/blob/v3.1.0/NEWS.md
  (section '3.0.0')

%package -n python3-%{radicale_package_name}
Summary:          Python module for Radicale
Recommends:       python3-bcrypt
Recommends:       python3-argon2-cffi
Recommends:       python3-passlib
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:        python-%{radicale_package_name} < %{version}-%{release}

Conflicts:        python3-radicale < 3.0.0
Conflicts:        python3-radicale2

%description -n python3-%{radicale_package_name}
Python module for Radicale

%package -n %{radicale_package_name}-httpd
Summary:        httpd config for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
Requires:       httpd
Requires:       python3-mod_wsgi

Conflicts:      radicale-httpd < 3.0.0
Conflicts:      radicale2-httpd

%description -n %{radicale_package_name}-httpd
httpd example config for Radicale (Python3).

%package -n %{radicale_package_name}-selinux
Summary:        SELinux definitions for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
%if "%{_selinux_policy_version}" != ""
Requires:         selinux-policy >= %{_selinux_policy_version}
%endif
Requires(post):   /usr/sbin/semodule
Requires(post):   /usr/sbin/fixfiles
Requires(post):   /usr/sbin/restorecon
Requires(post):   policycoreutils-python-utils
Requires(postun): /usr/sbin/semodule
Requires(postun): /usr/sbin/fixfiles
Requires(postun): /usr/sbin/restorecon
Requires(postun): policycoreutils-python-utils

%description -n %{radicale_package_name}-selinux
SELinux definitions for Radicale (Python3).
Supported toggles:
 - httpd_can_read_write_radicale
 - radicale_use_fusefs
 - radicale_exec_storage_hook

%package -n %{radicale_package_name}-logwatch
Summary:        logwatch config for Radicale
Requires:       %{radicale_package_name} = %{version}-%{release}
Requires:       logwatch

%description -n %{radicale_package_name}-logwatch
logwatch configuration for Radicale

%package -n %{radicale_package_name}-InfCloud
Summary:        InfCloud extension for Radicale internal WebUI
License:        AGPL-3.0-only
URL:            https://inf-it.com/open-source/clients/infcloud/
BuildRequires:  unzip
Requires:       ed
BuildRequires:  ed
Requires:       python3-%{radicale_package_name} = %{version}-%{release}

%description -n %{radicale_package_name}-InfCloud
Infcloud extension for Radicale internal WebUI
Bundled version: %{infcloud_version}

%package -n %{radicale_package_name}-InfCloud-fontware
Summary:        Fonts for InfCloud extension for Radicale internal WebUI
License:        Apache-2.0
URL:            https://inf-it.com/open-source/clients/infcloud/
Requires:       %{radicale_package_name}-InfCloud = %{version}-%{release}
Obsoletes:	%{radicale_package_name}-InfCloud-fonts < 3.5.4-3

%description -n %{radicale_package_name}-InfCloud-fontware
Fonts for Infcloud extension for Radicale internal WebUI
Bundled version: %{infcloud_version}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?gitcommit:1}
%define build_version %{gitcommit}
%else
%define build_version %{version}
%endif
%autosetup -n Radicale-%{build_version} -p 1

# inject SELinux note
sed -i 's|\(#hook =\)|# Note: in case SELinux is active, set related toggle: setsebool -P radicale_exec_storage_hook 1\n\1|' config

mkdir SELinux
cp -p %{SOURCE4} %{SOURCE5} %{SOURCE6} SELinux

# adjust _rundir according to definition
sed -i 's|\(/var/run\)|%{_rundir}|' SELinux/%{name}.fc

# restore original version after applying patches
%{__sed} -i 's|version = "%{radicale_major}.dev"|version = "%{radicale_version}"|' pyproject.toml

# restore "passlib" requirement until "libpass" is available
%{__sed} -i 's|libpass[^"]*|passlib|' pyproject.toml

%if (0%{?rhel} >= 11) || (0%{?fedora} >= 43)
# Create a sysusers.d config file
cat >radicale.sysusers.conf <<EOF
u radicale - 'Radicale service account' %{_sharedstatedir}/%{name} -
EOF
%endif

%build
%pyproject_wheel

cd SELinux
for selinuxvariant in %{selinux_variants}
do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
    %{__mv} %{name}.pp %{name}.pp.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
%pyproject_install
%if (0%{?rhel} >= 11) || (0%{?fedora} >= 43)
%pyproject_save_files -l %{name}
%endif

# move scripts away from _bindir to avoid conflicts and create a wrapper scripts
install -d -p %{buildroot}%{_libexecdir}/%{name}
%{__mv} %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/

cat > %{buildroot}%{_bindir}/%{radicale_name} << EOF
#!/bin/sh
if [ "\$(whoami)" != "%{name}" ]; then
    echo "This command must be run under the radicale user (%{name})."
    exit 1
fi
%{_libexecdir}/%{name}/%{radicale_name} \$@
EOF
chmod a+x %{buildroot}%{_bindir}/%{radicale_name}

# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 config %{buildroot}%{_sysconfdir}/%{name}/
sed -i 's|^#\(level =\).*|\1 info|' %{buildroot}%{_sysconfdir}/%{name}/config
install -p -m 640 rights %{buildroot}%{_sysconfdir}/%{name}/

# Empty configuration file
touch %{buildroot}%{_sysconfdir}/%{name}/users

# Install sysconfig file
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 640 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# Install wsgi file
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 radicale.wsgi %{buildroot}%{_datadir}/%{name}/
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/radicale.wsgi

# Install apache's configuration file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 contrib/apache/radicale.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Create folder where the collection-root will be stored (and radicale's home directory)
install -d -p  %{buildroot}%{_sharedstatedir}/%{name}

# Create folder where the collection-cache can be stored optional
install -d -p  %{buildroot}%{_localstatedir}/cache/%{name}

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

install -D -p -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}

# adjust _rundir
sed -i 's|/var/run|%{_rundir}|' %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i 's|/var/run|%{_rundir}|' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_rundir}/%{name}

for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done

%if 0%{?rhel} == 7 || 0%{?rhel} == 8
/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux
%else
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux
%endif

# logwatch
install -d %{buildroot}%{_datarootdir}/logwatch/scripts/services/
install -d %{buildroot}%{_datarootdir}/logwatch/default.conf/services/
install -p -m 644 contrib/logwatch/%{name} %{buildroot}%{_datarootdir}/logwatch/scripts/services/
install -p -m 644 contrib/logwatch/%{name}-journald.conf %{buildroot}%{_datarootdir}/logwatch/default.conf/services/%{name}.conf

%if (0%{?rhel} >= 11) || (0%{?fedora} >= 43)
install -m0644 -D radicale.sysusers.conf %{buildroot}%{_sysusersdir}/radicale.conf
%endif

## infcloud
# unpack
%{__unzip} -d %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/ %{SOURCE60}
# update cache
pushd %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/
./cache_update.sh
popd
# remove not required files
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/cache_update.sh
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/.htaccess
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/readme.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog_carddavmate.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog_caldavzap.txt
%{__rm} -rf %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/auth/
%{__rm} -rf %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/misc/

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONPATH

# check whether radicale binary is at least displaying help
echo "Check whether 'radicale' is at least able to display online help"
%{buildroot}%{_libexecdir}/%{name}/%{radicale_name} --help >/dev/null
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is at least able to display online help - SUCCESSFUL"
else
  exit 1
fi

# create radicale collections with examples
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf
cp %{SOURCE50} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/
cp %{SOURCE51} %{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/
echo '{"tag": "VADDRESSBOOK"}' >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-vcf/.Radicale.props
echo '{"tag": "VCALENDAR"}'    >%{buildroot}%{_sharedstatedir}/%{name}/collection-root/test-ics/.Radicale.props

echo "Check whether 'radicale' is able to verify example storage"
%{buildroot}%{_libexecdir}/%{name}/%{radicale_name} -D --verify-storage --storage-filesystem-folder /%{buildroot}%{_sharedstatedir}/%{name}
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is able to verify example storage - SUCCESSFUL"
else
  exit 1
fi

# cleanup before packaging
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/collection-root
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/.Radicale.lock

%pre -n %{radicale_package_name}
%if (0%{?rhel} < 11) || (0%{?fedora} < 43)
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Radicale service account" %{name}
exit 0
%endif

%post -n %{radicale_package_name}
%systemd_post %{name}.service

%post -n %{radicale_package_name}-selinux
for selinuxvariant in %{selinux_variants}
do
  if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant)"
    /usr/sbin/semodule -s ${selinuxvariant} -i \
      %{_datadir}/selinux/${selinuxvariant}/%{name}.pp
  else
    echo "SELinux semodule store for %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
  fi
done
# http://danwalsh.livejournal.com/10607.html
if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232 already done"
else
  echo "SELinux adjustments for %{radicale_package_name} port tcp/5232"
  semanage port -a -t radicale_port_t -p tcp 5232
fi

echo "SELinux fixfiles for: %{radicale_package_name}"
/usr/sbin/fixfiles -R %{radicale_package_name} restore >/dev/null

if [ -d %{_localstatedir}/log/%{name} ]; then
  echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
  /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
fi

%post -n python3-%{radicale_package_name}
# nothing related included so far in radicale.fc

%post -n %{radicale_package_name}-httpd
# nothing related included so far in radicale.fc

%preun -n %{radicale_package_name}
%systemd_preun %{name}.service

%postun -n %{radicale_package_name}
%systemd_postun_with_restart %{name}.service 

%postun -n %{radicale_package_name}-selinux
if [ $1 -eq 0 ] ; then
  if semanage port -l | grep -q "^radicale_port_t\s*tcp\s*5232$"; then
    echo "SELinux delete for %{radicale_package_name} port tcp/5232"
    semanage port -d -p tcp 5232
  fi
  for selinuxvariant in %{selinux_variants}
  do
    if rpm -q selinux-policy-$selinuxvariant >/dev/null 2>&1; then
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant)"
      /usr/sbin/semodule -s ${selinuxvariant} -r %{name}
    else
      echo "SELinux semodule reset %{radicale_package_name} ($selinuxvariant) SKIPPED - policy not installed"
    fi
  done

  if [ -d %{_localstatedir}/log/%{name} ]; then
    echo "SELinux restorecon for: %{_localstatedir}/log/%{name}"
    /usr/sbin/restorecon -R %{_localstatedir}/log/%{name}
  fi
fi

%files -n %{radicale_package_name}
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/config
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/rights
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/users
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(750, %{name}, %{name}) %{_sharedstatedir}/%{name}
%dir %attr(750, %{name}, %{name}) %{_localstatedir}/cache/%{name}
%dir %{_datadir}/%{name}
%dir %attr(755, %{name}, %{name}) %{_rundir}/%{name}

%{_libexecdir}/%{name}
%if (0%{?rhel} >= 11) || (0%{?fedora} >= 43)
%{_sysusersdir}/radicale.conf
%endif

%files -n %{radicale_package_name}-selinux
%doc SELinux/*
%{_datadir}/selinux/*/%{name}.pp

%if (0%{?rhel} >= 11) || (0%{?fedora} >= 43)
%files -n python3-%{radicale_package_name} -f %{pyproject_files}
%else
%files -n python3-%{radicale_package_name}
%license COPYING.md
%{python3_sitelib}/%{name}
%{python3_sitelib}/Radicale-*-info
%exclude %{python3_sitelib}/%{name}/web/internal_data/infcloud
%endif

%files -n %{radicale_package_name}-logwatch
%{_datarootdir}/logwatch/scripts/services/%{name}
%{_datarootdir}/logwatch/default.conf/services/%{name}.conf

%files -n %{radicale_package_name}-httpd
%{_datadir}/%{name}/%{name}.wsgi
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%files -n %{radicale_package_name}-InfCloud
%{python3_sitelib}/%{name}/web/internal_data/infcloud
%exclude %{python3_sitelib}/%{name}/web/internal_data/infcloud/fonts

%files -n %{radicale_package_name}-InfCloud-fontware
%{python3_sitelib}/%{name}/web/internal_data/infcloud/fonts

%changelog
%autochangelog
