%global source0_hash 388c44dc09d76f1536602ead6d325eb532f5c122f17782bd57fb47baeeb767e2
%bcond check 0
%global debug_package %{nil}
%global crate xz2
Name:           rust-xz2
Version:        0.1.7
Release:        1%{?dist}
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/xz2
Source0:        https://static.crates.io/crates/xz2/xz2-%{version}.crate
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

%package     -n %{name}+futures-devel
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-...
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-...
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-...
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-io-devel
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-...
BuildArch:      noarch
%description -n %{name}+tokio-io-devel

This package contains library source intended for building other packages which
use the "tokio-io" feature of the "%{crate}" crate.

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
%files -n rust-xz2-devel -f %{oreon_filedir}/rust-xz2-devel.list

%changelog

%autochangelog
