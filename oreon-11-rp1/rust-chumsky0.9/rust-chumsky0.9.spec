%global source0_hash 8eebd66744a15ded14960ab4ccdbfb51ad3b81f51f3f04a80adac98c985396c9
%bcond check 0
%global debug_package %{nil}
%global crate chumsky
Name:           rust-chumsky0.9
Version:        0.9.3
Release:        1%{?dist}
Summary:        Parser library for humans with powerful error recovery
License:        MIT
URL:            https://crates.io/crates/chumsky
Source0:        https://static.crates.io/crates/chumsky/chumsky-%{version}.crate
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
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+spill-stack-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+spill-stack-devel

This package contains library source intended for building other packages which
use the "spill-stack" feature of the "%{crate}" crate.

%package     -n %{name}+stacker-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+stacker-devel

This package contains library source intended for building other packages which
use the "stacker" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-chumsky0.9-devel -f %{oreon_filedir}/rust-chumsky0.9-devel.list

%changelog

%autochangelog
