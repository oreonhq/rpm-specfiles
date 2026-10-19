%global source0_hash 277639f0198568f70f8fe4ab88a52a67c96bca12f27ba5c17a76acdcb8b45834
%bcond check 0
%global debug_package %{nil}
%global crate minimad
Name:           rust-minimad
Version:        0.9.1
Release:        1%{?dist}
Summary:        light Markdown parser
License:        MIT
URL:            https://crates.io/crates/minimad
Source0:        https://static.crates.io/crates/minimad/minimad-%{version}.crate
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
Summary:        light Markdown parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+escaping-devel
Summary:        light Markdown parser
BuildArch:      noarch
%description -n %{name}+escaping-devel

This package contains library source intended for building other packages which
use the "escaping" feature of the "%{crate}" crate.

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
%files -n rust-minimad-devel -f %{oreon_filedir}/rust-minimad-devel.list

%changelog

%autochangelog
