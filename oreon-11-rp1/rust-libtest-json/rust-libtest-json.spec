%global source0_hash a8f58e30343a6bfe0fb896b0bb92cf482c34ed047c637aac4b561d0b251b638c
%bcond check 0
%global debug_package %{nil}
%global crate libtest-json
Name:           rust-libtest-json
Version:        0.0.2
Release:        1%{?dist}
Summary:        Definition of the json output for libtest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libtest-json
Source0:        https://static.crates.io/crates/libtest-json/libtest-json-%{version}.crate
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
Summary:        Definition of the json output for libtest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Definition of the json output for libtest
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Definition of the json output for libtest
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-schema-devel
Summary:        Definition of the json output for libtest
BuildArch:      noarch
%description -n %{name}+unstable-schema-devel

This package contains library source intended for building other packages which
use the "unstable-schema" feature of the "%{crate}" crate.

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
%files -n rust-libtest-json-devel -f %{oreon_filedir}/rust-libtest-json-devel.list

%changelog

%autochangelog
