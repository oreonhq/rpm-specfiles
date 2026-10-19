%global source0_hash 75ae8b5984a4863d8a32109a848d038bd6d914f20f010cc141375f7a183c41cf
%bcond check 1
%global debug_package %{nil}
%global crate file-locker
Name:           rust-file-locker
Version:        1.1.4
Release:        1%{?dist}
Summary:        File locking via POSIX advisory record locks
License:        MIT
URL:            https://crates.io/crates/file-locker
Source0:        https://static.crates.io/crates/file-locker/file-locker-%{version}.crate
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
Summary:        File locking via POSIX advisory record locks
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

%cargo_test -- -- --skip FileLock::lock
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-file-locker-devel -f %{oreon_filedir}/rust-file-locker-devel.list

%changelog

%autochangelog
