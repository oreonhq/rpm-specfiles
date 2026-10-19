%global source60_hash 9fa95edd2dcc2b864a10b503ab9220895ea28d4c5541ab02117de1511d5464d4
%global source0_hash 066c02cde17cb577e1797b9b54561bfc882f721edd6ae895bc51eacac5ee9089
%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})
%define radicale_major  3
%define radicale_version  3.8.0
%define radicale_release  1
%define radicale_name  radicale
%define radicale_package_name  radicale3
%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif
Name:           radicale
Version:        %{radicale_version}
Release:        1%{?dist}
Summary:        A simple CalDAV (calendar) and CardDAV (contact) server
License:        GPL-3.0-or-later
URL:            https://radicale.org
%if 0%{?gitcommit:1}
Source0:        https://github.com/Kozea/Radicale/archive/v%{version}/%{name}-%{version}.tar.gz
%else
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
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-radicale = %{version}-%{release}
# /oreon:deps
%package -n       python3-radicale+test
Summary:        Metapackage for python3-radicale test extras
Requires:       python3-radicale = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Provides:       python3dist(radicale[test]) = %{version}-%{release}

%description -n python3-radicale+test
Metapackage for python3-radicale test extras.

%package -n       python3-radicale+bcrypt
Summary:        Metapackage for python3-radicale bcrypt extras
Requires:       python3-radicale = %{version}-%{release}
Provides:       python3dist(radicale[bcrypt]) = %{version}-%{release}

%description -n python3-radicale+bcrypt
Metapackage for python3-radicale bcrypt extras.

%package -n       python3-radicale+argon2
Summary:        Metapackage for python3-radicale argon2 extras
Requires:       python3-radicale = %{version}-%{release}
Provides:       python3dist(radicale[argon2]) = %{version}-%{release}

%description -n python3-radicale+argon2
Metapackage for python3-radicale argon2 extras.

%package -n       python3-radicale+ldap
Summary:        Metapackage for python3-radicale ldap extras
Requires:       python3-radicale = %{version}-%{release}
Provides:       python3dist(radicale[ldap]) = %{version}-%{release}

%description -n python3-radicale+ldap
Metapackage for python3-radicale ldap extras.

%package -n       python3-radicale+pam
Summary:        Metapackage for python3-radicale pam extras
Requires:       python3-radicale = %{version}-%{release}
Provides:       python3dist(radicale[pam]) = %{version}-%{release}

%description -n python3-radicale+pam
Metapackage for python3-radicale pam extras.

%package -n       python3-radicale+dev
Summary:        Metapackage for python3-radicale dev extras
Requires:       python3-radicale = %{version}-%{release}
Provides:       python3dist(radicale[dev]) = %{version}-%{release}

%description -n python3-radicale+dev
Metapackage for python3-radicale dev extras.

%package -n %{radicale_package_name}
Summary:        A simple CalDAV (calendar) and CardDAV (contact) server
BuildRequires:    systemd
BuildRequires:    checkpolicy
BuildRequires:    selinux-policy-devel
BuildRequires:    hardlink
BuildRequires:    python3-defusedxml >= 0.7.1
BuildRequires:    python3-passlib >= 1.7.4
BuildRequires:    python3-vobject >= 0.9.6
BuildRequires:    python3-packaging
Conflicts:        radicale < 3.0.0
Conflicts:        radicale2
Requires:         python3-%{radicale_package_name} = %{version}-%{release}
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
install -d -p %{buildroot}%{_libexecdir}/%{name}
%{__mv} %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/
cat > %{buildroot}%{_bindir}/%{radicale_name} << EOF
if [ "\$(whoami)" != "%{name}" ]; then
    echo "This command must be run under the radicale user (%{name})."
    exit 1
fi
%{_libexecdir}/%{name}/%{radicale_name} \$@
EOF
chmod a+x %{buildroot}%{_bindir}/%{radicale_name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 config %{buildroot}%{_sysconfdir}/%{name}/
sed -i 's|^#\(level =\).*|\1 info|' %{buildroot}%{_sysconfdir}/%{name}/config
install -p -m 640 rights %{buildroot}%{_sysconfdir}/%{name}/
touch %{buildroot}%{_sysconfdir}/%{name}/users
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -p -m 640 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 radicale.wsgi %{buildroot}%{_datadir}/%{name}/
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/radicale.wsgi
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 contrib/apache/radicale.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -d -p  %{buildroot}%{_sharedstatedir}/%{name}
install -d -p  %{buildroot}%{_localstatedir}/cache/%{name}
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}
sed -i 's|/var/run|%{_rundir}|' %{buildroot}%{_tmpfilesdir}/%{name}.conf
sed -i 's|/var/run|%{_rundir}|' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_rundir}/%{name}
for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux
install -d %{buildroot}%{_datarootdir}/logwatch/scripts/services/
install -d %{buildroot}%{_datarootdir}/logwatch/default.conf/services/
install -p -m 644 contrib/logwatch/%{name} %{buildroot}%{_datarootdir}/logwatch/scripts/services/
install -p -m 644 contrib/logwatch/%{name}-journald.conf %{buildroot}%{_datarootdir}/logwatch/default.conf/services/%{name}.conf
%{__unzip} -d %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/ %{SOURCE60}
pushd %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/
./cache_update.sh
popd
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/cache_update.sh
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/.htaccess
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/readme.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog_carddavmate.txt
%{__rm} %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/changelog_caldavzap.txt
%{__rm} -rf %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/auth/
%{__rm} -rf %{buildroot}%{python3_sitelib}/%{name}/web/internal_data/infcloud/misc/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONPATH
echo "Check whether 'radicale' is at least able to display online help"
%{buildroot}%{_libexecdir}/%{name}/%{radicale_name} --help >/dev/null
if [ $? -eq 0 ]; then
  echo "Check whether 'radicale' is at least able to display online help - SUCCESSFUL"
else
  exit 1
fi
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
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/collection-root
rm -rf %{buildroot}%{_sharedstatedir}/%{name}/.Radicale.lock
%pre -n %{radicale_package_name}

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

%post -n %{radicale_package_name}-httpd

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
%files
%files -n radicale3 -f %{oreon_filedir}/radicale3.list
%files -n python3-radicale3 -f %{oreon_filedir}/python3-radicale3.list
%files -n radicale3-httpd -f %{oreon_filedir}/radicale3-httpd.list
%files -n radicale3-selinux -f %{oreon_filedir}/radicale3-selinux.list
%files -n radicale3-logwatch -f %{oreon_filedir}/radicale3-logwatch.list
%files -n radicale3-InfCloud -f %{oreon_filedir}/radicale3-InfCloud.list
%files -n radicale3-InfCloud-fontware -f %{oreon_filedir}/radicale3-InfCloud-fontware.list

%changelog

%autochangelog
