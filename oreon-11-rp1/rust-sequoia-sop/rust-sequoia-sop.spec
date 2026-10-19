%global source0_hash e04e8d600a1af255e2055b3bbdb8f506da4eb6ef78fdaa54112180b760d10e11
%bcond check 1
%global crate sequoia-sop
Name:           rust-sequoia-sop
Version:        0.37.3
Release:        1%{?dist}
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-sop
Source0:        https://static.crates.io/crates/sequoia-sop/sequoia-sop-%{version}.crate
Patch:          sequoia-sop-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
License:        %{shrink:
    GPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    LGPL-2.0-or-later AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
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
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+cliv-devel
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+cliv-devel

This package contains library source intended for building other packages which
use the "cliv" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-nettle-devel
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+crypto-nettle-devel

This package contains library source intended for building other packages which
use the "crypto-nettle" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-openssl-devel
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+crypto-openssl-devel

This package contains library source intended for building other packages which
use the "crypto-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-rust-devel
Summary:        Implementation of the Stateless OpenPGP Interface using Sequoia
BuildArch:      noarch
%description -n %{name}+crypto-rust-devel

This package contains library source intended for building other packages which
use the "crypto-rust" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

export ASSET_OUT_DIR=target/assets
%cargo_build -f cli,cliv
%{cargo_license_summary -f cli,cliv}
%{cargo_license -f cli,cliv} > LICENSE.dependencies
%install
%cargo_install -f cli,cliv
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/assets/man-pages/sqop*.1 %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/assets/shell-completions/sqop.bash \
    %{buildroot}/%{bash_completions_dir}/sqop.bash
install -Dpm 0644 target/assets/shell-completions/sqopv.bash \
    %{buildroot}/%{bash_completions_dir}/sqopv.bash
install -Dpm 0644 target/assets/shell-completions/sqop.fish \
    %{buildroot}/%{fish_completions_dir}/sqop.fish
install -Dpm 0644 target/assets/shell-completions/sqopv.fish \
    %{buildroot}/%{fish_completions_dir}/sqopv.fish
install -Dpm 0644 target/assets/shell-completions/_sqop \
    %{buildroot}/%{zsh_completions_dir}/_sqop
install -Dpm 0644 target/assets/shell-completions/_sqopv \
    %{buildroot}/%{zsh_completions_dir}/_sqopv
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f cli,cliv
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-sop -f %{oreon_filedir}/sequoia-sop.list
%files -n rust-sequoia-sop-devel -f %{oreon_filedir}/rust-sequoia-sop-devel.list

%changelog

%autochangelog
