%global source0_hash 95c589f335db0f6aaa168a7cd27b1fc6920f5e1470c804f814d9cd6e62a0f70b
%bcond check 1
%global debug_package %{nil}
%global crate quickcheck
Name:           rust-quickcheck
Version:        1.1.0
Release:        1%{?dist}
Summary:        Automatic property based testing with shrinking
License:        Unlicense OR MIT
URL:            https://crates.io/crates/quickcheck
Source0:        https://static.crates.io/crates/quickcheck/quickcheck-%{version}.crate
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
Summary:        Automatic property based testing with shrinking
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+env_logger-devel
Summary:        Automatic property based testing with shrinking
BuildArch:      noarch
%description -n %{name}+env_logger-devel

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Automatic property based testing with shrinking
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Automatic property based testing with shrinking
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+use_logging-devel
Summary:        Automatic property based testing with shrinking
BuildArch:      noarch
%description -n %{name}+use_logging-devel

This package contains library source intended for building other packages which
use the "use_logging" feature of the "%{crate}" crate.

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
%files -n rust-quickcheck-devel -f %{oreon_filedir}/rust-quickcheck-devel.list

%changelog

%autochangelog
