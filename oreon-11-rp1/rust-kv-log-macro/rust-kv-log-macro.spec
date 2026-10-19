%global source0_hash 0de8b303297635ad57c9f5059fd9cee7a47f8e8daa09df0fcd07dd39fb22977f
%bcond check 0
%global debug_package %{nil}
%global crate kv-log-macro
Name:           rust-kv-log-macro
Version:        1.0.7
Release:        1%{?dist}
Summary:        Log macro for log's kv-unstable backend.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/kv-log-macro
Source0:        https://static.crates.io/crates/kv-log-macro/kv-log-macro-%{version}.crate
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
Summary:        Log macro for log's kv-unstable backend.
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
%files -n rust-kv-log-macro-devel -f %{oreon_filedir}/rust-kv-log-macro-devel.list

%changelog

%autochangelog
