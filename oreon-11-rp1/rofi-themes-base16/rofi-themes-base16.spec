%global source0_hash def47cf011755f073c3ef8d11bba2a070972adb7de0338def9950719f12f6f51

Name: rofi-themes-base16
Version: 0.1.0
Release: 12%{?dist}
Summary: Base16 themes for rofi
BuildArch: noarch

License: MIT
URL: https://github.com/jordiorlando/base16-rofi
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: rofi
Requires: rofi-themes

%description
A collection of base16 themes for rofi

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n base16-rofi-%{version}

# Remove executable bits from rasi and config files
# https://github.com/jordiorlando/base16-rofi/pull/16
chmod -x themes/*.rasi
chmod -x themes/*.config

%build

%install
mkdir -p %{buildroot}/%{_datadir}/rofi/themes
cp -rp themes/* %{buildroot}/%{_datadir}/rofi/themes

%files
%license LICENSE
%doc README.md
%{_datadir}/rofi/themes/base16-*

%changelog
%autochangelog
