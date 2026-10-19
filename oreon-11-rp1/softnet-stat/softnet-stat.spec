%global source0_hash 76ca692e32e67fbdb4a850cfd78eb82d5d2fdd901f7707314e6c870601c3629d
%bcond check 0
Name:           softnet-stat
Version:        2.1.0
Release:        1%{?dist}
Summary:        Parse the `/proc/net/softnet_stat` file into something more readable
License:        GPL-3.0-or-later
URL:            https://github.com/hjr3/softnet-stat
Source0:        https://github.com/hjr3/softnet-stat/archive/refs/tags/v%{version}.tar.gz
ExclusiveArch:  %{rust_arches}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n softnet-stat-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
