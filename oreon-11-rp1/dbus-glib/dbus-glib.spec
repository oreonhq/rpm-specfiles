%global source0_hash none

%global source2_key_fpr DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90

%global expat_version 1.95.5
%global glib2_version 2.40.0
%global dbus_version 1.8

Name:    dbus-glib
Version: 0.112
Release: 13%{?dist}
Summary: GLib bindings for D-Bus

# dbus/dbus-bash-completion-helper.c is GPL-2.0-or-later
# some tests are (LGPL-2.1-or-later OR MIT) AND MIT, but not included in rpm
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:     https://www.freedesktop.org/software/dbus/
#VCS:    git:https://gitlab.freedesktop.org/dbus/dbus-glib.git
Source0:        https://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
Source1:        https://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz.asc
# gpg --keyserver keyring.debian.org --recv-keys 36EC5A6448A4F5EF79BEFE98E05AE1478F814C4F
# gpg --export --export-options export-minimal 0x36EC5A6448A4F5EF79BEFE98E05AE1478F814C4F > gpgkey-36EC5A6448A4F5EF79BEFE98E05AE1478F814C4F.gpg
Source2: gpgkey-36EC5A6448A4F5EF79BEFE98E05AE1478F814C4F.gpg

BuildRequires: pkgconfig(dbus-1) >= %{dbus_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: expat-devel >= %{expat_version}
BuildRequires: /usr/bin/chrpath
BuildRequires: dbus-daemon
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: make

%description

D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package devel
Summary: Libraries and headers for the D-Bus GLib bindings
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel

Headers and static libraries for the D-Bus GLib bindings

%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%set_build_flags
export CFLAGS="$CFLAGS -std=gnu17"
%configure --enable-tests=yes \
	--enable-asserts=yes \
	--disable-gtk-doc

%make_build

%check
%make_build check


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dbus-binding-tool
chrpath --delete $RPM_BUILD_ROOT%{_libexecdir}/dbus-bash-completion-helper

# Scripts that are sourced should not be executable.
chmod -x $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh


%ldconfig_scriptlets

%files
%doc NEWS
%license COPYING
%{_libdir}/libdbus-glib-1.so.*
%{_bindir}/dbus-binding-tool
%{_mandir}/man1/dbus-binding-tool.1*

%files devel
%{_libdir}/libdbus-glib-1.so
%{_libdir}/pkgconfig/dbus-glib-1.pc
%{_includedir}/dbus-1.0/dbus/*
%{_datadir}/gtk-doc/html/dbus-glib
%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_libexecdir}/dbus-bash-completion-helper


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.112-13
- Prepare for Oreon 11 (RP1)
