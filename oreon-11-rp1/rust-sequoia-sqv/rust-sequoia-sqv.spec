%global source0_hash d4eb1f22746894dd654a8fa50576200d047f0de0e1ae2a361d7ebe263d351bc8
%bcond check 1
%global crate sequoia-sqv
Name:           rust-sequoia-sqv
Version:        1.5.0
Release:        1%{?dist}
Summary:        Simple OpenPGP signature verification program
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-sqv
Source0:        https://static.crates.io/crates/sequoia-sqv/sequoia-sqv-%{version}.crate
Patch:          sequoia-sqv-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Simple OpenPGP signature verification program
License:        %{shrink:
    LGPL-2.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    MIT AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

export ASSET_OUT_DIR=target/assets
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/assets/man-pages/sqv*.1 %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/assets/shell-completions/sqv.bash \
    %{buildroot}/%{bash_completions_dir}/sqv.bash
install -Dpm 0644 target/assets/shell-completions/sqv.fish \
    %{buildroot}/%{fish_completions_dir}/sqv.fish
install -Dpm 0644 target/assets/shell-completions/_sqv \
    %{buildroot}/%{zsh_completions_dir}/_sqv
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-sqv -f %{oreon_filedir}/sequoia-sqv.list

%changelog

%autochangelog
