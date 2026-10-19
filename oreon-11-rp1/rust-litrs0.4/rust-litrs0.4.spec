%global source0_hash f5e54036fe321fd421e10d732f155734c4e4afd610dd556d9a82833ab3ee0bed
%bcond check 0
%global debug_package %{nil}
%global crate litrs
Name:           rust-litrs0.4
Version:        0.4.2
Release:        1%{?dist}
Summary:        Parse and inspect Rust literals (i.e. tokens in the Rust programming...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/litrs
Source0:        https://static.crates.io/crates/litrs/litrs-%{version}.crate
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
Summary:        Parse and inspect Rust literals (i.e. tokens in the Rust programming...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+check_suffix-devel
Summary:        Parse and inspect Rust literals (i.e. tokens in the Rust programming...
BuildArch:      noarch
%description -n %{name}+check_suffix-devel

This package contains library source intended for building other packages which
use the "check_suffix" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro2-devel
Summary:        Parse and inspect Rust literals (i.e. tokens in the Rust programming...
BuildArch:      noarch
%description -n %{name}+proc-macro2-devel

This package contains library source intended for building other packages which
use the "proc-macro2" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-xid-devel
Summary:        Parse and inspect Rust literals (i.e. tokens in the Rust programming...
BuildArch:      noarch
%description -n %{name}+unicode-xid-devel

This package contains library source intended for building other packages which
use the "unicode-xid" feature of the "%{crate}" crate.

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
%files -n rust-litrs0.4-devel -f %{oreon_filedir}/rust-litrs0.4-devel.list

%changelog

%autochangelog
