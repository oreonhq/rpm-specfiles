%global source0_hash fd87a207846fa650fd377219adc4b8a8193e55904d8a752c2c3715b4155d8d38
%global _hardened_build 1
%global prefix %{_libdir}/%{name}
%global exec_prefix %{_exec_prefix}/lib/%{name}
Name: heimdal
Version: 7.8.0
Release:        1%{?dist}
Summary:        A Kerberos 5 implementation without export restrictions
License: BSD-2-Clause AND BSD-3-Clause AND HPND-export-US AND HPND-export2-US AND LicenseRef-Fedora-Public-Domain
URL: http://www.heimdal.software/heimdal
Source0:        https://github.com/%{name}/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source3:  %{name}.sysconfig
Source4:  %{name}.sh
Source5:  %{name}.csh
Source9:  krb5.conf.sample
Source10: %{name}.logrotate
Source11: %{name}-bashrc
Source25: %{name}-kdc.conf
Source26: %{name}-kdc.service
Source27: %{name}-ipropd-master.service
Source28: %{name}-ipropd-slave.service
Source29: %{name}-kadmind.service
Source30: %{name}-kpasswdd.service
Source31: %{name}-ipropd-slave-wrapper
Patch1: heimdal-1.6.0-c25f45a-rename-commands.patch
Patch4: heimdal-7.7.0-configure.patch
Patch5: heimdal-7.7.0-58c8ad96-py3.patch
Patch6: heimdal-configure-c99.patch
Patch7: heimdal-7.8.0-1b57b62d-ac272.patch
Patch8: heimdal-7.8.0-e93a1357-slapdtest.patch
Provides: bundled(libtommath) = 0.42.0
# oreon:deps
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  groff-base
BuildRequires:  libcap-ng-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libdb-devel
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openldap-servers
BuildRequires:  pam-devel
BuildRequires:  perl(JSON)
BuildRequires:  python3
BuildRequires:  sqlite-devel
BuildRequires:  systemd-units
BuildRequires:  texinfo
# /oreon:deps
%description
Kerberos 5 is a network authentication and single sign-on system.
Heimdal is a free Kerberos 5 implementation without export restrictions
written from the spec (rfc1510 and successors) including advanced features
like thread safety, IPv6, master-slave replication of Kerberos Key
Distribution Center server and support for ticket delegation (S4U2Self,
S4U2Proxy).
This package can coexist with MIT Kerberos 5 packages. Hesiod is disabled
by default since it is deemed too big a security risk by the packager.

%package    workstation
Summary:    Heimdal kerberos programs for use on workstations
%description workstation
This package contains Heimdal Kerberos 5 programs and utilities for
use on workstations (kinit, klist, kdestroy, kpasswd)

%package server
Summary:  Heimdal kerberos server
Requires: logrotate
Requires(preun): systemd
Requires(postun): systemd
Requires(post): systemd
Provides: heimdal-kdc = %{version}-%{release}
Obsoletes: heimdal-kdc < 1.5
%description server
This package contains the master Heimdal kerberos Key Distribution
Center (KDC), admin interface server (admind) and master-slave
synchronisation daemons. Install this package if you intend to
set up Kerberos server.

%package libs
Summary: Heimdal kerberos shared libraries
Requires(post): info
Requires(preun): info
%description libs
This package contains shared libraries required by several of the other
Heimdal packages.

%package devel
Summary:  Header and other development files for Heimdal kerberos
%description devel
Contains files needed to compile and link software using the Heimdal
kerberos headers/libraries.

%package static
Summary:  Static libraries for Heimdal kerberos
Requires: %{name}-devel = %{version}-%{release}
%description static
Contains files needed to statically link software using the Heimdal
kerberos headers/libraries.

%package path
Summary: Heimdal kerberos PATH manipulation
Requires: %{name}-libs
Requires: setup
%description path
This package prepends the Heimdal binary directory to the beginning of
PATH.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .cmds
%patch -P4 -p1 -b .config
%patch -P5 -p1 -b .2to3
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

