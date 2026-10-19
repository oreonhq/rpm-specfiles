%global source0_hash c04141a07bb0c0bc461cb657808764de571702a59bc5c726c400ac9a7625e3ab
%bcond check 0
%global debug_package %{nil}
%global crate libssh2-sys
Name:           rust-libssh2-sys
Version:        0.3.2
Release:        1%{?dist}
Summary:        Native bindings to the libssh2 library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libssh2-sys
Source0:        https://static.crates.io/crates/libssh2-sys/libssh2-sys-%{version}.crate
Patch:          libssh2-sys-fix-metadata-auto.diff
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

%package     -n %{name}+openssl-on-win32-devel
Summary:        Native bindings to the libssh2 library
BuildArch:      noarch
%description -n %{name}+openssl-on-win32-devel

This package contains library source intended for building other packages which
use the "openssl-on-win32" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-openssl-devel
Summary:        Native bindings to the libssh2 library
BuildArch:      noarch
%description -n %{name}+vendored-openssl-devel

This package contains library source intended for building other packages which
use the "vendored-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-compat-devel
Summary:        Native bindings to the libssh2 library
BuildArch:      noarch
%description -n %{name}+zlib-ng-compat-devel

This package contains library source intended for building other packages which
use the "zlib-ng-compat" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-libssh2-sys-devel -f %{oreon_filedir}/rust-libssh2-sys-devel.list

%changelog

%autochangelog
