%global source0_hash 3c710ab0da9c69524ea44a2c42eaa106f349c35608a5e72e3e5a303c85d95078
Name:           dionaea
Version:        0.11.0
Summary:        Low interaction honeypot
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            https://dionaea.readthedocs.io/
VCS:            git:https://github.com/DinoTools/dionaea
%global         gituser         DinoTools
%global         gitname         dionaea
%global         commit          4e459f1b672a5b4c1e8335c0bff1b93738019215
%global         gitdate         20210228
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%bcond_without  systemd
%bcond_without     snapshot
%if 0%{?with_snapshot}
Release:        1%{?dist}
Source0:        https://github.com/%{gituser}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%else
Release:        1%{?dist}
%endif
Source1:        %{name}.sysconfig
Source2:        %{name}.initd
Source3:        %{name}.service
Source4:        %{name}.logrotate
Patch3:         dionaea-03_in6_pktinfo.patch
Patch15:        dionaea-15_pyeval_callobject.patch
Patch16:        dionaea-16_cmake_append_flags.patch
Patch17:        dionaea-17_cmake_dirs.patch
Patch18:        dionaea-18_python_regex.patch
Patch19:        dionaea-19_setuptools.patch
Patch20:        dionaea-20_fix_cython3.1_build.patch
%if 0%{?with_systemd}
%endif
Requires:       logrotate
Requires:       python%{python3_pkgversion}-dionaea
%if 0%{?with_systemd}
%{?systemd_requires}
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake3
BuildRequires:  curl-devel
BuildRequires:  flex
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  libemu-devel
BuildRequires:  libev-devel
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsq3-devel
BuildRequires:  libtool
BuildRequires:  loudmouth-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  readline-devel
BuildRequires:  sqlite
BuildRequires:  systemd-units
BuildRequires:  udns-devel
# /oreon:deps
%description
Dionaea is low interaction honeypot. It is meant to be a nepenthes successor,
embedding python as scripting language, using libemu to detect shell-codes,
supporting ipv6 and TLS.

# ============= documentation package ==========================================
%package doc
Summary:        Documentation for the dionaea honeypot package
BuildArch:      noarch
%description doc
This is documentation for the dionaea honeypot package.
Dionaea is low interaction honeypot. It is meant to be a nepenthes successor,
embedding python as scripting language, using libemu to detect shell-codes,
supporting ipv6 and TLS.

# ============= python3 package ================================================
%package -n python%{python3_pkgversion}-%{gitname}
Summary:        Python3 binding for the dionaea honeypot
%{?python_provide:%python_provide python%{python3_pkgversion}-%{gitname}}
Requires:       python%{python3_pkgversion}-bson
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-scapy
Requires:       python%{python3_pkgversion}-sqlalchemy
%description -n python%{python3_pkgversion}-%{gitname}
This is a Python3 library that gives access to dionaea honeypot functionality.

# ============= preparation ====================================================
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?with_snapshot}
# Build from git snapshot
%autosetup -p 1 -n %{gitname}-%{commit} -N
%else
# Build from git release version
%autosetup -p 1 -n %{gitname}-%{version} -N
%endif

%autopatch -p 1

# Unbundle the pyev library and use the system one
# https://github.com/DinoTools/dionaea/issues/169
rm -rf modules/python/pyev

# Fix paths:
# - remove the hardcoded prefix /opt/dionaea
# - move /var/dionaea to /var/lib/dionaea according to Linux FHS
# https://github.com/DinoTools/dionaea/issues/168
# https://github.com/DinoTools/dionaea/issues/256
sed -i -e "s|/opt/dionaea[/]*|/|g; s|/var/dionaea|/var/lib/dionaea|g;" \
    modules/python/util/gnuplotsql.py \
    modules/python/util/readlogsqltree.py \
    doc/source/tips_and_tricks.rst \
    doc/html/index.html \
    doc/source/old/configuration.rst \
    doc/source/old/seagfaults.rst \
    doc/source/old/utils.rst \
    doc/source/run.rst \
    doc/source/tips_and_tricks.rst

# Change var/dionaea to var/lib/dionaea for the location of sip user database
sed -i -e "s|var/dionaea|var/lib/dionaea|g;" \
    modules/python/dionaea/sip/extras.py

# Scripts should run with /usr/bin/python3 shabang and not /usr/bin/env python3 or /bin/python3
# Fedora specific - not reported upstream
sed -i -e 's|#!/bin/python3|#!/usr/bin/python3|g; s|#!/usr/bin/env python3|#!/usr/bin/python3|g;' \
    modules/python/util/readlogsqltree.py \
    modules/python/util/logsql2postgres.py \
    modules/python/util/gnuplotsql.py \
    modules/python/util/updateccs.py

# Create a sysusers.d config file
cat >dionaea.sysusers.conf <<EOF
u dionaea - 'Dionaea honeypot' /home/dionaea -
EOF

# ============= Build ==========================================================
%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%cmake3 \
    -L \
    -DCMAKE_INSTALL_FULL_SYSCONFDIR:PATH=%{_sysconfdir} \
    -DCMAKE_INSTALL_FULL_LIBDIR:PATH=%{_libdir} \
    -DCMAKE_INSTALL_FULL_LOCALSTATEDIR:PATH=%{_localstatedir} \
    -DDIONAEA_PYTHON_SITELIBDIR:PATH=%{python3_sitearch}
%cmake3_build -j1 --verbose --verbose
cd doc
make html
make man
rm -rf build/html/.{doctrees,buildinfo}
cd ..
%install
%cmake3_install
find %{buildroot} '(' -name '*.a' -o -name '*.la' ')' -delete
install -d %{buildroot}%{_mandir}/man1/
install -p -D -m 644 doc/build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mv doc/build/html/ ./html
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%if 0%{?with_systemd}
  mkdir -p %{buildroot}%{_unitdir}
  install -p -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
%else
  mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
  install -p -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
%endif
install -p -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name} || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/binaries || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/bistreams || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/roots/ftp  || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/roots/tftp || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/roots/www  || :
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/roots/upnp || :
touch %{buildroot}%{_sharedstatedir}/%{name}/dionaea.sqlite
touch %{buildroot}%{_sharedstatedir}/%{name}/dionaea_incident.sqlite
touch %{buildroot}%{_sharedstatedir}/%{name}/sipaccounts.sqlite
rm -f %{buildroot}/usr/share/doc/dionaea/LICENSE \
    %{buildroot}/usr/share/doc/dionaea/LICENSE.openssl
install -m0644 -D dionaea.sysusers.conf %{buildroot}%{_sysusersdir}/dionaea.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%if 0%{?with_systemd}
  %systemd_post %{name}.service
%else
  /sbin/chkconfig --add %{name}
%endif
%preun

%if 0%{?with_systemd}
  %systemd_preun %{name}.service
%else
  if [ $1 -eq 0 ] ; then
     /sbin/service %{name} stop >/dev/null 2>&1 || :
     /sbin/chkconfig --del %{name}
  fi
%endif
%postun

%if 0%{?with_systemd}
  %systemd_postun %{name}.service
%else
  if [ $1 -eq 1 ] ; then
     /sbin/service %{name} condrestart >/dev/null 2>&1 || :
  fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n dionaea-doc -f %{oreon_filedir}/dionaea-doc.list
%files -n python3-dionaea -f %{oreon_filedir}/python3-dionaea.list

%changelog

%autochangelog
