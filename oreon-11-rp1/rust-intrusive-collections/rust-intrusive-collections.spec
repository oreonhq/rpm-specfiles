%global source0_hash 189d0897e4cbe8c75efedf3502c18c887b05046e59d28404d4d8e46cbc4d1e86
%bcond check 0
%global debug_package %{nil}
%global crate intrusive-collections
Name:           rust-intrusive-collections
Version:        0.9.7
Release:        1%{?dist}
Summary:        Intrusive collections for Rust (linked list and red-black tree)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/intrusive-collections
Source0:        https://static.crates.io/crates/intrusive-collections/intrusive-collections-%{version}.crate
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
Summary:        Intrusive collections for Rust (linked list and red-black tree)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Intrusive collections for Rust (linked list and red-black tree)
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Intrusive collections for Rust (linked list and red-black tree)
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-intrusive-collections-devel -f %{oreon_filedir}/rust-intrusive-collections-devel.list

%changelog

%autochangelog
