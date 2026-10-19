%global source0_hash f42f67da2385b51a5f9652db9c93d78aeaf7610bf5ec366080b6de810604af53
%bcond check 0
%global debug_package %{nil}
%global crate serdect
Name:           rust-serdect0.3
Version:        0.3.0
Release:        1%{?dist}
Summary:        Constant-time serde serializer/deserializer helpers for data that pot...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/serdect
Source0:        https://static.crates.io/crates/serdect/serdect-%{version}.crate
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
Summary:        Constant-time serde serializer/deserializer helpers for data that pot...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Constant-time serde serializer/deserializer helpers for data that pot...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Constant-time serde serializer/deserializer helpers for data that pot...
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Constant-time serde serializer/deserializer helpers for data that pot...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-serdect0.3-devel -f %{oreon_filedir}/rust-serdect0.3-devel.list

%changelog

%autochangelog
