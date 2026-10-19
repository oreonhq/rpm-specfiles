%global source0_hash 0bae117ee14789185e129aaee5d93750abe67fdc5a9a62650452bfe4e122a3a9
%bcond check 0
%global debug_package %{nil}
%global crate tracing-flame
Name:           rust-tracing-flame
Version:        0.2.0
Release:        1%{?dist}
Summary:        Tracing layer for creating flamegraphs from span timings
License:        MIT
URL:            https://crates.io/crates/tracing-flame
Source0:        https://static.crates.io/crates/tracing-flame/tracing-flame-%{version}.crate
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
Summary:        Tracing layer for creating flamegraphs from span timings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Tracing layer for creating flamegraphs from span timings
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

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
%files -n rust-tracing-flame-devel -f %{oreon_filedir}/rust-tracing-flame-devel.list

%changelog

%autochangelog
