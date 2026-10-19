%global source0_hash 4148590afebada386688f18773da617792bf2ef03ffc1e4cbd2b1d45b023e0ba
%bcond check 0
%global debug_package %{nil}
%global crate serde
Name:           rust-serde
Version:        1.0.229
Release:        1%{?dist}
Summary:        Generic serialization/deserialization framework
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde
Source0:        https://static.crates.io/crates/serde/serde-%{version}.crate
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
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+rc-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+rc-devel

This package contains library source intended for building other packages which
use the "rc" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Generic serialization/deserialization framework
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-serde-devel -f %{oreon_filedir}/rust-serde-devel.list

%changelog

%autochangelog
