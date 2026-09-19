%global source0_hash 71c17ee00214fe04c8e1befff72bb3adf9f3fcb1eaabd2a56038d64ddde3eb0a

%global basever 0.8.18

Name:           simple-ccsm
Version:        0.8.18
Release:        20%{?dist}
Summary:        Simple settings manager for Compiz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(compiz) >= %{basever}
BuildRequires:  pkgconfig(libcompizconfig) >= %{basever}
Requires:       compiz-plugins-main >= %{basever}
Requires:       ccsm >= %{basever}
Requires:       python3-cairo
Requires:       compizconfig-python
Requires:       python3-gobject
Recommends:     compiz-plugins-extra >= %{basever}
Patch:          simple-ccsm-0.8.18-wheel-fix.patch

%description
Compiz settings manager focused on simplicity for an end-user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -M

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

fdupes -s %{buildroot}%{_datadir}/

desktop-file-install                              \
    --delete-original                             \
    --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang -f %{pyproject_files}
%license COPYING
%doc AUTHORS README.md NEWS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
