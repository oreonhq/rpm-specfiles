%global source0_hash 8593e8e72159ed2257d083c7a454a85cbf854f37a0966d8d483aff8c8a3ebcee
%bcond check 0
%global debug_package %{nil}
%global crate syn
Name:           rust-syn
Version:        3.0.6
Release:        2%{?dist}
Summary:        Parser for Rust source code
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/syn
Source0:        https://static.crates.io/crates/syn/syn-%{version}.crate
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
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clone-impls-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+clone-impls-devel

This package contains library source intended for building other packages which
use the "clone-impls" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+extra-traits-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+extra-traits-devel

This package contains library source intended for building other packages which
use the "extra-traits" feature of the "%{crate}" crate.

%package     -n %{name}+fold-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+fold-devel

This package contains library source intended for building other packages which
use the "fold" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+parsing-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+parsing-devel

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%package     -n %{name}+printing-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+printing-devel

This package contains library source intended for building other packages which
use the "printing" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+proc-macro-devel

This package contains library source intended for building other packages which
use the "proc-macro" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+visit-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+visit-devel

This package contains library source intended for building other packages which
use the "visit" feature of the "%{crate}" crate.

%package     -n %{name}+visit-mut-devel
Summary:        Parser for Rust source code
BuildArch:      noarch
%description -n %{name}+visit-mut-devel

This package contains library source intended for building other packages which
use the "visit-mut" feature of the "%{crate}" crate.

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
%files -n rust-syn-devel -f %{oreon_filedir}/rust-syn-devel.list

%changelog

%autochangelog
