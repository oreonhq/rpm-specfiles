%global source0_hash 618fc4e8de393b719b1641c1d8eec01826d4d39d15ade92679d221c7f5e4e70d

Name:           libnice
Version:        0.1.23
Release:        2%{?dist}
Summary:        GLib ICE implementation

License:        LGPL-2.1-or-later OR MPL-1.1
URL:            https://nice.freedesktop.org/
Source0:        https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
Source1:        https://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz.asc

# gpg --recv-keys 1D388E5A4ED9A2BB
# gpg --output olivier.pgp --armor --export olivier.crete@ocrete.ca
Source2: olivier.pgp

# Build against the new gupnp-igd
Patch0:         libnice-gupnp-1.6.patch

BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel >= 2.12.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel >= 0.11.91
BuildRequires:  gstreamer1-plugins-base-devel >= 0.11.91
BuildRequires:  gupnp-igd-devel >= 0.1.2
BuildRequires:  gtk-doc
BuildRequires:  graphviz
BuildRequires:  meson

Requires:       gupnp-igd%{?_isa}

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


%check
# Temporarily make the upstream test-suite run on Intel arches only because we
# are getting random crashes in Koji on secondary arches but I have not been
# able to reproduce them locally so far.
%ifarch x86_64 %{ix86}
%meson_test
%endif


%ldconfig_scriptlets


%files
%doc NEWS README
%license COPYING COPYING.LGPL COPYING.MPL
%{_bindir}/stunbdc
%{_bindir}/stund
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Nice-0.1.typelib


%files gstreamer1
%{_libdir}/gstreamer-1.0/libgstnice.so


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/nice.pc
%{_datadir}/gtk-doc/html/%{name}/
%{_datadir}/gir-1.0/Nice-0.1.gir


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.23-2
- Prepare for Oreon 11 (RP1)
