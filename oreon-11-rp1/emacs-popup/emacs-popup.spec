%global source0_hash 2691e9f57f35f2e1b3ae514bd31af72a5950b8b99864704cfd1bd22b9ee3e352

%global pkg popup

Name:           emacs-%{pkg}
Version:        0.5.9
Release:        10%{?dist}
Summary:        Visual Popup Interface Library for Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/auto-complete/%{pkg}-el/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
Emacs.popup.el is a visual popup user interface library for Emacs. This provides
a basic API and common UI widgets such as popup tooltips and popup menus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-el-%{version}

%build
%{_emacs_bytecompile} %{pkg}.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

%files
%doc README.md
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
