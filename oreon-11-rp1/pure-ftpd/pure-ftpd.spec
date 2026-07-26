%global source0_hash b3b879468275e0344555458c8e62465dcf525205ecf9ad78c3f208557d0c1947

Name:       pure-ftpd
Version:    1.0.52
Release:    3%{?dist}
Summary:    Lightweight, fast and secure FTP server
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://www.pureftpd.org

Source0:    http://download.pureftpd.org/pub/pure-ftpd/releases/pure-ftpd-%{version}.tar.bz2
Source1:    pure-ftpd.service
Source2:    pure-ftpd.logrotate
Source6:    pure-ftpd.README.SELinux
Source7:    pure-ftpd.pureftpd.te
Source8:    pure-ftpd-with-tls-init.service
Source9:    pure-ftpd-with-tls.service
Patch0:     0001-modify-pam.patch
Patch1:     0002-fedora-specific-config-file.patch

Provides:   ftpserver
BuildRequires: make
BuildRequires:  pam-devel, libcap-devel
BuildRequires:  libxcrypt-devel
%{!?_without_ldap:BuildRequires:  openldap-devel}
%{!?_without_mysql:BuildRequires: mariadb-connector-c-devel}
%{!?_without_pgsql:BuildRequires: libpq-devel}
%{!?_without_tls:BuildRequires: openssl-devel}
BuildRequires: checkpolicy, selinux-policy-devel
BuildRequires: systemd
BuildRequires: git
BuildRequires: gcc
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:   logrotate
%{!?_without_tls:Requires: sscg}

%description
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.
Rebuild switches:
--without ldap     disable ldap support
--without mysql    disable mysql support
--without pgsql    disable postgresql support
--without extauth  disable external authentication
--without tls      disable SSL/TLS

%package    selinux
Summary:    SELinux support for Pure-FTPD
Requires:   %{name} = %{version}
Requires(post): policycoreutils, %{name}
Requires(preun): policycoreutils, %{name}
Requires(postun): policycoreutils

%description selinux
This package adds SELinux enforcement to Pure-FTPD. Install it if you want
Pure-FTPd to be protected in the same way other FTP servers are in Fedora
(e.g. VSFTPd and ProFTPd)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
install -pm 644 %{SOURCE6} README.SELinux
mkdir selinux
cp -p %{SOURCE7} selinux/pureftpd.te

%build
%configure  \
            --sysconfdir=%{_sysconfdir}/%{name} \
            --with-capabilities \
            --with-sendfile \
            --with-paranoidmsg \
            --with-altlog \
            --with-puredb \
            %{!?_without_extauth:--with-extauth} \
            --with-pam \
            --with-cookie \
            --with-throttling \
            --with-ratios \
            --with-quotas \
            --with-ftpwho \
            --with-welcomemsg \
            --with-uploadscript \
            --with-virtualhosts \
            --with-virtualchroot \
            --with-diraliases \
            --with-peruserlimits \
            %{!?_without_ldap:--with-ldap} \
            %{!?_without_mysql:--with-mysql} \
            %{!?_without_pgsql:--with-pgsql} \
            --with-privsep \
            %{!?_without_tls:--with-tls --with-certfile=%{_sysconfdir}/pki/%{name}/%{name}.pem} \
            --with-rfc2640 \
            --without-bonjour \

%make_build

%install
%make_install

install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_localstatedir}/ftp
%{!?_without_tls:install -d -m 700 $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}}

# Conf
install -p -m 644 pure-ftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-ldap.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-pgsql.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

# Man
install -p -m 644 man/pure-ftpd.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-ftpwho.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-mrtginfo.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-uploadscript.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-pw.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-pwconvert.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-statsdecode.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-quotacheck.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-authd.8 $RPM_BUILD_ROOT%{_mandir}/man8

# Systemd services
%if 0%{!?_without_tls:1}
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd-init.service
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd.service
%else
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd.service
%endif

# Pam 
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m 644 pam/pure-ftpd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/

# Logrotate
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

# SELinux support
pushd selinux
echo "%{_sbindir}/pure-ftpd    system_u:object_r:ftpd_exec_t:s0" > pureftpd.fc
echo '%{_localstatedir}/log/pureftpd.log    system_u:object_r:xferlog_t:s0' >> pureftpd.fc
touch pureftpd.if
make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D pureftpd.pp $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{name}/pureftpd.pp
popd

# Remove unnecessary docs
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/README.MacOS-X

%post
%systemd_post pure-ftpd.service

%preun
%systemd_preun pure-ftpd.service

%postun
%systemd_postun_with_restart pure-ftpd.service

%post selinux
if [ "$1" -le "1" ]; then # Fist install
    semodule -i %{_datadir}/selinux/packages/%{name}/pureftpd.pp 2>/dev/null || :
    fixfiles -R pure-ftpd restore || :
    /bin/systemctl condrestart pure-ftpd > /dev/null 2>&1  || :
fi

%preun selinux
if [ "$1" -lt "1" ]; then # Final removal
    semodule -r pureftpd 2>/dev/null || :
    fixfiles -R pure-ftpd restore || :
    /bin/systemctl condrestart pure-ftpd > /dev/null 2>&1  || :
fi

%postun selinux
if [ "$1" -ge "1" ]; then # Upgrade
    # Replaces the module if it is already loaded
    semodule -i %{_datadir}/selinux/packages/%{name}/pureftpd.pp 2>/dev/null || :
    # no need to restart the daemon
fi

%files
%doc FAQ THANKS AUTHORS HISTORY NEWS
%doc README README.Authentication-Modules README.Configuration-File
%doc README.Donations README.LDAP README.MySQL README.SELinux
%doc README.PGSQL README.TLS README.Virtual-Users
%doc pureftpd.schema
%doc %{_docdir}/%{name}/*.conf
%{_bindir}/pure-*
%{_sbindir}/pure-*
%if 0%{!?_without_tls:1}
%{_unitdir}/pure-ftpd-init.service
%{_unitdir}/pure-ftpd.service
%else
%{_unitdir}/pure-ftpd.service
%endif
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{!?_without_tls:%{_sysconfdir}/pki/%{name}}
%{_mandir}/man8/*
%dir /var/ftp/

%files selinux
%doc README.SELinux
%{_datadir}/selinux/packages/%{name}/pureftpd.pp

%changelog
%autochangelog
