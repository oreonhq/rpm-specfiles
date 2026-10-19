%global source0_hash a36fb3a748a4c9736ed7aeb5f2dfc99665247f1ce306abbddb2bf0ba2ac530a4
%bcond check 0
%global debug_package %{nil}
%global crate nanoserde
Name:           rust-nanoserde0.2
Version:        0.2.1
Release:        1%{?dist}
Summary:        Serialization library with zero dependencies.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/nanoserde
Source0:        https://static.crates.io/crates/nanoserde/nanoserde-%{version}.crate
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
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+binary-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+nanoserde-derive-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+nanoserde-derive-devel

This package contains library source intended for building other packages which
use the "nanoserde-derive" feature of the "%{crate}" crate.

%package     -n %{name}+ron-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+ron-devel

This package contains library source intended for building other packages which
use the "ron" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        Serialization library with zero dependencies.
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

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
%files -n rust-nanoserde0.2-devel -f %{oreon_filedir}/rust-nanoserde0.2-devel.list

%changelog

%autochangelog
