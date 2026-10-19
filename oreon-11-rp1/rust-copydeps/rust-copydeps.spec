%global source0_hash b0d7e2c92c4aac73d1f3536edfffc6a290d065d6e3996447861b7c1bf33a810b
%bcond check 0
%global crate copydeps
Name:           rust-copydeps
Version:        5.0.1
Release:        1%{?dist}
Summary:        Find and copy all the .so / .dll files needed by an executable
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/copydeps
Source0:        https://static.crates.io/crates/copydeps/copydeps-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Find and copy all the .so / .dll files needed by an executable
License:        GPL-3.0-or-later AND MIT AND Unicode-DFS-2016 AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
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
install -m 644 -Dp misc/%{crate}.man %{buildroot}%{_mandir}/man1/%{crate}.1
install -m 644 -Dp misc/%{crate}.bash-completion %{buildroot}%{bash_completions_dir}/%{crate}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n copydeps -f %{oreon_filedir}/copydeps.list

%changelog

%autochangelog
