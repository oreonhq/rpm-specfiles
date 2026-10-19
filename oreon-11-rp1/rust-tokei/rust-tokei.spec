%global source0_hash cee2d8d958bbbe166867f95c85eb95ce0c67cdf6377ef8cd3186ce843c3f752c
%bcond check 1
%global crate tokei
Name:           rust-tokei
Version:        15.0.0
Release:        1%{?dist}
Summary:        Count your code, quickly
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokei
Source0:        https://static.crates.io/crates/tokei/tokei-%{version}.crate
Source10:       tokei.1
Patch:          tokei-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Count your code, quickly
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    BSD-3-Clause AND
    MIT AND
    MPL-2.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Count your code, quickly
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        Count your code, quickly
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+cbor-devel
Summary:        Count your code, quickly
BuildArch:      noarch
%description -n %{name}+cbor-devel

This package contains library source intended for building other packages which
use the "cbor" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Count your code, quickly
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        Count your code, quickly
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%install
%cargo_install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE10}'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -a -- -- --exact %{shrink:
    --skip language::language_type::tests::jupyter_notebook_has_correct_totals
    --skip language::language_type::tests::lf_embedded_language_is_counted
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n tokei -f %{oreon_filedir}/tokei.list
%files -n rust-tokei-devel -f %{oreon_filedir}/rust-tokei-devel.list

%changelog

%autochangelog
