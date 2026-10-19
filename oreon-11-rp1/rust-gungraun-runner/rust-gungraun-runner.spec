%global source0_hash 6da6487203fa53ae6b1c8fead642fe79a3199464b0dd1337635594d675a9ac05
%bcond check 1
%global crate gungraun-runner
Name:           rust-gungraun-runner
Version:        0.17.2
Release:        1%{?dist}
Summary:        Binary package needed by the Gungraun library
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/gungraun-runner
Source0:        https://static.crates.io/crates/gungraun-runner/gungraun-runner-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Binary package needed by the Gungraun library
License:        # FIXME
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Binary package needed by the Gungraun library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+api-devel
Summary:        Binary package needed by the Gungraun library
BuildArch:      noarch
%description -n %{name}+api-devel

This package contains library source intended for building other packages which
use the "api" feature of the "%{crate}" crate.

%package     -n %{name}+runner-devel
Summary:        Binary package needed by the Gungraun library
BuildArch:      noarch
%description -n %{name}+runner-devel

This package contains library source intended for building other packages which
use the "runner" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        Binary package needed by the Gungraun library
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

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
%files -n gungraun-runner -f %{oreon_filedir}/gungraun-runner.list
%files -n rust-gungraun-runner-devel -f %{oreon_filedir}/rust-gungraun-runner-devel.list

%changelog

%autochangelog
