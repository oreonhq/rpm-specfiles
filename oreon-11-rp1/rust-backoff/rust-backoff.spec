%global source0_hash b62ddb9cb1ec0a098ad4bbf9344d0713fa193ae1a80af55febcff2627b6a00c1
%bcond check 1
%global debug_package %{nil}
%global crate backoff
Name:           rust-backoff
Version:        0.4.0
Release:        1%{?dist}
Summary:        Retry operations with exponential backoff policy
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/backoff
Source0:        https://static.crates.io/crates/backoff/backoff-%{version}.crate
Patch:          backoff-fix-metadata.diff
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
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async_std_1-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+async_std_1-devel

This package contains library source intended for building other packages which
use the "async_std_1" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+pin-project-lite-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+pin-project-lite-devel

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio_1-devel
Summary:        Retry operations with exponential backoff policy
BuildArch:      noarch
%description -n %{name}+tokio_1-devel

This package contains library source intended for building other packages which
use the "tokio_1" feature of the "%{crate}" crate.

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
%files -n rust-backoff-devel -f %{oreon_filedir}/rust-backoff-devel.list

%changelog

%autochangelog
