%global source0_hash 44eaca382e94505a49f1a4849658d153aebf79d9c1a58e5dd3b10361511e9f43
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-aws-v4
Name:           rust-reqsign-aws-v4
Version:        3.0.0
Release:        1%{?dist}
Summary:        AWS SigV4 signing implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-aws-v4
Source0:        https://static.crates.io/crates/reqsign-aws-v4/reqsign-aws-v4-%{version}.crate
Patch:          reqsign-aws-v4-fix-metadata.diff
Patch10:        reqsign-aws-v4-2.0.0-unwanted-dev-deps.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  python3-devel
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
Summary:        AWS SigV4 signing implementation for reqsign
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%{py3_shebang_fix} tests/mocks
find tests/mocks -type f ! -executable -exec sed -r -i '1{/^#!/d}' '{}' '+'
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
find %{buildroot}%{crate_instdir}/tests/mocks -type f -executable \
    -exec chmod -v a-x '{}' '+' -exec sed -r -i '1{/^#!/d}' '{}' '+'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

export PYTHONDONTWRITEBYTECODE=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-reqsign-aws-v4-devel -f %{oreon_filedir}/rust-reqsign-aws-v4-devel.list

%changelog

%autochangelog
