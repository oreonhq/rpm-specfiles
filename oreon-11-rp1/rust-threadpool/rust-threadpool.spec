%global source0_hash d050e60b33d41c19108b32cea32164033a9013fe3b46cbd4457559bfbf77afaa
%bcond check 1
%global debug_package %{nil}
%global crate threadpool
Name:           rust-threadpool
Version:        1.8.1
Release:        1%{?dist}
Summary:        A thread pool for running a number of jobs on a fixed set of worker t...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/threadpool
Source0:        https://static.crates.io/crates/threadpool/threadpool-%{version}.crate
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
Summary:        A thread pool for running a number of jobs on a fixed set of worker t...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
touch README.md
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
%files -n rust-threadpool-devel -f %{oreon_filedir}/rust-threadpool-devel.list

%changelog

%autochangelog
