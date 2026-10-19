%global source0_hash 0363053954f3e679645fc443321ca128b7b950a6fe288cf5f9335cc22ee58394
%bcond check 0
%global debug_package %{nil}
%global crate criterion
Name:           rust-criterion0.2
Version:        0.2.11
Release:        1%{?dist}
Summary:        Statistics-driven micro-benchmarking library
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/criterion
Source0:        https://static.crates.io/crates/criterion/criterion-%{version}.crate
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
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+criterion-plot-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+criterion-plot-devel

This package contains library source intended for building other packages which
use the "criterion-plot" feature of the "%{crate}" crate.

%package     -n %{name}+html_reports-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+html_reports-devel

This package contains library source intended for building other packages which
use the "html_reports" feature of the "%{crate}" crate.

%package     -n %{name}+real_blackbox-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+real_blackbox-devel

This package contains library source intended for building other packages which
use the "real_blackbox" feature of the "%{crate}" crate.

%package     -n %{name}+tinytemplate-devel
Summary:        Statistics-driven micro-benchmarking library
BuildArch:      noarch
%description -n %{name}+tinytemplate-devel

This package contains library source intended for building other packages which
use the "tinytemplate" feature of the "%{crate}" crate.

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
%files -n rust-criterion0.2-devel -f %{oreon_filedir}/rust-criterion0.2-devel.list

%changelog

%autochangelog