for f in lib/*/*.py; do
    sed -i "$f" -re 's,^#!/usr/(local/|)bin/python,#!/usr/bin/python3,'
done

# FIXME check-slapd fails
for f in tests/Makefile.{in,am}; do sed -i $f -re 's, ldap , ,'; done

./autogen.sh

%build

%ifarch i386
%global build_fix "-march=i686"
%else
%global build_fix ""
%endif
autoreconf -ivf
%configure \
        --prefix=%{_prefix} \
        --includedir=%{_includedir}/%{name} \
        --libdir=%{prefix}/lib \
        --enable-static \
        --enable-shared \
        --enable-pthread-support \
        --without-x \
        --without-hesiod \
        --with-ipv6 \
        --enable-kcm \
        --enable-pk-init \
        --with-openldap=%{_prefix} \
        --with-sqlite3=%{_prefix} \
        --with-libedit=%{_prefix} \
        LIBS="-ltermcap" \
        CFLAGS="-fPIC %{optflags} %{build_fix}"
%make_build -C include krb5-types.h
%make_build
%make_build -C doc html
touch po/localefiles
%make_build -C po mo
%check

%make_build -j1 check
%install
%make_install
mkdir -p %{buildroot}%{_unitdir}
pushd %{buildroot}%{_unitdir}
  install -p -D -m 644 %{SOURCE26} heimdal-kdc.service
  install -p -D -m 644 %{SOURCE27} heimdal-ipropd-master.service
  install -p -D -m 644 %{SOURCE28} heimdal-ipropd-slave.service
  install -p -D -m 644 %{SOURCE29} heimdal-kadmind.service
  install -p -D -m 644 %{SOURCE30} heimdal-kpasswdd.service
popd
install -p -D -m 755 %{SOURCE31} %{buildroot}%{_libexecdir}/ipropd-slave-wrapper
install -p -D -m 644 %{SOURCE3}  %{buildroot}%{_sysconfdir}/sysconfig/heimdal
install -p -D -m 644 %{SOURCE4}  %{buildroot}%{_sysconfdir}/profile.d/heimdal.sh
install -p -D -m 644 %{SOURCE5}  %{buildroot}%{_sysconfdir}/profile.d/heimdal.csh
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/logrotate.d/heimdal
mkdir -p %{buildroot}%{_localstatedir}/heimdal/
install -p -D -m 755 %{SOURCE25}  %{buildroot}%{_sysconfdir}/heimdal-kdc.conf
ln -s %{_sysconfdir}/heimdal-kdc.conf %{buildroot}%{_localstatedir}/heimdal/kdc.conf
echo "# see man heimdal-kadmind(8)" > %{buildroot}%{_sysconfdir}/heimdal-kadmind.acl
ln -s %{_sysconfdir}/heimdal-kadmind.acl %{buildroot}%{_localstatedir}/heimdal/kadmind.acl
touch    %{buildroot}%{_sysconfdir}/heimdal-slaves
ln -s %{_sysconfdir}/heimdal-slaves %{buildroot}%{_localstatedir}/heimdal/slaves
install -d -m 700 %{buildroot}%{_localstatedir}/log/heimdal
install -d -m 755 %{buildroot}/%{_pkgdocdir}
install -p -D -m 644 LICENSE    %{buildroot}/%{_pkgdocdir}/LICENSE
install -p -D -m 644 %{SOURCE9} %{buildroot}/%{_pkgdocdir}/krb5.conf.sample
install -p -D -m 644 %{SOURCE11} %{buildroot}/%{_pkgdocdir}/bashrc
rm -rf %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_mandir}/man1/kx.1*
rm -f %{buildroot}%{_mandir}/man1/rxtelnet.1*
rm -f %{buildroot}%{_mandir}/man1/rxterm.1*
rm -f %{buildroot}%{_mandir}/man1/tenletxr.1*
rm -f %{buildroot}%{_mandir}/man1/xnlock.1*
rm -f %{buildroot}%{_mandir}/man8/kxd.8*
rm -rf %{buildroot}%{_mandir}/cat*
find %{buildroot} -type f -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf << EOF
%{prefix}/lib
EOF
mkdir -p %{buildroot}%{exec_prefix}/bin
mkdir -p %{buildroot}%{_mandir}/%{name}/man{1,5,8}
for prog in kadmin kadmind kdestroy kinit klist kpasswd krb5-config ktutil su pagsh compile_et
do
   if [ -e %{buildroot}%{_bindir}/${prog} ]; then
     mv %{buildroot}%{_bindir}/{,%{name}-}${prog}
     ln -s %{_bindir}/%{name}-${prog} %{buildroot}%{exec_prefix}/bin/${prog}
   elif [ -e %{buildroot}%{_sbindir}/${prog} ]; then
     mv %{buildroot}%{_sbindir}/{,%{name}-}${prog}
     ln -s %{_sbindir}/%{name}-${prog} %{buildroot}%{exec_prefix}/bin/${prog}
   elif [ -e %{buildroot}%{_libexecdir}/${prog} ]; then
     mv %{buildroot}%{_libexecdir}/{,%{name}-}${prog}
   fi
   if [ -e %{buildroot}%{_mandir}/man1/${prog}.1 ]; then
     mv %{buildroot}%{_mandir}/man1/{,%{name}-}${prog}.1
   elif [ -e %{buildroot}%{_mandir}/man8/${prog}.8 ]; then
     mv %{buildroot}%{_mandir}/man8/{,%{name}-}${prog}.8
   fi
done
mv %{buildroot}%{_bindir}/{,%{name}-}kswitch
ln -s %{_bindir}/%{name}-kswitch %{buildroot}%{exec_prefix}/bin/kswitch
mv %{buildroot}%{_mandir}/man1/{,%{name}-}kswitch.1
ln -s %{name}-kinit %{buildroot}%{_bindir}/kauth
mv %{buildroot}%{_mandir}/man5/{,%{name}-}krb5.conf.5
rm %{buildroot}%{_mandir}/man5/qop.5
ln -s mech.5.gz %{buildroot}%{_mandir}/man5/qop.5.gz
sha256sum %{buildroot}%{_mandir}/man3/*.3 | sort >man3hash
firsthash="X"; firstname="X"
while read hash path; do
    name="${path##*/}"
    if [ "$hash" != "$firsthash" ]; then
        firsthash="$hash"
        firstname="${path##*/}"
    else
        rm "$path"
        ln -s "$firstname".gz "$path".gz
    fi
