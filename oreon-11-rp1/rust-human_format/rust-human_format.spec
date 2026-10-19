%global source0_hash eaec953f16e5bcf6b8a3cb3aa959b17e5577dbd2693e94554c462c08be22624b
%bcond check 0
%global debug_package %{nil}
%global crate human_format
Name:           rust-human_format
Version:        1.2.1
Release:        1%{?dist}
Summary:        Rust Port of human-format from node, formatting numbers for us, while...
License:        MIT
URL:            https://crates.io/crates/human_format
Source0:        https://static.crates.io/crates/human_format/human_format-%{version}.crate
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

%package     -n %{name}+panic_parse-devel
Summary:        Rust Port of human-format from node, formatting numbers for us, while...
BuildArch:      noarch
%description -n %{name}+panic_parse-devel

This package contains library source intended for building other packages which
use the "panic_parse" feature of the "%{crate}" crate.

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
%files -n rust-human_format-devel -f %{oreon_filedir}/rust-human_format-devel.list

%changelog

%autochangelog
