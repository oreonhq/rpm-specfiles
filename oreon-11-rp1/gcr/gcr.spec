%global source0_hash c4442c15d4330f17a1f5194df08c576877af68412ab2521446a93bd5e24c931b
%ifarch %{valgrind_arches}
%global has_valgrind 1
%endif
Name:           gcr
Version:        4.4.1
Release:        1%{?dist}
Summary:        A library for bits of crypto UI and parsing
License:        LGPL-2.1-or-later AND FSFULLRWD AND (LGPL-3.0-or-later OR CC-BY-SA-3.0) AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND GCR-docs
URL:            https://gitlab.gnome.org/GNOME/gcr
Source0:        https://download.gnome.org/sources/%{name}/4.4/%{name}-%{version}.tar.xz
%if 0%{?has_valgrind}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: /usr/bin/gpg2
Requires: /usr/bin/ssh-add
Requires: /usr/bin/ssh-agent
# oreon:deps
BuildRequires:  /usr/bin/gpg2
BuildRequires:  /usr/bin/ssh-add
BuildRequires:  /usr/bin/ssh-agent
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
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

%package        libs
Summary:        gcr and gck libraries
Obsoletes:      %{name}-base < 3.92.0-1
Provides:       %{name}-base = %{version}-%{release}
Provides:       %{name}-base%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-gtk3 < 3.92.0-1
Obsoletes:      %{name}-gtk4 < 3.92.0-1
%description    libs
The %{name}-libs package contains the gcr and gck shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
Obsoletes:      %{name}-gtk3-devel < 3.92.0-1
Obsoletes:      %{name}-gtk4-devel < 3.92.0-1
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dcrypto=gnutls
%meson_build
%install
%meson_install
%find_lang gcr-4
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_user_post gcr-ssh-agent.service
%preun

%systemd_user_preun gcr-ssh-agent.service
%postun

%systemd_user_postun_with_restart gcr-ssh-agent.service
%files -f %{oreon_filedir}/main.list
%files -n gcr-libs -f %{oreon_filedir}/gcr-libs.list
%files -n gcr-devel -f %{oreon_filedir}/gcr-devel.list

%changelog

%autochangelog
