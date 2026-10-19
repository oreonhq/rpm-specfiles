%global source0_hash 45bb67a18fa91266cc7807181f62f9178a6873bfad7dc788c42e6430db40184f
%bcond check 0
%global debug_package %{nil}
%global crate shell-escape
Name:           rust-shell-escape
Version:        0.1.5
Release:        1%{?dist}
Summary:        Escape characters that may have a special meaning in a shell
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/shell-escape
Source0:        https://static.crates.io/crates/shell-escape/shell-escape-%{version}.crate
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
Summary:        Escape characters that may have a special meaning in a shell
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
%files -n rust-shell-escape-devel -f %{oreon_filedir}/rust-shell-escape-devel.list

%changelog

%autochangelog
