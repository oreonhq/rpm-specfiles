%global source0_hash 42b8cfee0e339a0337359f3c88165702ac6e600dc01c0cc9579a92d62b08477a
%bcond check 0
%global debug_package %{nil}
%global crate notify-types
Name:           rust-notify-types
Version:        2.1.0
Release:        1%{?dist}
Summary:        Types used by the notify crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/notify-types
Source0:        https://static.crates.io/crates/notify-types/notify-types-%{version}.crate
Patch:          notify-types-fix-metadata.diff
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
Summary:        Types used by the notify crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Types used by the notify crate
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-compat-6-devel
Summary:        Types used by the notify crate
BuildArch:      noarch
%description -n %{name}+serialization-compat-6-devel

This package contains library source intended for building other packages which
use the "serialization-compat-6" feature of the "%{crate}" crate.

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
%files -n rust-notify-types-devel -f %{oreon_filedir}/rust-notify-types-devel.list

%changelog

%autochangelog
