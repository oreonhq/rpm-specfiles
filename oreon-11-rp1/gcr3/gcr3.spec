%global source0_hash bb7128a3c2febbfee9c03b90d77d498d0ceb237b0789802d60185c71c4bea24f
%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif
Name:           gcr3
Version:        3.41.1
Release:        1%{?dist}
Summary:        A library for bits of crypto UI and parsing
License:        LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND FSFULLRWD AND (LGPL-3.0-or-later OR CC-BY-SA-3.0) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND GCR-docs
URL:            https://wiki.gnome.org/Projects/CryptoGlue
Source0:        https://download.gnome.org/sources/gcr/3.41/gcr-%{version}.tar.xz
%if 0%{?has_valgrind}
%endif
Requires: %{name}-base%{?_isa} = %{version}-%{release}
Requires: /usr/bin/ssh-add
Requires: /usr/bin/ssh-agent
Conflicts: gcr < 3.90.0
# oreon:deps
BuildRequires:  /usr/bin/gpg2
BuildRequires:  /usr/bin/ssh-add
BuildRequires:  /usr/bin/ssh-agent
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  libgcrypt-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
gcr is a library for displaying certificates, and crypto UI, accessing
key stores. It also provides a viewer for crypto files on the GNOME
desktop.

gck is a library for accessing PKCS#11 modules like smart cards.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: gcr-devel < 3.90.0
%description devel
The %{name}-devel package includes the header files for the gcr library.

%package base
Summary: Library files for gcr
Conflicts: gcr-base < 3.90.0
%description base
The %{name}-base package includes the gcr-base library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gcr-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang gcr
rm -rf $RPM_BUILD_ROOT%{_libexecdir}/gcr-ssh-agent
rm -rf $RPM_BUILD_ROOT%{_userunitdir}/gcr-ssh-agent.service
rm -rf $RPM_BUILD_ROOT%{_userunitdir}/gcr-ssh-agent.socket
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gcr3-devel -f %{oreon_filedir}/gcr3-devel.list
%files -n gcr3-base -f %{oreon_filedir}/gcr3-base.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.41.1-12
- Prepare for Oreon 11 (RP1)
