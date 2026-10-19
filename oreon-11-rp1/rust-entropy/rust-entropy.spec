%global source0_hash aaddcf1b2c2d0a2c4fe3cf7fbbd7172d07e3fedc61dda7405a0560084d1a483e
%bcond check 1
%global debug_package %{nil}
%global crate entropy
Name:           rust-entropy
Version:        0.4.3
Release:        1%{?dist}
Summary:        Calculates the Shannon entropy of arrays of bytes and strings
License:        MIT
URL:            https://crates.io/crates/entropy
Source0:        https://static.crates.io/crates/entropy/entropy-%{version}.crate
Patch:          entropy-fix-metadata.diff
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
Summary:        Calculates the Shannon entropy of arrays of bytes and strings
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
%files -n rust-entropy-devel -f %{oreon_filedir}/rust-entropy-devel.list

%changelog

%autochangelog
