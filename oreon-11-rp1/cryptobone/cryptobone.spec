%global source0_hash c4e727be58b4602f10a2b0224f314e0b397844e3be67c55d504a5832a4f109ed

%global cryptobonedir %{_prefix}/lib/%{name}
%global _hardened_build 1

Name:       cryptobone
Version:    2.0   
Release:    5%{?dist}
Summary:    Secure Communication Under Your Control      

License:    BSD-3-Clause and Sleepycat and OpenSSL
URL:        https://crypto-bone.com      
Source0:    https://crypto-bone.com/release/source/cryptobone-%{version}.tar.gz       
Source1:    https://crypto-bone.com/release/source/cryptobone-%{version}.tar.gz.asc
Source2:    gpgkey-3274CB29956498038A9C874BFBF6E2C28E9C98DD.asc

ExclusiveArch: x86_64 ppc64le aarch64 riscv64

BuildRequires: libbsd-devel
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: desktop-file-utils
BuildRequires: systemd
BuildRequires: make
BuildRequires: libmd-devel
BuildRequires: cryptlib
BuildRequires: cryptlib-devel

Requires: cryptlib
Requires: cryptlib-python3
Requires: systemd
Requires: bash    
Requires: python3
Requires: python3-tkinter
Requires: openssh-askpass
Requires: openssl
Requires: coreutils
Requires: rng-tools
Requires: socat
Requires: cryptsetup
Requires: openssh
Requires: polkit
Requires: tar

%description
The Crypto Bone is a secure messaging system that makes sure a user's
email is always encrypted without burdening the user with the message
key management. Based on a GUI and a separate daemon, both ease-of-use
and security are assured by a novel approach to encryption key management.

