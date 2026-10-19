%global source0_hash c466cd63a4217d5b2b8e32f23f58312741ce96e3c84bf7438677d2baff0fc555
%bcond check 0
%global debug_package %{nil}
%global crate hickory-client
Name:           rust-hickory-client
Version:        0.25.2
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-client
Source0:        https://static.crates.io/crates/hickory-client/hickory-client-%{version}.crate
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

%package     -n %{name}+backtrace-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-ring-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
BuildArch:      noarch
%description -n %{name}+dnssec-ring-devel

This package contains library source intended for building other packages which
use the "dnssec-ring" feature of the "%{crate}" crate.

%package     -n %{name}+mdns-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
BuildArch:      noarch
%description -n %{name}+mdns-devel

This package contains library source intended for building other packages which
use the "mdns" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the Client libr...
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

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
%files -n rust-hickory-client-devel -f %{oreon_filedir}/rust-hickory-client-devel.list

%changelog

%autochangelog
