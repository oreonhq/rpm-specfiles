%global source0_hash dab93c7205280c4785c44517fe84d99751b81f6deb8450cb196da6be88e332bb
%bcond check 0
%global debug_package %{nil}
%global crate fallible_collections
Name:           rust-fallible_collections
Version:        0.5.2
Release:        1%{?dist}
Summary:        a crate which adds fallible allocation api to std collections
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fallible_collections
Source0:        https://static.crates.io/crates/fallible_collections/fallible_collections-%{version}.crate
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
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+hashmap-devel
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+hashmap-devel

This package contains library source intended for building other packages which
use the "hashmap" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_57-devel
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+rust_1_57-devel

This package contains library source intended for building other packages which
use the "rust_1_57" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+std_io-devel
Summary:        a crate which adds fallible allocation api to std collections
BuildArch:      noarch
%description -n %{name}+std_io-devel

This package contains library source intended for building other packages which
use the "std_io" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        a crate which adds fallible allocation api to std collections
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
%files -n rust-fallible_collections-devel -f %{oreon_filedir}/rust-fallible_collections-devel.list

%changelog

%autochangelog
