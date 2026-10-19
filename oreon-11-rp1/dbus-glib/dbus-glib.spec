%global source0_hash e3f3d4487e2883800770ed5899ed111bdc4ba7056af34a255c4c46ad8a2486f3
%global source1_hash 61f82a7ca4bc9c922c5a8b8b36c0feab772fea1db0ea744f823e57b726b8dbed
%global expat_version 1.95.5
%global glib2_version 2.40.0
%global dbus_version 1.8
Name:    dbus-glib
Version: 0.116
Release:        1%{?dist}
Summary:        GLib bindings for D-Bus
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:     https://www.freedesktop.org/software/dbus/
Source0:        https://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
Source1: https://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz.asc
Source2: gpgkey-DA98F25C0871C49A59EAFF2C4DE8FF2A63C7CC90.gpg
# oreon:deps
BuildRequires:  /usr/bin/chrpath
BuildRequires:  dbus-daemon
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description

D-Bus add-on library to integrate the standard D-Bus library with
the GLib thread abstraction and main loop.

%package devel
Summary: Libraries and headers for the D-Bus GLib bindings
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel

Headers and static libraries for the D-Bus GLib bindings

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
chmod -x $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%ldconfig_scriptlets
%oreon_autofiles dbus-glib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dbus-glib-devel -f %{oreon_filedir}/dbus-glib-devel.list

%changelog

%autochangelog
