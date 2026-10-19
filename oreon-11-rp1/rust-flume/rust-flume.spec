%global source0_hash 5e139bc46ca777eb5efaf62df0ab8cc5fd400866427e56c68b22e414e53bd3be
%bcond check 0
%global debug_package %{nil}
%global crate flume
Name:           rust-flume
Version:        0.12.0
Release:        1%{?dist}
Summary:        Blazingly fast multi-producer channel
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/flume
Source0:        https://static.crates.io/crates/flume/flume-%{version}.crate
Patch:          flume-fix-metadata.diff
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
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+eventual-fairness-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+eventual-fairness-devel

This package contains library source intended for building other packages which
use the "eventual-fairness" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-sink-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+futures-sink-devel

This package contains library source intended for building other packages which
use the "futures-sink" feature of the "%{crate}" crate.

%package     -n %{name}+select-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+select-devel

This package contains library source intended for building other packages which
use the "select" feature of the "%{crate}" crate.

%package     -n %{name}+spin-devel
Summary:        Blazingly fast multi-producer channel
BuildArch:      noarch
%description -n %{name}+spin-devel

This package contains library source intended for building other packages which
use the "spin" feature of the "%{crate}" crate.

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
%files -n rust-flume-devel -f %{oreon_filedir}/rust-flume-devel.list

%changelog

%autochangelog
