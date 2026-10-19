%global source0_hash b3644627a5af5fa321c95b9b235a72fd24cd29c648c2c379431e6628655627bf
%bcond check 0
%global debug_package %{nil}
%global crate unicode-truncate
Name:           rust-unicode-truncate
Version:        1.1.0
Release:        1%{?dist}
Summary:        Unicode-aware algorithm to pad or truncate `str` in terms of displaye...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-truncate
Source0:        https://static.crates.io/crates/unicode-truncate/unicode-truncate-%{version}.crate
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
Summary:        Unicode-aware algorithm to pad or truncate `str` in terms of displaye...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Unicode-aware algorithm to pad or truncate `str` in terms of displaye...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-unicode-truncate-devel -f %{oreon_filedir}/rust-unicode-truncate-devel.list

%changelog

%autochangelog
