%global source0_hash 3f3da5255c95d5a716857d54b5b8f4e8d67c3484d3beaaaae2ce25063b3ba981
%bcond check 0
%global debug_package %{nil}
%global crate hickory-resolver
Name:           rust-hickory-resolver
Version:        0.26.3
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-resolver
Source0:        https://static.crates.io/crates/hickory-resolver/hickory-resolver-%{version}.crate
Patch:          hickory-resolver-fix-metadata-auto.diff
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
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-ring-devel
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
BuildArch:      noarch
%description -n %{name}+dnssec-ring-devel

This package contains library source intended for building other packages which
use the "dnssec-ring" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+system-config-devel
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
BuildArch:      noarch
%description -n %{name}+system-config-devel

This package contains library source intended for building other packages which
use the "system-config" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Hickory DNS is a safe and secure DNS library. This Resolver library...
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
%files -n rust-hickory-resolver-devel -f %{oreon_filedir}/rust-hickory-resolver-devel.list

%changelog

%autochangelog
