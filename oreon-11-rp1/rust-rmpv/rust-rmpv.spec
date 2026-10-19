%global source0_hash 7a4e1d4b9b938a26d2996af33229f0ca0956c652c1375067f0b45291c1df8417
%bcond check 1
%global debug_package %{nil}
%global crate rmpv
Name:           rust-rmpv
Version:        1.3.1
Release:        1%{?dist}
Summary:        Decoding/Encoding MessagePack values without schema
License:        MIT
URL:            https://crates.io/crates/rmpv
Source0:        https://static.crates.io/crates/rmpv/rmpv-%{version}.crate
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
Summary:        Decoding/Encoding MessagePack values without schema
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+with-serde-devel
Summary:        Decoding/Encoding MessagePack values without schema
BuildArch:      noarch
%description -n %{name}+with-serde-devel

This package contains library source intended for building other packages which
use the "with-serde" feature of the "%{crate}" crate.

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
%files -n rust-rmpv-devel -f %{oreon_filedir}/rust-rmpv-devel.list

%changelog

%autochangelog
