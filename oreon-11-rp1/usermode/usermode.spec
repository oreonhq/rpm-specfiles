%global source0_hash e7f58712b12175965b3a21522052863a061f3f1a888df3ffbe713b434f80254f

# Add `--without gtk' option (enable gtk by default):
# No GTK 2 in RHEL 10
%if 0%{?rhel} > 9
%bcond_with gtk
%else
%bcond_without gtk
%endif

Summary: Tools for certain user account management tasks
Name: usermode
Version: 1.114
Release: 16%{?dist}
License: GPL-2.0-or-later
URL: https://pagure.io/%{name}/
Source:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.xz
Source1: config-util
Patch1: fix-sast.patch
Requires: pam, passwd, util-linux
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/IJFYI5Q2BYZKIGDFS2WLOBDUSEGWHIKV/
BuildRequires: make
BuildRequires: gcc
BuildRequires: gettext, glib2-devel, intltool
%if %{with gtk}
BuildRequires: desktop-file-utils, gtk2-devel, startup-notification-devel, libSM-devel
%endif
BuildRequires: libblkid-devel, libselinux-devel, libuser-devel
BuildRequires: pam-devel, perl-XML-Parser
BuildRequires: util-linux

%if %{with gtk}
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
# make userformat symlink to usermount
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

%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS README
%attr(4711,root,root) /%{_sbindir}/userhelper
%{_bindir}/consolehelper
%{_mandir}/man8/userhelper.8*
%{_mandir}/man8/consolehelper.8*
%dir /etc/security/console.apps
%config(noreplace) /etc/security/console.apps/config-util

%if %{with gtk}
%files gtk
%{_bindir}/usermount
%{_mandir}/man1/usermount.1*
%{_bindir}/userformat
%{_mandir}/man1/userformat.1*
%{_bindir}/userinfo
%{_mandir}/man1/userinfo.1*
%{_bindir}/userpasswd
%{_mandir}/man1/userpasswd.1*
%{_bindir}/consolehelper-gtk
%{_mandir}/man8/consolehelper-gtk.8*
%{_bindir}/pam-panel-icon
%{_mandir}/man1/pam-panel-icon.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.114-16
- Prepare for Oreon 11 (RP1)
