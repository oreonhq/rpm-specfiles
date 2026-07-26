%global source0_hash b85c5469d83eea1f8963ef0f636a4c296f033549af725ef870adc71cb1b90a2b

Summary: Run OCI containers with bubblewrap
Name: bwrap-oci
Version: 0.1.2
Release: 27%{?dist}
Source0: %{url}/archive/%{name}-%{version}.tar.gz
License: LGPL-2.0-or-later
URL: https://github.com/projectatomic/bwrap-oci

Requires: bubblewrap
Provides: bubblewrap-oci
# We always run autogen.sh
BuildRequires: autoconf automake
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: libseccomp-devel
BuildRequires: libxslt
BuildRequires: bubblewrap
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: make

%description
bwrap-oci uses Bubblewrap to run a container from an OCI spec file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
