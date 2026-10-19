%global source0_hash 622f3fc73690be383c7214310406f28a90e6edeadc3cea882f9d71e495b9711a
%bcond check 1
%global debug_package %{nil}
%global crate crossbeam-deque
Name:           rust-crossbeam-deque
Version:        0.8.8
Release:        1%{?dist}
Summary:        Concurrent work-stealing deque
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crossbeam-deque
Source0:        https://static.crates.io/crates/crossbeam-deque/crossbeam-deque-%{version}.crate
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
Summary:        Concurrent work-stealing deque
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Concurrent work-stealing deque
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-crossbeam-deque-devel -f %{oreon_filedir}/rust-crossbeam-deque-devel.list

%changelog

%autochangelog
