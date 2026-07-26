%global source0_hash 1346144ef1380266ea1b0434c726311f49823690d8bfca2e2a526eed5dc612cf

%global commit0 bd275a72f85a64eae0f7543603631c5f4891e70a
%global gittag0 v2015.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7}) 

Summary: Helper program for calling chroot(2) as non-root
Name: linux-user-chroot
Version: 2015.1
Release: 24%{?dist}
#VCS: git:git://git.gnome.org/linux-user-chroot
# I used "git archive" 
Source0: https://git.gnome.org/browse/linux-user-chroot/snapshot/linux-user-chroot-%{version}.tar.xz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://git.gnome.org/browse/linux-user-chroot
BuildRequires: autoconf automake libtool
BuildRequires: kernel-headers
BuildRequires: pkgconfig(libseccomp)
BuildRequires: make

%description
A tool made for build systems that run as non-root, offering chroot(2)
and Linux container features to non-root users.
Only install this on systems for which local, authenticated denial of
service attacks are not a serious concern.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --enable-documentation
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%attr(4755,root,root) %{_bindir}/linux-user-chroot
%{_mandir}/man8/*.gz

%changelog
%autochangelog
