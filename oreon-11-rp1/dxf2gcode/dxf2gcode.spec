%global source0_hash c7b634f1573c1ad154820c3b9218cdd96920e1181ff331ef7a6cf96f2be97f7f

%{?python_enable_dependency_generator}
%global date 20240509
%global vdate %(x=%{date}; echo "${x:0:4}-${x:4:2}-${x:6:2}")
%global py_setup st-setup.py

Name:           dxf2gcode
Version:        %{date}
Release:        11%{?dist}
Summary:        2D drawings to CNC machine compatible G-Code converter
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
Url:            https://sourceforge.net/p/dxf2gcode/wiki/Home/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  /usr/bin/git
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  qt5-linguist
BuildRequires:  /usr/bin/pyuic5
BuildRequires:  /usr/bin/pyrcc5

Requires:       /usr/bin/pdftops
Requires:       /usr/bin/pstoedit
Requires:       hicolor-icon-theme

%description
%{name} is a tool for converting 2D (DXF, PDF, PS) drawings to CNC machine
compatible GCode. It has the following features:
    - Integration in EMC2,
    - Fully adjustable Postprocessor,
    - G0 moves reduction by route optimization,
    - Import of DXF and PDF,
    - Improved accuracy for splines import by Line and Arc's,
    - Mill parameter specification by layers,
    - Drag knife and lathe support,
    - Breaks a.k.a Tabs support,
    - AutoCAD Blocks and Inserts,
    - Multiple tools,
    - Multiple language support: English, German, French, Russian,
    - 3D viewer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git
# Original setup.py file is for windows platform only
cp -af st-setup.py setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
# regenerate *images5_rc.py and *ui5.py files
python3 ./make_py_uic.py 5
# regenerate translation files
lrelease-qt5 i18n/*.ts
%pyproject_wheel

%install
%pyproject_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%license COPYING
%doc README.txt
%{_bindir}/%{name}
%{python3_sitelib}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/*.appdata.xml

%changelog
%autochangelog
