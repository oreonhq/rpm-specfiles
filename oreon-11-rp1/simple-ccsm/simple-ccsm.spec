%global source0_hash 71c17ee00214fe04c8e1befff72bb3adf9f3fcb1eaabd2a56038d64ddde3eb0a
%global basever 0.8.18
Name:           simple-ccsm
Version:        0.8.18
Release:        1%{?dist}
Summary:        Simple settings manager for Compiz
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch
Requires:       compiz-plugins-main >= %{basever}
Requires:       ccsm >= %{basever}
Requires:       python3-cairo
Requires:       compizconfig-python
Requires:       python3-gobject
Recommends:     compiz-plugins-extra >= %{basever}
Patch:          simple-ccsm-0.8.18-wheel-fix.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-simple-ccsm = %{version}-%{release}
# /oreon:deps
%description
Compiz settings manager focused on simplicity for an end-user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_datadir}/{metainfo,appdata}/
fdupes -s %{buildroot}%{_datadir}/
desktop-file-install                              \
    --delete-original                             \
    --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files

%changelog

%autochangelog
