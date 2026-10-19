%global source0_hash b766684a183c8a439f2ca24d6973cf8bfdc1353ae9c54b2b91e81d2630dd034e
%bcond check 0
%global debug_package %{nil}
%global crate async-std-resolver
Name:           rust-async-std-resolver
Version:        0.24.4
Release:        1%{?dist}
Summary:        DNS resolver implementation based on async-std and Hickory DNS
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-std-resolver
Source0:        https://static.crates.io/crates/async-std-resolver/async-std-resolver-%{version}.crate
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
Summary:        DNS resolver implementation based on async-std and Hickory DNS
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+system-config-devel
Summary:        DNS resolver implementation based on async-std and Hickory DNS
BuildArch:      noarch
%description -n %{name}+system-config-devel

This package contains library source intended for building other packages which
use the "system-config" feature of the "%{crate}" crate.

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
%files -n rust-async-std-resolver-devel -f %{oreon_filedir}/rust-async-std-resolver-devel.list

%changelog

%autochangelog
