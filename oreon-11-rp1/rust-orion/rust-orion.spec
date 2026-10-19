%global source0_hash 5e6758747fd1ce1efaf2bd43219ac4aa9e28263b236b2b6a1e486bcd06820707
%bcond check 0
%global debug_package %{nil}
%global crate orion
Name:           rust-orion
Version:        0.17.15
Release:        1%{?dist}
Summary:        Usable, easy and safe pure-Rust crypto
License:        MIT
URL:            https://crates.io/crates/orion
Source0:        https://static.crates.io/crates/orion/orion-%{version}.crate
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
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ct-codecs-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+ct-codecs-devel

This package contains library source intended for building other packages which
use the "ct-codecs" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+safe_api-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+safe_api-devel

This package contains library source intended for building other packages which
use the "safe_api" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Usable, easy and safe pure-Rust crypto
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Usable, easy and safe pure-Rust crypto
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
%files -n rust-orion-devel -f %{oreon_filedir}/rust-orion-devel.list

%changelog

%autochangelog
