%global source0_hash 8de56eb4784a2c5c1efede55a0f06fbf481bc12b42b355b9525c15db1e3581a8
%bcond check 0
%global debug_package %{nil}
%global crate snapbox
Name:           rust-snapbox
Version:        1.2.2
Release:        1%{?dist}
Summary:        Snapshot testing toolbox
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/snapbox
Source0:        https://static.crates.io/crates/snapbox/snapbox-%{version}.crate
Patch:          snapbox-fix-metadata-auto.diff
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
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%{_bindir}/snap-fixture
%package     -n %{name}+cmd-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+cmd-devel

This package contains library source intended for building other packages which
use the "cmd" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+color-auto-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+color-auto-devel

This package contains library source intended for building other packages which
use the "color-auto" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+detect-encoding-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+detect-encoding-devel

This package contains library source intended for building other packages which
use the "detect-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+dir-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+dir-devel

This package contains library source intended for building other packages which
use the "dir" feature of the "%{crate}" crate.

%package     -n %{name}+examples-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+examples-devel

This package contains library source intended for building other packages which
use the "examples" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+path-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+path-devel

This package contains library source intended for building other packages which
use the "path" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+structured-data-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+structured-data-devel

This package contains library source intended for building other packages which
use the "structured-data" feature of the "%{crate}" crate.

%package     -n %{name}+term-svg-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+term-svg-devel

This package contains library source intended for building other packages which
use the "term-svg" feature of the "%{crate}" crate.

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
%files -n rust-snapbox-devel -f %{oreon_filedir}/rust-snapbox-devel.list

%changelog

%autochangelog
