%global source0_hash a81ea3136ddc88e19c2cc2eb3176b72abee4e831367cd8949f2a88ac5497e64e
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate trycmd
Name:           rust-trycmd0.15
Version:        0.15.11
Release:        1%{?dist}
Summary:        Snapshot testing for a herd of CLI tests
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/trycmd
Source0:        https://static.crates.io/crates/trycmd/trycmd-%{version}.crate
Patch:          trycmd-fix-metadata.diff
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
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+color-auto-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+color-auto-devel

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+escargot-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+escargot-devel

This package contains library source intended for building other packages which
use the "escargot" feature of the "%{crate}" crate.

%package     -n %{name}+examples-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+examples-devel

This package contains library source intended for building other packages which
use the "examples" feature of the "%{crate}" crate.

%package     -n %{name}+filesystem-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+filesystem-devel

This package contains library source intended for building other packages which
use the "filesystem" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        Snapshot testing for a herd of CLI tests
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f schema
%install
%cargo_install -f schema
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f schema
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-trycmd0.15-devel -f %{oreon_filedir}/rust-trycmd0.15-devel.list

%changelog

%autochangelog
