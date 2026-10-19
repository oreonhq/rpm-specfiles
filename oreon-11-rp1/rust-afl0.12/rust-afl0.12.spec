%global source0_hash f6c32f2f36624ffe2a8f65f9d76c224846b3a3d7242485bb5927c1127ee6c715
%bcond check 0
%global crate afl
Name:           rust-afl0.12
Version:        0.12.17
Release:        1%{?dist}
Summary:        Fuzzing Rust code with american-fuzzy-lop
License:        Apache-2.0
URL:            https://crates.io/crates/afl
Source0:        https://static.crates.io/crates/afl/afl-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fuzzing Rust code with american-fuzzy-lop
License:        # FIXME
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Fuzzing Rust code with american-fuzzy-lop
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        Fuzzing Rust code with american-fuzzy-lop
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+no_cfg_fuzzing-devel
Summary:        Fuzzing Rust code with american-fuzzy-lop
BuildArch:      noarch
%description -n %{name}+no_cfg_fuzzing-devel

This package contains library source intended for building other packages which
use the "no_cfg_fuzzing" feature of the "%{crate}" crate.

%package     -n %{name}+reset_lazy_static-devel
Summary:        Fuzzing Rust code with american-fuzzy-lop
BuildArch:      noarch
%description -n %{name}+reset_lazy_static-devel

This package contains library source intended for building other packages which
use the "reset_lazy_static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n afl -f %{oreon_filedir}/afl.list
%files -n rust-afl0.12-devel -f %{oreon_filedir}/rust-afl0.12-devel.list

%changelog

%autochangelog
