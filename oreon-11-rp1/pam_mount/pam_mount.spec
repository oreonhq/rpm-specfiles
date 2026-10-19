%global source1_hash d7e6791bc951442e4cee33b27d600c026774c842e47d50d46e498b9799b6d1cc
%global source0_hash 5426207a485680f8e1764ba405bb38c39a4e0c8306bc8271910f1b819a336ced
Name:           pam_mount
Version:        2.22
Release:        1%{?dist}
Summary:        A PAM module that can mount volumes for a user session
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://inai.de/projects/pam_mount/
Source0:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.xz
Source1:        https://inai.de/files/pam_mount/%{name}-%{version}.tar.asc
Source2:        gpgkey-BCA0C5C309CAC569E74A921CF76EFE5D0C223A8F.asc
Patch0:         pam_mount-2.16-LTINIT.patch
Requires:       libHX%{?_isa} >= 3.12.1
Requires:       hxtools
Requires:       pam%{?_isa}
Requires:       libcryptmount%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cryptsetup-devel
BuildRequires:  gcc
BuildRequires:  gpg
BuildRequires:  libHX-devel
BuildRequires:  libmount-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter
BuildRequires:  xz
# /oreon:deps
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
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package -n libcryptmount
Summary: Library to mount crypto images and handle key files
%description -n libcryptmount
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%package -n libcryptmount-devel
Summary: Development files for libcryptmount
Requires: libcryptmount = %{version}
%description -n libcryptmount-devel
libcryptmount takes care of the many steps involved in making a
crypto image (file) available as a mountable block device, including
supplemental key file decryption, loop device setup and crypto device
setup. It supports pam_mount style plain EHD2/OpenSSL images and LUKS
and transparent use of the OS's crypto layer.
%files -f %{oreon_filedir}/main.list
%files -n libcryptmount -f %{oreon_filedir}/libcryptmount.list
%files -n libcryptmount-devel -f %{oreon_filedir}/libcryptmount-devel.list

%changelog

%autochangelog
