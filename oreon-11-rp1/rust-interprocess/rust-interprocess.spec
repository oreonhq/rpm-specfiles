%global source0_hash 6cb02ffbf25e8ef0f4a95bff054eef75f6d1bf16919474cf2caa63b21997478a
%bcond check 1
%global debug_package %{nil}
%global crate interprocess
Name:           rust-interprocess
Version:        2.4.4
Release:        1%{?dist}
Summary:        Interprocess communication toolkit
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/interprocess
Source0:        https://static.crates.io/crates/interprocess/interprocess-%{version}.crate
Patch:          interprocess-fix-metadata-auto.diff
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
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+doc_cfg-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+doc_cfg-devel

This package contains library source intended for building other packages which
use the "doc_cfg" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Interprocess communication toolkit
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-interprocess-devel -f %{oreon_filedir}/rust-interprocess-devel.list

%changelog

%autochangelog
