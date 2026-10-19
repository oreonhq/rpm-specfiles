%global source0_hash 5b81787e655bd59cecadc91f7b6b8651330b2be6c33246039a65e5cd6f4e0828
%bcond check 1
%global debug_package %{nil}
%global crate serde-json-core
Name:           rust-serde-json-core
Version:        0.6.0
Release:        1%{?dist}
Summary:        Serde-json for no_std programs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde-json-core
Source0:        https://static.crates.io/crates/serde-json-core/serde-json-core-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Serde-json for no_std programs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+custom-error-messages-devel
Summary:        Serde-json for no_std programs
BuildArch:      noarch
%description -n %{name}+custom-error-messages-devel

This package contains library source intended for building other packages which
use the "custom-error-messages" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Serde-json for no_std programs
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Serde-json for no_std programs
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' '+'
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
%files -n rust-serde-json-core-devel -f %{oreon_filedir}/rust-serde-json-core-devel.list

%changelog

%autochangelog
