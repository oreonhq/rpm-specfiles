%global source0_hash 14840736bdc573461623d3065849d52b46cff42039de1810fba6a40395e461ec
%define debug_package %{nil}
%global _changelog_trimtime %(date +%s -d "1 year ago")
Name:    eric
Summary:        Python IDE
Version: 26.8
Release:        1%{?dist}
License: GPL-3.0-or-later
URL:     https://eric-ide.python-projects.org
Source0:        https://downloads.sourceforge.net/sourceforge/eric-ide/%{name}7-%{version}.tar.gz
Source30: eric-32.png
Source31: eric-48.png
Source32: eric-64.png
Patch100: eric7-23.9-defaults.patch
Patch101: eric7-25.6.1-python314.patch
BuildArch: noarch
ExclusiveArch: %{qt6_qtwebengine_arches} noarch
Provides: eric7 = %{version}-%{release}
Requires: python3-pyqt6
Requires: python3-pyqt6-charts
Requires: python3-pyqt6-webengine
Requires: python3-qscintilla-qt6
Requires: python3dist(pip)
Requires: python3dist(tomlkit)
Requires: python3dist(asttokens)
Requires: python3dist(editorconfig)
Requires: python3dist(pygments)
Requires: python3dist(parso)
Requires: python3dist(jedi)
Requires: python3dist(packaging)
Requires: python3dist(trove-classifiers)
Requires: python3dist(spdx-license-list)
Requires: python3dist(black)
Requires: python3dist(isort)
Requires: python3dist(coverage)
Requires: python3dist(semver)
Requires: python3dist(pipdeptree)
Requires: python3dist(watchdog)
Requires: python3dist(psutil)
Requires: python3dist(requests)
Recommends: python3dist(docutils)
Recommends: python3dist(markdown)
Recommends: python3dist(pyyaml)
Recommends: python3dist(chardet)
Recommends: python3dist(pyenchant)
Recommends: python3dist(wheel)
Recommends: python3dist(fido2)
Recommends: python3dist(pyusb)
Recommends: pyside6-tools
Recommends: qt6-assistant
Recommends: qt6-designer
Recommends: qt6-doctools
Recommends: qt6-linguist
Recommends: git-core
Recommends: mercurial
Recommends: subversion
Recommends: python3-docs
Recommends: qt6-doc-html
Recommends: qt6-qttranslations
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt6
BuildRequires:  python3-pyqt6-charts
BuildRequires:  python3-pyqt6-webengine
BuildRequires:  python3-qscintilla-qt6
BuildRequires:  python3dist(asttokens)
BuildRequires:  python3dist(black)
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(editorconfig)
BuildRequires:  python3dist(fido2)
BuildRequires:  python3dist(isort)
BuildRequires:  python3dist(jedi)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pipdeptree)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pyenchant)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pyusb)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(spdx-license-list)
BuildRequires:  python3dist(tomlkit)
BuildRequires:  python3dist(trove-classifiers)
BuildRequires:  python3dist(watchdog)
BuildRequires:  python3dist(wheel)
# /oreon:deps
%description
eric7 is a full featured Python IDE.

%prep
%global oreon_srcdir eric7-%{version}
%oreon_prep
%build

pushd eric/src
find eric7/ -name __init__.py | sed -e '/CycloneDX/d;s|/__init__.py||;s|/|.|g' > ../../eric.pkgs
popd
%install
%{__python3} install.py \
  -i %{buildroot}/ \
  -b %{_bindir} \
  -d %{python3_sitelib} \
  -z
install -m644 -p -D %{SOURCE30} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eric.png
install -m644 -p -D %{SOURCE32} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/eric.png
desktop-file-edit --remove-category=MicroPython %{buildroot}%{_datadir}/applications/eric7_mpy.desktop
%find_lang %{name} --with-qt --all-name
rm -fv  %{buildroot}%{_datadir}/appdata/eric7.appdata.xml
rm -rfv %{buildroot}%{_datadir}/icons/eric*
rm -fv  %{buildroot}%{python3_sitelib}/eric7/LICENSE.txt
sed -i -e 's|-i %{buildroot}/||' %{buildroot}%{python3_sitelib}/eric7/eric7install.json
%oreon_autofiles main

%check

%py3_check_import -f eric.pkgs
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/eric7.appdata.xml
test "$(grep '^Exec' %{buildroot}%{_datadir}/applications/eric7_ide.desktop)" = "Exec=%{_bindir}/eric7_ide"
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_browser.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_ide.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/eric7_mpy.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
