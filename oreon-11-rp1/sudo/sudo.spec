%global source0_hash 4a38a1ab3adb1199257edc2a7c4a2bd714665eb605b04368843b06dada2cfcfb
%global extraver p2
Summary:        Allows restricted root access for specified users
Name: sudo
Version: 1.9.17
Release:        1%{?dist}
License: ISC
URL: https://www.sudo.ws
Source0:        https://www.sudo.ws/dist/sudo-1.9.17p2.tar.gz
Source1: sudoers
Requires: pam
Recommends: system-default-editor
Recommends: %{name}-python-plugin%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  groff
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Sudo (superuser do) allows a system administrator to give certain
users (or groups of users) the ability to run some (or all) commands
as root while logging all commands and arguments. Sudo operates on a
per-command basis.  It is not a replacement for the shell.  Features
include: the ability to restrict what commands a user may run on a
per-host basis, copious logging of each command (providing a clear
audit trail of who did what), a configurable timeout of the sudo
command, and the ability to use the same configuration file (sudoers)
on many different machines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains header files developing sudo
plugins that use %{name}.

%package        logsrvd
Summary:        High-performance log server for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  openssl-devel
%description    logsrvd
%{name}-logsrvd is a high-performance log server that accepts event and I/O logs from sudo.
It can be used to implement centralized logging of sudo logs.

%package        python-plugin
Summary:        Python plugin for %{name}
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python3-devel
%description    python-plugin
%{name}-python-plugin allows using sudo plugins written in Python.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{?extraver}

%build

rm -rf zlib/
%configure \
        --prefix=%{_prefix} \
        --sbindir=%{_sbindir} \
        --libdir=%{_libdir} \
        --docdir=%{_pkgdocdir} \
        --enable-tmpfiles.d=%{_tmpfilesdir} \
        --enable-openssl \
        --disable-root-mailer \
        --disable-intercept \
        --with-logging=syslog \
        --with-logfac=authpriv \
        --with-pam \
        --with-pam-login \
        --with-editor=%{_bindir}/nano:%{_bindir}/vim:%{_bindir}/vi \
        --with-env-editor \
        --with-ignore-dot \
        --with-tty-tickets \
        --with-ldap \
        --with-selinux \
        --with-sendmail=/usr/sbin/sendmail \
        --with-passprompt="[sudo] password for %p: " \
        --enable-python \
        --enable-zlib=system \
        --with-linux-audit \
        --with-sssd
%make_build
%check

%make_build check
%install
%make_install install_uid=`id -u` install_gid=`id -g` sudoers_uid=`id -u` sudoers_gid=`id -g`
chmod 755 $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_sbindir}/*
install -p -d -m 700 $RPM_BUILD_ROOT/var/db/sudo
install -p -d -m 700 $RPM_BUILD_ROOT/var/db/sudo/lectured
install -p -d -m 750 $RPM_BUILD_ROOT/etc/sudoers.d
install -p -c -m 0440 %{SOURCE1} $RPM_BUILD_ROOT/etc/sudoers
mkdir -p $RPM_BUILD_ROOT/etc/dnf/protected.d/
echo "sudo" >$RPM_BUILD_ROOT/etc/dnf/protected.d/sudo.conf
mkdir -p $RPM_BUILD_ROOT/usr/share/dnf5/libdnf.conf.d/
cat >$RPM_BUILD_ROOT/usr/share/dnf5/libdnf.conf.d/protect-sudo.conf <<EOF
[main]
protected_packages = sudo
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/sudo/*.so # for stripping, reset in %%files
rm -rf $RPM_BUILD_ROOT%{_pkgdocdir}/LICENSE
rm -rf $RPM_BUILD_ROOT%{_datadir}/examples/sudo
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/sudoers.dist
%find_lang sudo
%find_lang sudoers
cat sudo.lang sudoers.lang > sudo_all.lang
rm sudo.lang sudoers.lang
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/sudo << EOF
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF
cat > $RPM_BUILD_ROOT/etc/pam.d/sudo-i << EOF
auth       include      sudo
account    include      sudo
password   include      sudo
session    optional     pam_keyinit.so force revoke
session    include      sudo
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sudo-devel -f %{oreon_filedir}/sudo-devel.list
%files -n sudo-logsrvd -f %{oreon_filedir}/sudo-logsrvd.list
%files -n sudo-python-plugin -f %{oreon_filedir}/sudo-python-plugin.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.17-1
- Prepare for Oreon 11 (RP1)
