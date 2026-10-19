%global source0_hash 9d47c1b176be1c0d4a4c16e94dcb55df9c893ee9d2ad6dbc09b4719d5b557645
%bcond check 1
%bcond pgtests %{undefined el9}
%global forgeurl https://github.com/atuinsh/atuin
Name:           atuin
Version:        18.11.0
Release:        1%{?dist}
Summary:        Magical shell history
SourceLicense:  MIT
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    BSD-3-Clause AND
    CDLA-Permissive-2.0 AND
    ISC AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR BSL-1.0 OR MIT) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (BSD-3-Clause OR Apache-2.0) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
%forgemeta
URL:            https://atuin.sh
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        atuin.sh.in
Patch:          atuin-relax-MSRV.patch
Patch:          atuin-remove-divan.patch
Patch:          atuin-Update-tiny-bip39.patch
Patch:          atuin-whoami2.patch
%if %{with check} && %{with pgtests}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        all-users
Summary:        atuin init script for all users
Requires:       atuin = %{version}-%{release}
BuildArch:      noarch
%description    all-users

This package contains the init script to enable atuin for all users.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgeautosetup -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
mkdir -p other_installs/shell_completion
for shell in bash fish zsh; do
  ./target/rpm/atuin gen-completions --shell ${shell} -o other_installs/shell_completion
done
mkdir -p other_installs/libexec/atuin
for shell in bash fish zsh; do
  ./target/rpm/atuin init ${shell} > other_installs/libexec/atuin/atuin-init.${shell}
done
mkdir -p other_installs/profile.d
sed "s|@ATUIN_SCRIPTS_DIR@|%{_libexecdir}/atuin|" %SOURCE1 > other_installs/profile.d/atuin.sh
%install
install -Dpm 0755 target/rpm/atuin -t %{buildroot}%{_bindir}
install -Dpm 0644 other_installs/shell_completion/atuin.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 other_installs/shell_completion/atuin.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 other_installs/shell_completion/_atuin -t %{buildroot}%{zsh_completions_dir}
for shell in bash fish zsh; do
  install -Dpm 0755 other_installs/libexec/atuin/atuin-init.${shell} %{buildroot}%{_libexecdir}/atuin/atuin-init.${shell}
done
install -Dpm 0755 other_installs/profile.d/atuin.sh %{buildroot}%{_sysconfdir}/profile.d/atuin.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%if %{with pgtests}
export PGTESTS_LOCALE="C.UTF-8"
export PGTESTS_USERS="atuin:pass"
export PGTESTS_DATABASES="atuin:atuin"
export PGTESTS_PORT=5432
%postgresql_tests_run
%cargo_test -a
%else
%cargo_test -a -- -- --skip sync --skip change_password --skip multi_user_test --skip registration
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
