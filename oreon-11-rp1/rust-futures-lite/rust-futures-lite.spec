%global source0_hash f78e10609fe0e0b3f4157ffab1876319b5b0db102a2c60dc4626306dc46b44ad
%bcond check 0
%global debug_package %{nil}
%global crate futures-lite
Name:           rust-futures-lite
Version:        2.6.1
Release:        1%{?dist}
Summary:        Futures, streams, and async I/O combinators
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/futures-lite
Source0:        https://static.crates.io/crates/futures-lite/futures-lite-%{version}.crate
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
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+fastrand-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+fastrand-devel

This package contains library source intended for building other packages which
use the "fastrand" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+parking-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+parking-devel

This package contains library source intended for building other packages which
use the "parking" feature of the "%{crate}" crate.

%package     -n %{name}+race-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+race-devel

This package contains library source intended for building other packages which
use the "race" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Futures, streams, and async I/O combinators
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-futures-lite-devel -f %{oreon_filedir}/rust-futures-lite-devel.list

%changelog

%autochangelog
