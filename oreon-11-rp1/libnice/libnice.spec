%global source1_hash 4404944fb6dbf0dd4df4c821175da9787413b462b6f7e8ccd9230b9020cd015e
%global source0_hash cfb5e8e778534f2f5b3c6f4958a1eb057c6b95c537c0f100817a537cf5d64fcc
Name:           libnice
Version:        0.1.24
Release:        1%{?dist}
Summary:        GLib ICE implementation
License:        LGPL-2.1-or-later OR MPL-1.1
URL:            https://nice.freedesktop.org/
Source0:        https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
Source1:        https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz.asc
Source2: olivier.pgp
Patch0:         libnice-gupnp-1.6.patch
Requires:       gupnp-igd%{?_isa}
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gupnp-igd-devel
BuildRequires:  meson
# /oreon:deps
%description
%{name} is an implementation of the IETF draft Interactive Connectivity
Establishment standard (ICE). ICE is useful for applications that want to
establish peer-to-peer UDP data streams. It automates the process of traversing
NATs and provides security against some attacks. Existing standards that use
ICE include the Session Initiation Protocol (SIP) and Jingle, XMPP extension
for audio/video calls.

%package        gstreamer1
Summary:        GStreamer plugin for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    gstreamer1
The %{name}-gstreamer1 package contains a gstreamer 1.0 plugin for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# disable tests that don't work in koji environment
sed \
    -e "s/^ *'test-set-port-range'/#&/" \
    -e "s/^ *'test-slow-resolving'/#&/" \
    -i tests/meson.build

%build

%meson -D gtk_doc=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch x86_64 %{ix86}
%meson_test
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libnice-gstreamer1 -f %{oreon_filedir}/libnice-gstreamer1.list
%files -n libnice-devel -f %{oreon_filedir}/libnice-devel.list

%changelog

%autochangelog
