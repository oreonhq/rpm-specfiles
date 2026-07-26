%global source0_hash 581a6a9a333e6e8aedf710c702237f7ebf7da170a6c3c1712a9629ae0daddddb

Name:          whichfont
Version:       2.3.0
Release:       3%{?dist}
Summary:       Querying Fontconfig

License:       GPL-3.0-or-later
URL:           https://github.com/sudipshil9862/whichfont
Source0:       %{url}/archive/refs/tags/%{version}.tar.gz#/whichfont-%{version}.tar.gz

BuildRequires: fontconfig-devel
BuildRequires: meson
BuildRequires: gcc
BuildRequires: make

%description
Querying fontconfig for certain code point. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
