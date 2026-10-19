%global source0_hash 83a0692ec44e4cf1ef28ca317f14f8f07da2d95ec3fa01f86e4467b725e60917
%bcond check 1
%global debug_package %{nil}
%global crate pbkdf2
Name:           rust-pbkdf2_0.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Generic implementation of PBKDF2
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pbkdf2
Source0:        https://static.crates.io/crates/pbkdf2/pbkdf2-%{version}.crate
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
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+hmac-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+hmac-devel

This package contains library source intended for building other packages which
use the "hmac" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+password-hash-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+password-hash-devel

This package contains library source intended for building other packages which
use the "password-hash" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+simple-devel
Summary:        Generic implementation of PBKDF2
BuildArch:      noarch
%description -n %{name}+simple-devel

This package contains library source intended for building other packages which
use the "simple" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic implementation of PBKDF2
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
%files -n rust-pbkdf2_0.11-devel -f %{oreon_filedir}/rust-pbkdf2_0.11-devel.list

%changelog

%autochangelog
