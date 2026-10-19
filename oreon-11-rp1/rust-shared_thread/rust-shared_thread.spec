%global source0_hash 52b86057fcb5423f5018e331ac04623e32d6b5ce85e33300f92c79a1973928b0
%bcond check 1
%global debug_package %{nil}
%global crate shared_thread
Name:           rust-shared_thread
Version:        0.2.0
Release:        1%{?dist}
Summary:        Similar to shared_child, but for threads instead of processes
License:        MIT
URL:            https://crates.io/crates/shared_thread
Source0:        https://static.crates.io/crates/shared_thread/shared_thread-%{version}.crate
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
Summary:        Similar to shared_child, but for threads instead of processes
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
%files -n rust-shared_thread-devel -f %{oreon_filedir}/rust-shared_thread-devel.list

%changelog

%autochangelog
