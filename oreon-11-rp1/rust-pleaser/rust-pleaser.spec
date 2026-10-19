%global source0_hash b5d9bee5511888e370c6e894d05f98f283de2a26669ec4e225d198505f9052d7
%bcond check 0
%global crate pleaser
Name:           rust-pleaser
Version:        0.5.6
Release:        1%{?dist}
Summary:        Please, a polite regex-first sudo alternative
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/pleaser
Source0:        https://static.crates.io/crates/pleaser/pleaser-%{version}.crate
Patch0:         pleaser-0.5.6.file.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Please, a polite regex-first sudo alternative
License:        GPL-3.0-or-later AND Apache-2.0 AND MIT AND Unicode-DFS-2016
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Please, a polite regex-first sudo alternative
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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%{__install} -Dpm4755 -t %{buildroot}%{_bindir} target/release/please
%{__install} -Dpm4755 -t %{buildroot}%{_bindir} target/release/pleaseedit
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/please.1
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man5 man/please.ini.5
%{__install} -Dpm0644 -t %{buildroot}%{bash_completions_dir} completions/bash/please
%{__install} -Dpm0644 -t %{buildroot}%{zsh_completions_dir} completions/zsh/_please
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/please << EOF
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cat > $RPM_BUILD_ROOT/etc/pam.d/pleaseedit << EOF
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --tests -- --skip test::test_search_bin_default_sbin
%endif
%files -f %{oreon_filedir}/main.list
%files -n pleaser -f %{oreon_filedir}/pleaser.list
%files -n rust-pleaser-devel -f %{oreon_filedir}/rust-pleaser-devel.list

%changelog

%autochangelog
