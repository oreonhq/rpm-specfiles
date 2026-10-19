%global source0_hash 5c7398b9c8b70908f6371f47ed36737907c87c52af34c268fed0bf0ceb92ead9
%bcond check 0
%global debug_package %{nil}
%global crate num_threads
Name:           rust-num_threads
Version:        0.1.7
Release:        1%{?dist}
Summary:        A minimal library that determines the number of running threads for t...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num_threads
Source0:        https://static.crates.io/crates/num_threads/num_threads-%{version}.crate
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
Summary:        A minimal library that determines the number of running threads for t...
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
%files -n rust-num_threads-devel -f %{oreon_filedir}/rust-num_threads-devel.list

%changelog

%autochangelog
