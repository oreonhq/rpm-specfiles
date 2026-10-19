%global source0_hash f1fd850498411e4057f1cba79e6e2bc7cbe960544c1046ab46d4685c403a1121
%bcond check 1
%global debug_package %{nil}
%global crate cryptoki-sys
Name:           rust-cryptoki-sys
Version:        0.5.0
Release:        1%{?dist}
Summary:        FFI wrapper around the PKCS #11 API
License:        Apache-2.0
URL:            https://crates.io/crates/cryptoki-sys
Source0:        https://static.crates.io/crates/cryptoki-sys/cryptoki-sys-%{version}.crate
Patch:          cryptoki-sys-fix-metadata.diff
Patch2:         0001-Unconditionally-rebuild-bindings-to-support-all-arch.patch
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
Summary:        FFI wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        FFI wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+generate-bindings-devel
Summary:        FFI wrapper around the PKCS #11 API
BuildArch:      noarch
%description -n %{name}+generate-bindings-devel

This package contains library source intended for building other packages which
use the "generate-bindings" feature of the "%{crate}" crate.

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
%files -n rust-cryptoki-sys-devel -f %{oreon_filedir}/rust-cryptoki-sys-devel.list

%changelog

%autochangelog