While the message keys are secured by a daemon running on the Linux machine,
additional protection can be achieved by using an external device for storing
encryption keys. This external device can be another Linux computer dedicated
to this task or a Beagle Bone or a Raspberry Pi.  (https://crypto-bone.com)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

KEYRING=$(echo %{SOURCE2})
KEYRING=${KEYRING%%.asc}.gpg
mkdir -p .gnupg
gpg2 --homedir .gnupg --no-default-keyring --quiet --yes --output $KEYRING --dearmor  %{SOURCE2}
gpg2 --homedir .gnupg --no-default-keyring --keyring $KEYRING --verify %{SOURCE1} %{SOURCE0}

%setup 

%build

echo OPTFLAGS: %{optflags}
make %{?_smp_mflags} ADDFLAGS="%{optflags}"

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/cryptobone.png %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/cryptobone-safewebdrop.png %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/logo-cryptobone.png %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/logo-cryptobone-safewebdrop.png %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/external-cryptobone-admin.png %{buildroot}%{_datadir}/icons/default
cp %{buildroot}%{cryptobonedir}/GUI/question-mark.png %{buildroot}%{_datadir}/icons/default
desktop-file-install --dir %{buildroot}%{_datadir}/applications -m 644 %{buildroot}%{cryptobonedir}/GUI/cryptobone2.desktop
desktop-file-install --dir %{buildroot}%{_datadir}/applications -m 644 %{buildroot}%{cryptobonedir}/GUI/external-cryptobone-admin.desktop

%post
# this script is run after the packet's installation 
if [ $1 -eq 1 ] ; then
     # installation only, not running after update
     if [ -x /usr/sbin/semodule ]; then
          # only if SELinux is installed, prepare cryptobone.pp
          /usr/sbin/semodule -i /usr/lib/cryptobone/selinux/cryptobone.pp
          /usr/sbin/semodule -e cryptobone
     fi
fi
/bin/touch --no-create %{_datadir}/icons/default &>/dev/null || :

%pretrans
# this is run before anything else is done
# store the header if it exists already
if [ -r %{cryptobonedir}/safewebdrop.header ] ; then
     /usr/bin/cp %{cryptobonedir}/safewebdrop.header %{cryptobonedir}/header.backup
fi

%preun
# this script is run before the package is removed
if [ $1 -eq 0 ] ; then
     # removal only, not running before update
     systemctl stop cryptoboned
     systemctl disable cryptoboned
     systemctl stop cryptoboneexternd
     systemctl disable cryptoboneexternd
     systemctl disable cryptobone-fetch.timer
     systemctl stop cryptobone-fetch.timer
     umount %{cryptobonedir}/keys 2> /dev/null
     rm -f /etc/sudoers.d/cbcontrol
     if [ -f %{cryptobonedir}/bootswitch ] ; then
          chattr -i %{cryptobonedir}/bootswitch
     fi
     rm -rf /dev/shm/RAM 2>/dev/null
     rm -rf /dev/shm/EXRAM 2>/dev/null
     /usr/sbin/userdel cryptobone
     # delete all config files in main cryptobone directory
     rm -rf %{cryptobonedir}/keys/* 2> /dev/null
     rm -rf %{cryptobonedir}/cryptobone/* 2> /dev/null
     rm -f %{cryptobonedir}/database* 2> /dev/null
     rm -f %{cryptobonedir}/cbb.config 2> /dev/null
     rm -f %{cryptobonedir}/bootswitch 2> /dev/null
     rm -f %{cryptobonedir}/keys.tgz 2> /dev/null
     rm -f %{cryptobonedir}/masterkey 2> /dev/null
     rm -f %{cryptobonedir}/pinghost 2> /dev/null
fi

%postun
# this script is run after the package is removed
if [ $1 -eq 0 ] ; then
     # just in case!
     rm -rf %{cryptobonedir} 2> /dev/null > /dev/null
     /bin/touch --no-create %{_datadir}/icons/default &>/dev/null
     /usr/bin/gtk-update-icon-cache %{_datadir}/icons/default &>/dev/null  || :
     if [ -x /usr/sbin/semodule ]; then
          semodule -r cryptobone
     fi
fi

%posttrans
# this is run after everything is done
# restore the header
if [ -r %{cryptobonedir}/header.backup ] ; then
     /usr/bin/cp %{cryptobonedir}/header.backup %{cryptobonedir}/safewebdrop.header
fi

/usr/bin/gtk-update-icon-cache %{_datadir}/icons/default &>/dev/null || :
if grep cryptobone /etc/passwd >/dev/null 2>/dev/null; then
     # update permissions on cryptobone's home directory and shell
     chown cryptobone %{cryptobonedir} %{cryptobonedir}/ext
     chown cryptobone %{cryptobonedir}/ext/cryptoboneshell
fi

%files
%{_unitdir}/cryptoboned.service
%{_unitdir}/cryptobone-dbinit.service
%{_unitdir}/cryptoboneexternd.service
%{_unitdir}/cryptobone-fetch.service
%{_unitdir}/cryptobone-fetch.timer
%{_bindir}/activate-cryptobone
%{_bindir}/cryptobone2
%{_bindir}/external-cryptobone
%{_bindir}/external-cryptobone-admin

# The directory %%{cryptobonedir} contains security-critical files that need to be
# protected from being accessed by non-root users. In addition to restricting the
# main cryptobone directory to root-access, certain files will also have 0700 mode
# to ensure that they are protected even if (accidentally) the directory permission
# might be changed. In particular, this is crucial for the keys subdirectory.
%{cryptobonedir}

%{_datadir}/applications/cryptobone2.desktop
%{_datadir}/applications/external-cryptobone-admin.desktop
%{_datadir}/icons/default/cryptobone.png
%{_datadir}/icons/default/logo-cryptobone.png
%{_datadir}/icons/default/cryptobone-safewebdrop.png
%{_datadir}/icons/default/logo-cryptobone-safewebdrop.png
%{_datadir}/icons/default/external-cryptobone-admin.png
%{_datadir}/icons/default/question-mark.png

%{_mandir}/man8/cryptoboned.8.gz
%{_mandir}/man8/cryptobone2.8.gz
%{_mandir}/man8/activate-cryptobone.8.gz
%{_mandir}/man8/external-cryptobone-admin.8.gz
%{_mandir}/man8/external-cryptobone.8.gz
%{_mandir}/man8/cbcontrol.8.gz

%license   %{_datadir}/licenses/%{name}/COPYING
%doc       %{_docdir}/%{name}/README
%doc       %{_docdir}/%{name}/README-cryptlib

%changelog
%autochangelog
