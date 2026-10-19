%global source0_hash d54ad936ceb654e99f59b0227e4d1974b858970d250d98c6484abcfdc8334722
%global glib2_version 2.45.8
%global json_glib_version 1.1.1
Summary:        Library for reading Jcat files
Name:      libjcat
Version:   0.2.6
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/%{name}
Source0:        https://github.com/hughsie/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         skip-pq-test-when-crypto-policy-blocks.patch
Requires: glib2%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gnutls-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel
BuildRequires:  meson
BuildRequires:  vala
# /oreon:deps
%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package tests
Summary: Files for installed tests
%description tests
Executable and data files for installed tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Dgtkdoc=true \
    -Dtests=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test

%files -f %{oreon_filedir}/main.list
%files -n libjcat-devel -f %{oreon_filedir}/libjcat-devel.list
%files -n libjcat-tests -f %{oreon_filedir}/libjcat-tests.list
