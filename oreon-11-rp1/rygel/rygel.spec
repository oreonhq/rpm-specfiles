%global source0_hash cf386e280d8eaf9b6677a2f48ba78484c72a09554d5c58c51cd87fa5945617c8
%global apiver 2.8
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:          rygel
Version:       46.0
Release:        1%{?dist}
Summary:        A collection of UPnP/DLNA services
License:       LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:           https://wiki.gnome.org/Projects/Rygel
Source0:        https://download.gnome.org/sources/%{name}/45/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libunistring-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gupnp-1.6)
BuildRequires:  pkgconfig(gupnp-av-1.0)
BuildRequires:  pkgconfig(gupnp-dlna-2.0)
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tinysparql-3.0)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  valadoc
# /oreon:deps
%description
Rygel is a home media solution that allows you to easily share audio, video and
pictures, and control of media player on your home network. In technical terms
it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in
mechanism. Interoperability with other devices in the market is achieved by
conformance to very strict requirements of DLNA and on the fly conversion of
media to format that client devices are capable of handling.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package localsearch
Summary: Localsearch plugin for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-tracker <= %{version}
%description localsearch
A plugin for rygel to use localsearch to locate media on the local machine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
  -Dapi-docs=true \
  -Dintrospection=enabled \
  -Dexamples=false
%meson_build
%install
%meson_install
%find_lang %{name}
%systemd_user_post %{name}.service
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%preun

%systemd_user_preun %{name}.service
%postun

%systemd_user_postun_with_restart %{name}.service
%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel-preferences.desktop
%files -f %{oreon_filedir}/main.list
%files -n rygel-devel -f %{oreon_filedir}/rygel-devel.list
%files -n rygel-localsearch -f %{oreon_filedir}/rygel-localsearch.list

%changelog

%autochangelog
