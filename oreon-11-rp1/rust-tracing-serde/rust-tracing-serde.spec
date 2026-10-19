%global source0_hash 704b1aeb7be0d0a84fc9828cae51dab5970fee5088f83d1dd7ee6f6246fc6ff1
%bcond check 0
%global debug_package %{nil}
%global crate tracing-serde
Name:           rust-tracing-serde
Version:        0.2.0
Release:        1%{?dist}
Summary:        A compatibility layer for serializing trace data with `serde`
License:        MIT
URL:            https://crates.io/crates/tracing-serde
Source0:        https://static.crates.io/crates/tracing-serde/tracing-serde-%{version}.crate
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

%package     -n %{name}+valuable-devel
Summary:        A compatibility layer for serializing trace data with `serde`
BuildArch:      noarch
%description -n %{name}+valuable-devel

This package contains library source intended for building other packages which
use the "valuable" feature of the "%{crate}" crate.

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
%files -n rust-tracing-serde-devel -f %{oreon_filedir}/rust-tracing-serde-devel.list

%changelog

%autochangelog
