%global source0_hash 26d1e2536ce4f35f4846aa13bff16bd0ff40157cdb14cc056c7b14ba41233ba0
%bcond check 0
%global debug_package %{nil}
%global crate rustls-platform-verifier
Name:           rust-rustls-platform-verifier
Version:        0.7.0
Release:        1%{?dist}
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustls-platform-verifier
Source0:        https://static.crates.io/crates/rustls-platform-verifier/rustls-platform-verifier-%{version}.crate
Patch:          rustls-platform-verifier-fix-metadata-auto.diff
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

%package     -n %{name}+base64-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+cert-logging-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+cert-logging-devel

This package contains library source intended for building other packages which
use the "cert-logging" feature of the "%{crate}" crate.

%package     -n %{name}+dbg-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+dbg-devel

This package contains library source intended for building other packages which
use the "dbg" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+ffi-testing-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+ffi-testing-devel

This package contains library source intended for building other packages which
use the "ffi-testing" feature of the "%{crate}" crate.

%package     -n %{name}+jni-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+jni-devel

This package contains library source intended for building other packages which
use the "jni" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        rustls-platform-verifier supports verifying TLS certificates in rustl...
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

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
%files -n rust-rustls-platform-verifier-devel -f %{oreon_filedir}/rust-rustls-platform-verifier-devel.list

%changelog

%autochangelog
