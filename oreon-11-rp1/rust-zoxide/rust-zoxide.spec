%global source0_hash 88592ccf9081e6a3f915f785357c1a70c05c52ce0637afb5f9b67161eefc050c
%bcond check 1
%global crate zoxide
Name:           rust-zoxide
Version:        0.10.0
Release:        1%{?dist}
Summary:        Smarter cd command for your terminal
License:        MIT
URL:            https://crates.io/crates/zoxide
Source0:        https://static.crates.io/crates/zoxide/zoxide-%{version}.crate
Patch:          zoxide-fix-metadata-auto.diff
Patch:          zoxide-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/bash
BuildRequires:  /usr/bin/fish
BuildRequires:  /usr/bin/shellcheck
BuildRequires:  /usr/bin/zsh
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Smarter cd command for your terminal
License:        MIT AND MPL-2.0 AND (Apache-2.0 OR MIT) AND (MIT-0 OR Apache-2.0)
Recommends:     fzf
%if %{with check} && (0%{?__isa_bits} != 32 || %{defined fc41})
BuildRequires:  /usr/bin/fish
%endif
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm 644 man/man1/%{crate}*.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 644 contrib/completions/%{crate}.bash -t %{buildroot}/%{bash_completions_dir}/
%if 0%{?__isa_bits} != 32 || %{defined fc41}
install -Dpm 644 contrib/completions/%{crate}.fish -t %{buildroot}/%{fish_completions_dir}/
%endif
install -Dpm 644 contrib/completions/_%{crate} -t %{buildroot}/%{zsh_completions_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n zoxide -f %{oreon_filedir}/zoxide.list

%changelog

%autochangelog
