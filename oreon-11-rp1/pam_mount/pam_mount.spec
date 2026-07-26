%global source0_hash 5426207a485680f8e1764ba405bb38c39a4e0c8306bc8271910f1b819a336ced

Name:           pam_mount
Version:        2.20
Release:        5%{?dist}
Summary:        A PAM module that can mount volumes for a user session

# The library and binaries are LGPLv2.1+ with these Exceptions:
# "pmvarrun" and "mount.crypt" programs, especially their .c file are under GPLv2+
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://inai.de/projects/pam_mount/
Source0:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.xz
Source1:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.asc
# GPG key from official website: https://inai.de/about/
Source2:        gpgkey-BCA0C5C309CAC569E74A921CF76EFE5D0C223A8F.asc

# AM_PROG_LIBTOOL is obsolete
Patch0:         pam_mount-2.16-LTINIT.patch

# For source verification with gpgv
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cryptsetup-devel
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  libHX-devel >= 3.12.1
BuildRequires:  libmount-devel >= 2.20
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter
BuildRequires:  xz

Requires:       libHX%{?_isa} >= 3.12.1
Requires:       hxtools
Requires:       pam%{?_isa}
Requires:       libcryptmount%{?_isa} = %{version}-%{release}

%description
This module is aimed at environments with central file servers that a user
wishes to mount on login and unmount on logout, such as (semi-)diskless
stations where many users can logon and where statically mounting the entire
/home from a server is a security risk, or listing all possible volumes in
/etc/fstab is not feasible.

* Users can define their own list of volumes without having to change
  (possibly non-writable) global config files.
* Single sign-on feature - the user needs to type the password just once (at login)
* Transparent mount process
* No stored passwords
* Volumes are unmounted on logout, freeing system resources and not leaving
  data exposed.

The module also supports mounting local filesystems of any kind the normal
mount utility supports, with extra code to make sure certain volumes are set up
properly because often they need more  than just a mount call, such as
encrypted volumes. This includes SMB/CIFS, FUSE, dm-crypt and LUKS.

If  you  intend  to use pam_mount to protect volumes on your computer using an
encrypted filesystem system, please know that there are many other issues you
need to consider in order to protect your data. For example, you probably want
to disable or encrypt your swap partition (the cryptoswap can help you do
this). Do not assume  a  system  is  secure  without  carefully  considering
potential threats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

rm -f %{SOURCE2}.gpg ; gpg --dearmor %{SOURCE2}
xzcat %{SOURCE0} | gpgv --quiet --keyring %{SOURCE2}.gpg %{SOURCE1} -
%setup -q
%patch -P0 -p1 -b.LTINIT
./autogen.sh

%build
%configure                     \
  --with-dtd                   \
  --with-slibdir=%{_libdir}    \
  --with-ssbindir=%{_sbindir}
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libcryptmount.la

%ldconfig_scriptlets

%files
%doc doc/faq.txt doc/options.txt doc/todo.txt
# generated from manpage, no need to package it twice:
#doc/pam_mount.txt
%doc config/pam_mount.conf.xml
%license COPYING LICENSE.GPL2 LICENSE.GPL3 LICENSE.LGPL2 LICENSE.LGPL3
%config(noreplace) %{_sysconfdir}/security/pam_mount.conf.xml
%{_libdir}/security/pam_mount.so
%{_sbindir}/pmvarrun
%{_sbindir}/pmt-ehd
%{_sbindir}/mount.crypt
%{_sbindir}/umount.crypt
%{_sbindir}/mount.crypt_LUKS
%{_sbindir}/umount.crypt_LUKS
%{_sbindir}/mount.crypto_LUKS
%{_sbindir}/umount.crypto_LUKS
%{_mandir}/man5/pam_mount.conf.5*
%{_mandir}/man8/mount.crypt.8*
%{_mandir}/man8/mount.crypt_LUKS.8*
%{_mandir}/man8/mount.crypto_LUKS.8*
%{_mandir}/man8/pam_mount.8*
%{_mandir}/man8/pmt-ehd.8*
%{_mandir}/man8/pmvarrun.8*
%{_mandir}/man8/umount.crypt.8*
%{_mandir}/man8/umount.crypt_LUKS.8*
%{_mandir}/man8/umount.crypto_LUKS.8*
%ghost %{_localstatedir}/run/pam_mount
%dir %{_datadir}/xml/pam_mount/
%dir %{_datadir}/xml/pam_mount/dtd/
%{_datadir}/xml/pam_mount/dtd/pam_mount.conf.xml.dtd

%package -n libcryptmount
Summary: Library to mount crypto images and handle key files
%description -n libcryptmount
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%files -n libcryptmount
%{_libdir}/libcryptmount.so
%{_libdir}/libcryptmount.so.0
%{_libdir}/libcryptmount.so.0.0.0

%package -n libcryptmount-devel
Summary: Development files for libcryptmount
Requires: libcryptmount = %{version}
%description -n libcryptmount-devel
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%files -n libcryptmount-devel
%{_includedir}/libcryptmount.h
%{_libdir}/pkgconfig/libcryptmount.pc

%changelog
%autochangelog
