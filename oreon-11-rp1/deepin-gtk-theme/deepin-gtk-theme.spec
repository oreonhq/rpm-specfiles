%global source0_hash 25439e65a702b5c578c7ca494e5ca0fbc24f3178d38658fb324de5d408917822

Name:           deepin-gtk-theme
Version:        2020.06.10
Release:        %autorelease
Summary:        Deepin GTK Theme
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
%autochangelog
