%global source0_hash f8a6fe56c0038198998a6f217ca4e7ef3a5e51f46163bd6dd60b5c71ca6c6502
%bcond check 1
%global debug_package %{nil}
%global crate hickory-proto
Name:           rust-hickory-proto0.25
Version:        0.25.2
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-proto
Source0:        https://static.crates.io/crates/hickory-proto/hickory-proto-%{version}.crate
Patch:          hickory-proto-fix-metadata.diff
Patch10:        0001-Omit-tests-that-require-test_support-not-in-the-crat.patch
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
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+mdns-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+mdns-devel

This package contains library source intended for building other packages which
use the "mdns" feature of the "%{crate}" crate.

%package     -n %{name}+no-std-rand-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+no-std-rand-devel

This package contains library source intended for building other packages which
use the "no-std-rand" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-platform-verifier-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+rustls-platform-verifier-devel

This package contains library source intended for building other packages which
use the "rustls-platform-verifier" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+text-parsing-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+text-parsing-devel

This package contains library source intended for building other packages which
use the "text-parsing" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm src/quic/tests.rs
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
%files -n rust-hickory-proto0.25-devel -f %{oreon_filedir}/rust-hickory-proto0.25-devel.list

%changelog

%autochangelog
