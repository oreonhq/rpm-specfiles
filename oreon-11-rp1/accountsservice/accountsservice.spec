%global source0_hash adda4cdeae24fa0992e7df3ffff9effa7090be3ac233a3edfdf69d5a9c9b924f
Name:           accountsservice
Version:        23.13.9
Release:        1%{?dist}
Summary:        D-Bus interfaces for querying and manipulating user account information
License:        GPL-3.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/AccountsService/
Source0:        https://www.freedesktop.org/software/accountsservice/accountsservice-%{version}.tar.xz
Requires:       polkit
Requires:       shadow-utils
%{?systemd_requires}
Patch10001:     0001-mocklibc-Fix-compiler-warning.patch
Patch10002:     0002-user-manager-Fix-another-compiler-warning.patch
Patch10003:     0003-act-user-Use-the-reentrant-interfaces-of-crypt-_gens.patch
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libxcrypt-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  polkit-devel
BuildRequires:  python3-dbusmock
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  vala
# /oreon:deps
%description
The accountsservice project provides a set of D-Bus interfaces for
querying and manipulating user account information and an implementation
of these interfaces, based on the useradd, usermod and userdel commands.

%package libs
Summary: Client-side library to talk to accountsservice
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libs
The accountsservice-libs package contains a library that can
be used by applications that want to interact with the accountsservice
daemon.

%package devel
Summary: Development files for accountsservice-libs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The accountsservice-devel package contains headers and other
files needed to build applications that use accountsservice-libs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
 -Dgtk_doc=true \
 -Dadmin_group=wheel
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/accountsservice/interfaces/
%find_lang accounts-service
%ldconfig_scriptlets libs
%oreon_autofiles accountsservice-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles accountsservice-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post accounts-daemon.service
%preun

%systemd_preun accounts-daemon.service
%postun

%systemd_postun accounts-daemon.service
%files -f %{oreon_filedir}/main.list
%files -n accountsservice-libs -f %{oreon_filedir}/accountsservice-libs.list
%files -n accountsservice-devel -f %{oreon_filedir}/accountsservice-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.13.9-1
- Prepare for Oreon 11 (RP1)
