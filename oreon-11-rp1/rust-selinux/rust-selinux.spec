%global source0_hash 7f4d7a0c34b924081f7fbdcb93121399f0d4182c0ec4bf9c01bfe4e7e21fcf16
%bcond check 1
%global debug_package %{nil}
%global crate selinux
Name:           rust-selinux
Version:        0.6.0
Release:        1%{?dist}
Summary:        Flexible Mandatory Access Control for Linux
License:        MIT
URL:            https://crates.io/crates/selinux
Source0:        https://static.crates.io/crates/selinux/selinux-%{version}.crate
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
Summary:        Flexible Mandatory Access Control for Linux
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip avc::tests::access_vector_cache_
    --skip label::tests::labeler_
    --skip policy::tests::set_root_path
    --skip tests::se_user_and_level
    --skip tests::security_class_new
    --skip tests::security_context_
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-selinux-devel -f %{oreon_filedir}/rust-selinux-devel.list

%changelog

%autochangelog
