%global source0_hash 0c456f6a5c9e47ce6825ac50d467e7a797e14239b2b9a72bfeb2df0100f4af31

Summary: PAM module for use with SSH keys and ssh-agent
Name: pam_ssh
Version: 2.3
Release: 22%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: BSD-2-Clause
URL: http://sourceforge.net/projects/pam-ssh/
Source0: http://downloads.sourceforge.net/pam-ssh/pam_ssh-%{version}.tar.xz
BuildRequires: make
BuildRequires: pam-devel, openssh-clients, openssl-devel, libtool
BuildRequires: systemd-units
Requires: openssh-clients
Conflicts: selinux-policy-targeted < 3.0.8-55
Patch0: pam_ssh-2.3-rundir.patch
Patch1: pam_ssh-2.3-inexistent_directory.patch

%description
This PAM module provides single sign-on behavior for UNIX using SSH keys. 
Users are authenticated by decrypting their SSH private keys with the 
password provided. In the first PAM login session phase, an ssh-agent 
process is started and keys are added. The same agent is used for the
following PAM sessions. In any case the appropriate environment variables
are set in the session phase.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

# re-run autoconf utils to libtoolize properly
autoreconf -f -si

%build
CFLAGS="$RPM_OPT_FLAGS -fcommon -std=gnu99"
%configure  --with-pam-dir=/%{_lib}/security/
make clean

#  only needed symbols should be exported
cat >>pam_ssh.sym <<EOF
pam_sm_acct_mgmt
pam_sm_authenticate
pam_sm_chauthtok
pam_sm_close_session
pam_sm_open_session
pam_sm_setcred
EOF

make %{?_smp_mflags} LDFLAGS='-export-symbols pam_ssh.sym'

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la

install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
cat <<EOF >$RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
D %{_rundir}/pam_ssh 0755 root root -
EOF

install -d -m 755 $RPM_BUILD_ROOT%{_rundir}/pam_ssh

%files
/%{_lib}/security/*.so
%dir %{_rundir}/pam_ssh
%{_tmpfilesdir}/%{name}.conf
%doc AUTHORS NEWS README ChangeLog TODO
%license COPYING
%{_mandir}/*/*

%changelog
%autochangelog
