%global source0_hash e7f58712b12175965b3a21522052863a061f3f1a888df3ffbe713b434f80254f
%bcond_without gtk
Summary:        Tools for certain user account management tasks
Name: usermode
Version: 1.114
Release:        16%{?dist}
License: GPL-2.0-or-later
URL: https://pagure.io/%{name}/
Source0:        https://deb.debian.org/debian/pool/main/u/usermode/usermode_%{version}.orig.tar.xz#/usermode-%{version}.tar.xz
Source1: config-util
Patch1: fix-sast.patch
Requires: pam, passwd, util-linux
%if %{with gtk}
%endif
%if %{with gtk}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libSM-devel
BuildRequires:  libblkid-devel
BuildRequires:  libselinux-devel
BuildRequires:  libuser-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  startup-notification-devel
BuildRequires:  util-linux
# /oreon:deps
%package gtk
Summary: Graphical tools for certain user account management tasks
Requires: %{name} = %{version}-%{release}
%endif
%global _hardened_build 1
%description
The usermode package contains the userhelper program, which can be
used to allow configured programs to be run with superuser privileges
by ordinary users.

%if %{with gtk}
%description gtk
The usermode-gtk package contains several graphical tools for users:
userinfo, usermount and userpasswd.  Userinfo allows users to change
their finger information.  Usermount lets users mount, unmount, and
format file systems.  Userpasswd allows users to change their
passwords.

Install the usermode-gtk package if you would like to provide users with
graphical tools for certain account management tasks.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 1 -p 1

%build

%configure --with-selinux --without-fexecve %{!?with_gtk:--without-gtk}
%make_build
%install
%make_install
%if %{with gtk}
ln -sf usermount $RPM_BUILD_ROOT%{_bindir}/userformat
ln -s usermount.1 $RPM_BUILD_ROOT%{_mandir}/man1/userformat.1
%endif
mkdir -p $RPM_BUILD_ROOT/etc/security/console.apps
install -p -m 644 %{SOURCE1} \
	$RPM_BUILD_ROOT/etc/security/console.apps/config-util
%if %{with gtk}
for i in redhat-userinfo.desktop redhat-userpasswd.desktop \
	redhat-usermount.desktop; do
	echo 'NotShowIn=GNOME;KDE;' >>$RPM_BUILD_ROOT%{_datadir}/applications/$i
	desktop-file-install --vendor redhat --delete-original \
		--dir $RPM_BUILD_ROOT%{_datadir}/applications \
		$RPM_BUILD_ROOT%{_datadir}/applications/$i
done
%endif
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n usermode-gtk -f %{oreon_filedir}/usermode-gtk.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.114-16
- Prepare for Oreon 11 (RP1)
