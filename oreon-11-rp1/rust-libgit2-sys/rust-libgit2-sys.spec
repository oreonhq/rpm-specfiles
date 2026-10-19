%global source0_hash 7f7c568b25d7489bc3fb2988ed69ab111d2944d2f5fec3d5c987fe545ea97b50
%bcond check 0
%global debug_package %{nil}
%global crate libgit2-sys
%global crate_version 0.18.8+1.9.7
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-libgit2-sys
Version:        0.18.8
Release:        1%{?dist}
Summary:        Native bindings to the libgit2 library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libgit2-sys
Source0:        https://static.crates.io/crates/libgit2-sys/libgit2-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+https-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+https-devel

This package contains library source intended for building other packages which
use the "https" feature of the "%{crate}" crate.

%package     -n %{name}+libssh2-sys-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+libssh2-sys-devel

This package contains library source intended for building other packages which
use the "libssh2-sys" feature of the "%{crate}" crate.

%package     -n %{name}+ssh-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+ssh-devel

This package contains library source intended for building other packages which
use the "ssh" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-sha256-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+unstable-sha256-devel

This package contains library source intended for building other packages which
use the "unstable-sha256" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-openssl-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+vendored-openssl-devel

This package contains library source intended for building other packages which
use the "vendored-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Native bindings to the libgit2 library
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
sed -i '1s|#!/usr/bin/env python$|#!/usr/bin/env python3|' libgit2/script/release.py
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libgit2-sys-devel -f %{oreon_filedir}/rust-libgit2-sys-devel.list

%changelog

%autochangelog
