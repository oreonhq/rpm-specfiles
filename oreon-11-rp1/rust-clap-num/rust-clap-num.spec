%global source0_hash 822c4000301ac390e65995c62207501e3ef800a1fc441df913a5e8e4dc374816
%bcond check 1
%global debug_package %{nil}
%global crate clap-num
Name:           rust-clap-num
Version:        1.2.0
Release:        1%{?dist}
Summary:        Number parsers for clap
License:        MIT
URL:            https://crates.io/crates/clap-num
Source0:        https://static.crates.io/crates/clap-num/clap-num-%{version}.crate
Patch2:         https://github.com/newAM/clap-num/commit/905655d8f4cf55db446c94d731b321a405240ff8.patch#/%{name}-1.2.0-debug_assert.patch
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
Summary:        Number parsers for clap
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
%files -n rust-clap-num-devel -f %{oreon_filedir}/rust-clap-num-devel.list

%changelog

%autochangelog
