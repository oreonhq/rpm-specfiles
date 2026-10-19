%global source0_hash 931686e6a9b46d23f16c98180709ed70a1360aa4a7eaa8724c9d5dabab953547
%bcond check 0
%global debug_package %{nil}
%global crate nu-pretty-hex
Name:           rust-nu-pretty-hex
Version:        0.115.1
Release:        1%{?dist}
Summary:        Pretty hex dump of bytes slice in the common style
License:        MIT
URL:            https://crates.io/crates/nu-pretty-hex
Source0:        https://static.crates.io/crates/nu-pretty-hex/nu-pretty-hex-%{version}.crate
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
Summary:        Pretty hex dump of bytes slice in the common style
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
%files -n rust-nu-pretty-hex-devel -f %{oreon_filedir}/rust-nu-pretty-hex-devel.list

%changelog

%autochangelog
