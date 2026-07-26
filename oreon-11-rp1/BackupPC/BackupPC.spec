%global source0_hash 8bc04cd513d47629508bd2fd6f455ced38316974913638e971f44e37786c6365

%global _hardened_build 1

# tmpfiles.d & systemd not supported in RHEL < 7
%if 0%{?fedora} || 0%{?rhel} >= 7
%global _with_tmpfilesd 1
%global _with_systemd 1
%endif

%global _updatedb_conf /etc/updatedb.conf

Name:           BackupPC
Version:        4.4.0
Release:        22%{?dist}
Summary:        High-performance backup system

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://backuppc.github.io/backuppc/index.html
Source0:        https://github.com/backuppc/backuppc/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        BackupPC.htaccess
Source2:        BackupPC.logrotate
Source3:        README.setup
#A C wrapper to use since perl-suidperl is no longer provided
Source4:        BackupPC_Admin.c
Source5:        backuppc.service
Source6:        BackupPC.tmpfiles
Source7:        README.RHEL
Source8:        apache.users

Patch0:         BackupPC-4.1.3-docfix.patch
# Fixes https://bugzilla.redhat.com/show_bug.cgi?id=2091514
Patch1:         https://github.com/backuppc/backuppc/commit/2c9270b9b849b2c86ae6301dd722c97757bc9256.patch

BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl(BackupPC::XS) >= 0.53
BuildRequires:  perl(CGI)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Listing)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
%if 0%{?_with_systemd}
BuildRequires:  systemd
%endif

# Unbundled libraries
Requires:       perl(Net::FTP::AutoReconnect)
Requires:       perl(Net::FTP::RetrHandle)

Requires:       bzip2
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       webserver
Recommends:     httpd
%else
Requires:       httpd
%endif
Requires:       iputils
Requires:       openssh-clients
%if ! 0%{?el6}
Requires:       par2cmdline
%endif
Requires:       rrdtool
Requires:       rsync-bpc >= 3.0.9.6
Requires:       perl(BackupPC::XS) >= 0.53
Requires:       perl-Time-modules
Requires:       samba-client
Requires:       %{_sbindir}/sendmail

%if 0%{?_with_systemd}
Requires(post): shadow-utils
%{?systemd_requires}
%else
Requires(preun): initscripts chkconfig
Requires(post): initscripts chkconfig shadow-utils
Requires(postun): initscripts
%endif

Requires:       policycoreutils
BuildRequires:  selinux-policy-devel checkpolicy
BuildRequires: make
Provides:       backuppc = %{version}-%{release}

%description
BackupPC is a high-performance, enterprise-grade system for backing up Linux
and WinXX and Mac OS X PCs and laptops to a server's disk. BackupPC is highly
configurable and easy to install and maintain.

NOTE: Proper configuration is required after install, see README.setup for more
information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

for f in ChangeLog; do
  iconv -f ISO-8859-1 -t UTF-8 $f > $f.utf && mv $f.utf $f
done

cp %{SOURCE3} .
cp %{SOURCE7} .
cp %{SOURCE4} .

mkdir selinux
pushd selinux

cat >%{name}.te <<EOF
policy_module(%{name},0.0.6)
require {
        type httpd_t, var_lib_t, var_log_t;
        class sock_file { write };
        type unconfined_service_t;
        class unix_stream_socket { connectto };
        type ssh_exec_t, ping_exec_t, sendmail_exec_t;
        class file { getattr };
        type var_run_t;
        class sock_file { getattr };
        type httpd_log_t;
        class file { open };
        class dir { read };
}

allow httpd_t var_run_t:sock_file write;
allow httpd_t var_lib_t:file write;
allow httpd_t unconfined_service_t:unix_stream_socket connectto;
allow httpd_t ping_exec_t:file getattr;
allow httpd_t sendmail_exec_t:file getattr;
allow httpd_t ssh_exec_t:file getattr;
allow httpd_t var_run_t:sock_file getattr;
allow httpd_t httpd_log_t:file open;
allow httpd_t httpd_log_t:dir read;
EOF

cat >%{name}.fc <<EOF
%{_sysconfdir}/%{name}(/.*)?            gen_context(system_u:object_r:httpd_sys_script_rw_t,s0)
%{_sysconfdir}/%{name}/LOCK             gen_context(system_u:object_r:httpd_lock_t,s0)
%{_localstatedir}/run/%{name}(/.*)?     gen_context(system_u:object_r:var_run_t,s0)
%{_localstatedir}/lib/%{name}(/.*)?     gen_context(system_u:object_r:httpd_var_lib_t,s0)
%{_localstatedir}/log/%{name}(/.*)?     gen_context(system_u:object_r:httpd_log_t,s0)
EOF
popd

# attempt to unbundle as much as possible
for m in Net/FTP; do
  rm -rf lib/$m
  sed -i "\@lib/$m@d" configure.pl 
done

# Create a sysusers.d config file
cat >backuppc.sysusers.conf <<EOF
u backuppc - - %{_localstatedir}/lib/%{name} -
EOF

%build
# Build C wrapper
gcc -o BackupPC_Admin BackupPC_Admin.c %{optflags}

# SElinux 
pushd selinux
make -f %{_datadir}/selinux/devel/Makefile
popd

