%global source0_hash 4d37f49a35de5ac23d88a61180d663ba3c2da089418818a588de31f9e920f8d6

Name:           ternimal
Version:        0.1.0
Release:        21%{?dist}
Summary:        Simulate a lifeform in the terminal

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/p-e-w/ternimal
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
rustc %{build_rustflags} ternimal.rs -o ternimal

%install
install -Dpm0755 -t %{buildroot}%{_bindir} ternimal

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/ternimal

%changelog
%autochangelog
