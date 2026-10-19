%global source0_hash 4d37f49a35de5ac23d88a61180d663ba3c2da089418818a588de31f9e920f8d6
Name:           ternimal
Version:        0.1.0
Release:        1%{?dist}
Summary:        Simulate a lifeform in the terminal
License:        GPL-3.0-or-later
URL:            https://github.com/p-e-w/ternimal
Source0:        https://github.com/p-e-w/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{rust_arches}
# oreon:deps
BuildRequires:  cargo-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

rustc %{build_rustflags} ternimal.rs -o ternimal
%install
install -Dpm0755 -t %{buildroot}%{_bindir} ternimal
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