%install
%{__perl} configure.pl \
        --batch \
        --backuppc-user=backuppc \
        --dest-dir %{buildroot} \
        --config-dir %{_sysconfdir}/%{name}/ \
        --config-override CgiURL=\"http://localhost/%{name}\" \
        --config-override ClientNameAlias=undef \
        --config-override NmbLookupPath=\"%{_bindir}/nmblookup\" \
        --config-override ParPath=\"%{_bindir}/par2\" \
        --config-override PingPath=\"%{_bindir}/ping\" \
        --config-override Ping6Path=\"%{_sbindir}/ping6\" \
        --config-override RrdToolPath=\"%{_bindir}/rrdtool\" \
        --config-override RsyncBackupPCPath=\"%{_bindir}/rsync_bpc\" \
        --config-override RsyncClientPath=\"%{_bindir}/rsync\" \
        --config-override SendmailPath=\"%{_sbindir}/sendmail\" \
        --config-override SmbClientPath=\"%{_bindir}/smbclient\" \
        --config-override SshPath=\"%{_bindir}/ssh\" \
        --config-override TarClientPath=\"%{_bindir}/gtar\" \
        --config-override XferMethod=\"rsync\" \
        --cgi-dir %{_libexecdir}/%{name} \
        --data-dir %{_localstatedir}/lib/%{name}/ \
        --hostname localhost \
        --html-dir %{_datadir}/%{name}/html/ \
        --html-dir-url /%{name}/images \
        --install-dir %{_datadir}/%{name} \
        --log-dir %{_localstatedir}/log/%{name} \
        --no-set-perms \
        --uid-ignore

# Make bin files executable
chmod +x %{buildroot}%{_datadir}/%{name}/bin/*

%if 0%{?_with_tmpfilesd}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%endif

%if 0%{?_with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/
%else
mkdir -p %{buildroot}%{_initrddir}
install -p -m 0755 systemd/src/init.d/linux-backuppc %{buildroot}%{_initrddir}/backuppc
%endif

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/pc

install -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -m 0644 %{SOURCE8} \
    %{buildroot}%{_sysconfdir}/%{name}/

# perl-suidperl is no longer avaialable, we use a C wrapper
mkdir -p %{buildroot}%{_datadir}/%{name}/sbin
mv %{buildroot}%{_libexecdir}/%{name}/BackupPC_Admin \
   %{buildroot}%{_datadir}/%{name}/sbin/BackupPC_Admin
install -pm 0755 BackupPC_Admin %{buildroot}%{_libexecdir}/%{name}/

# SElinux 
mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 0644 selinux/%{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/%{name}.pp

install -m0644 -D backuppc.sysusers.conf %{buildroot}%{_sysusersdir}/backuppc.conf

%preun
%if 0%{?_with_systemd}
%systemd_preun backuppc.service
%else
if [ $1 = 0 ]; then
  # Package removal, not upgrade
  service backuppc stop > /dev/null 2>&1 || :
  chkconfig --del backuppc || :
fi
%endif

%post
(
     # Install/update Selinux policy
     semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp
     # files created by app
     restorecon -R %{_sysconfdir}/%{name}
     restorecon -R %{_localstatedir}/log/%{name}
) &>/dev/null

%if 0%{?_with_systemd}
%systemd_post backuppc.service
%else
if [ $1 -eq 1 ]; then
  # initial installation
  chkconfig --add backuppc || :
fi
%{_sbindir}/usermod -a -G backuppc apache || :
%endif

# add BackupPC backup directories to PRUNEPATHS in locate database
if [ -w %{_updatedb_conf} ]; then
  grep ^PRUNEPATHS %{_updatedb_conf} | grep %{_localstatedir}/lib/%{name} > /dev/null
  if [ $? -eq 1 ]; then
    sed -i '\@PRUNEPATHS@s@"$@ '%{_localstatedir}/lib/%{name}'"@' %{_updatedb_conf}
  fi
fi
:

%postun
# clear out any BackupPC configuration in apache
service httpd condrestart > /dev/null 2>&1 || :

if [ $1 -eq 0 ]; then
  # uninstall
  # Remove the SElinux policy.
  semodule -r %{name} &> /dev/null || :
  # remove BackupPC backup directories from PRUNEPATHS in locate database
  if [ -w %{_updatedb_conf} ]; then
    sed -i '\@PRUNEPATHS@s@[ ]*'%{_localstatedir}/lib/%{name}'@@' %{_updatedb_conf} || :
  fi
fi

%systemd_postun_with_restart backuppc.service

%files
%doc README.md README.setup README.RHEL ChangeLog doc/*
%license LICENSE
%dir %attr(-,backuppc,backuppc) %{_localstatedir}/log/%{name} 
%dir %attr(-,backuppc,apache) %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %attr(-,backuppc,apache) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/sbin
%{_datadir}/%{name}/[^s]*
%attr(750,backuppc,apache) %{_datadir}/%{name}/sbin/BackupPC_Admin

%if 0%{?_with_tmpfilesd}
%{_tmpfilesdir}/%{name}.conf
%else
%dir %attr(0775,root,backuppc) %{_localstatedir}/run/%{name} 
%endif

%if 0%{?_with_systemd}
%{_unitdir}/backuppc.service
%else
%attr(0755,root,root) %{_initrddir}/backuppc
%endif

%attr(4750,backuppc,apache) %{_libexecdir}/%{name}/BackupPC_Admin
%attr(-,backuppc,root) %{_localstatedir}/lib/%{name}/
%{_datadir}/selinux/packages/%{name}/%{name}.pp
%{_sysusersdir}/backuppc.conf

%changelog
%autochangelog