done <man3hash
rm man3hash
%find_lang %{name} --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post heimdal-kdc.service
%systemd_post heimdal-ipropd-master.service
%systemd_post heimdal-ipropd-slave.service
%systemd_post heimdal-kadmind.service
%systemd_post heimdal-kpasswdd.service
%preun server

%systemd_preun heimdal-kdc.service
%systemd_preun heimdal-ipropd-master.service
%systemd_preun heimdal-ipropd-slave.service
%systemd_preun heimdal-kadmind.service
%systemd_preun heimdal-kpasswdd.service
%postun server

%systemd_postun_with_restart heimdal-kdc.service
%systemd_postun_with_restart heimdal-ipropd-master.service
%systemd_postun_with_restart heimdal-ipropd-slave.service
%systemd_postun_with_restart heimdal-kadmind.service
%systemd_postun_with_restart heimdal-kpasswdd.service
%files -f %{oreon_filedir}/main.list
%files -n heimdal-workstation -f %{oreon_filedir}/heimdal-workstation.list
%files -n heimdal-server -f %{oreon_filedir}/heimdal-server.list
%files -n heimdal-libs -f %{oreon_filedir}/heimdal-libs.list
%files -n heimdal-devel -f %{oreon_filedir}/heimdal-devel.list
%files -n heimdal-static -f %{oreon_filedir}/heimdal-static.list
%files -n heimdal-path -f %{oreon_filedir}/heimdal-path.list

%changelog

%autochangelog
