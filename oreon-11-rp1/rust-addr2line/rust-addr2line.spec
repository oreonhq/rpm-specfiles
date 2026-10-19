%global source0_hash 1b5d307320b3181d6d7954e663bd7c774a838b8220fe0593c86d9fb09f498b4b
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate addr2line
Name:           rust-addr2line
Version:        0.25.1
Release:        1%{?dist}
Summary:        Cross-platform symbolication library written in Rust, using gimli
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/addr2line
Source0:        https://static.crates.io/crates/addr2line/addr2line-%{version}.crate
Patch:          addr2line-fix-metadata.diff
Patch10:        addr2line-0.25.1-cpp_demangle-0.5.patch
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
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cargo-all-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+cargo-all-devel

This package contains library source intended for building other packages which
use the "cargo-all" feature of the "%{crate}" crate.

%package     -n %{name}+cpp_demangle-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+cpp_demangle-devel

This package contains library source intended for building other packages which
use the "cpp_demangle" feature of the "%{crate}" crate.

%package     -n %{name}+fallible-iterator-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+fallible-iterator-devel

This package contains library source intended for building other packages which
use the "fallible-iterator" feature of the "%{crate}" crate.

%package     -n %{name}+loader-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+loader-devel

This package contains library source intended for building other packages which
use the "loader" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-demangle-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+rustc-demangle-devel

This package contains library source intended for building other packages which
use the "rustc-demangle" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Cross-platform symbolication library written in Rust, using gimli
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm src/bin/addr2line.rs
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
%files -n rust-addr2line-devel -f %{oreon_filedir}/rust-addr2line-devel.list

%changelog

%autochangelog
