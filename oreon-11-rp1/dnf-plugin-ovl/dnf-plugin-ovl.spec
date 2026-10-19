%global source0_hash 9114d09fa02f7ec3f9b92b66cc81fc05801cc0df60c7c0c316094355c8016c3f
Name:    dnf-plugin-ovl
Version: 0.0.3
Release:        1%{?dist}
Summary:        DNF plugin to work around overlayfs issues
URL:     https://github.com/FlorianLudwig/dnf-plugin-ovl
License: GPL-2.0-only
Source0:        https://github.com/FlorianLudwig/dnf-plugin-ovl/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python3-dnf
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
Workaround to run dnf on overlayfs. A port of yum-plugin-ovl to dnf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
install -D -p ovl.py %{buildroot}/%{python3_sitelib}/dnf-plugins/ovl.py
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
