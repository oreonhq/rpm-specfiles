%global source0_hash 7f78c730aaa7d0b9336a299029ea49f9ee53b0ed06e9202e8cb7db9bae7b8c82
%bcond check 0
%global debug_package %{nil}
%global crate link-cplusplus
Name:           rust-link-cplusplus
Version:        1.0.12
Release:        1%{?dist}
Summary:        Link libstdc++ or libc++ automatically or manually
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/link-cplusplus
Source0:        https://static.crates.io/crates/link-cplusplus/link-cplusplus-%{version}.crate
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
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libc++-devel
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+libc++-devel

This package contains library source intended for building other packages which
use the "libc++" feature of the "%{crate}" crate.

%package     -n %{name}+libcxx-devel
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+libcxx-devel

This package contains library source intended for building other packages which
use the "libcxx" feature of the "%{crate}" crate.

%package     -n %{name}+libstdc++-devel
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+libstdc++-devel

This package contains library source intended for building other packages which
use the "libstdc++" feature of the "%{crate}" crate.

%package     -n %{name}+libstdcxx-devel
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+libstdcxx-devel

This package contains library source intended for building other packages which
use the "libstdcxx" feature of the "%{crate}" crate.

%package     -n %{name}+nothing-devel
Summary:        Link libstdc++ or libc++ automatically or manually
BuildArch:      noarch
%description -n %{name}+nothing-devel

This package contains library source intended for building other packages which
use the "nothing" feature of the "%{crate}" crate.

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
%files -n rust-link-cplusplus-devel -f %{oreon_filedir}/rust-link-cplusplus-devel.list

%changelog

%autochangelog
