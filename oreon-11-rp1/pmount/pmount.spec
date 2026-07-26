%global source0_hash db38fc290b710e8e9e9d442da2fb627d41e13b3ee80326c15cc2595ba00ea036

%global _hardened_build 1
%define download_dir 3310

Name:           pmount
Version:        0.9.23
Release:        35%{?dist}
Summary:        Enable normal user mount

# realpath.c is GPLv2+. Others are GPL+;
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pmount.alioth.debian.org/
# BEWARE: The number in the url determines the content, ahs to be updated each time.
Source0:        http://alioth.debian.org/frs/download.php/%{download_dir}/%{name}-%{version}.tar.bz2
# don't set the setuid bits during make install
Patch0:         pmount-0.9.17-nosetuid.patch
# Add exfat support
# https://bugs.launchpad.net/ubuntu/+source/pmount/+bug/1524523
Patch1:         pmount.exfat.patch
Patch2:         pmount-c99.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  e2fsprogs-devel
BuildRequires:  libblkid-devel

# ntfs-3g may be used too, it is considered optional, will be used if installed.
Requires:       cryptsetup
Requires:       /bin/mount

%description
pmount  ("policy mount") is a wrapper around the standard mount program
which permits normal users to mount removable devices without a  
matching /etc/fstab entry.

Be warned that pmount is installed setuid root.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
# mount, umount, cryptsetup and ntfs-3g paths are right and don't use rpm 
# macros, so the corresponding configure options are not used. /media/ is
# also rightly used.
%configure \
  --enable-hal=no \
  --with-lock-dir=%{_localstatedir}/lock/pmount \
  --with-whitelist=%{_sysconfdir}/pmount.allow

%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.devel COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
%{_mandir}/man1/p*mount*.1*

%changelog
%autochangelog
