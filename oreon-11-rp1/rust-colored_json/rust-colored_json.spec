%global source0_hash e35980a1b846f8e3e359fd18099172a0857140ba9230affc4f71348081e039b6
%bcond check 0
%global debug_package %{nil}
%global crate colored_json
Name:           rust-colored_json
Version:        5.0.0
Release:        1%{?dist}
Summary:        Colorize JSON, for printing it out on the command line
License:        EPL-2.0
URL:            https://crates.io/crates/colored_json
Source0:        https://static.crates.io/crates/colored_json/colored_json-%{version}.crate
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
Summary:        Colorize JSON, for printing it out on the command line
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-colored_json-devel -f %{oreon_filedir}/rust-colored_json-devel.list

%changelog

%autochangelog
