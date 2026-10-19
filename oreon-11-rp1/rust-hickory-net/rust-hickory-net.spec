%global source0_hash c480823ed7c2c5d0f09c41020cb6b7c28029ce60ec42dc942158dcf22f8e0a4d
%bcond check 0
%global debug_package %{nil}
%global crate hickory-net
Name:           rust-hickory-net
Version:        0.26.3
Release:        1%{?dist}
Summary:        Hickory-net is a safe and secure low-level DNS library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-net
Source0:        https://static.crates.io/crates/hickory-net/hickory-net-%{version}.crate
Patch:          hickory-net-fix-metadata-auto.diff
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
Summary:        Hickory-net is a safe and secure low-level DNS library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+mdns-devel
Summary:        Hickory-net is a safe and secure low-level DNS library
BuildArch:      noarch
%description -n %{name}+mdns-devel

This package contains library source intended for building other packages which
use the "mdns" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory-net is a safe and secure low-level DNS library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+socket2-devel
Summary:        Hickory-net is a safe and secure low-level DNS library
BuildArch:      noarch
%description -n %{name}+socket2-devel

This package contains library source intended for building other packages which
use the "socket2" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Hickory-net is a safe and secure low-level DNS library
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Hickory-net is a safe and secure low-level DNS library
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
%files -n rust-hickory-net-devel -f %{oreon_filedir}/rust-hickory-net-devel.list

%changelog

%autochangelog
