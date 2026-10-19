%global source0_hash db38fc290b710e8e9e9d442da2fb627d41e13b3ee80326c15cc2595ba00ea036
%global _hardened_build 1
%define download_dir 3310
Name:           pmount
Version:        0.9.23
Release:        1%{?dist}
Summary:        Enable normal user mount
License:        GPL-2.0-or-later
URL:            http://pmount.alioth.debian.org/
Source0:        http://alioth.debian.org/frs/download.php/%{download_dir}/%{name}-%{version}.tar.bz2
Patch0:         pmount-0.9.17-nosetuid.patch
Patch1:         pmount.exfat.patch
Patch2:         pmount-c99.patch
Requires:       cryptsetup
Requires:       /bin/mount
# oreon:deps
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libblkid-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
pmount  ("policy mount") is a wrapper around the standard mount program
which permits normal users to mount removable devices without a  
matching /etc/fstab entry.

Be warned that pmount is installed setuid root.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  --enable-hal=no \
  --with-lock-dir=%{_localstatedir}/lock/pmount \
  --with-whitelist=%{_sysconfdir}/pmount.allow
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
