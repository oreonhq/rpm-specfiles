%global source0_hash aa00adbd2c77f584cfe41f348772d2f131af1fa519a7f6b98638f1144ead96a4
%bcond check 0
%global debug_package %{nil}
%global crate gix-command
Name:           rust-gix-command
Version:        0.10.1
Release:        1%{?dist}
Summary:        A crate of the gitoxide project handling internal git command execution
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-command
Source0:        https://static.crates.io/crates/gix-command/gix-command-%{version}.crate
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
Summary:        A crate of the gitoxide project handling internal git command execution
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
%files -n rust-gix-command-devel -f %{oreon_filedir}/rust-gix-command-devel.list

%changelog

%autochangelog
