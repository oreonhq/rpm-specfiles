%global source0_hash 1fd32eb54d016e203b7c2600e3a7802c75843a92e38ccc4869aefeca21771a64
%bcond check 1
%global debug_package %{nil}
%global crate colored_json
Name:           rust-colored_json2
Version:        2.1.0
Release:        1%{?dist}
Summary:        Colorize JSON, for printing it out on the command line
License:        EPL-2.0
URL:            https://crates.io/crates/colored_json
Source0:        https://static.crates.io/crates/colored_json/colored_json-%{version}.crate
Patch:          colored_json-fix-metadata.diff
Patch10:        colored_json-2-no-atty.patch
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
%files -n rust-colored_json2-devel -f %{oreon_filedir}/rust-colored_json2-devel.list

%changelog

%autochangelog
