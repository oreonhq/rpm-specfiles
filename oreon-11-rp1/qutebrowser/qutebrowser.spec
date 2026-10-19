%global source0_hash c7f95884ea5e6675e584025bea55cff950c47d749aff7f415f68da03fcce0f92
%global srcname qutebrowser
Name:		%{srcname}
Version:	3.7.0
Release:        1%{?dist}
Summary:        A keyboard-driven, vim-like browser based on PyQt5 and QtWebEngine
License:	GPL-3.0-only
URL:		http://www.qutebrowser.org
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	qt6-qtbase
Requires:	qt6-qtdeclarative
Requires:	python3-pyqt6
Requires:	python3-jinja2
Requires:	python3-PyYAML
Requires:	(qt6-qtwebengine and python3-pyqt6-webengine)
Recommends:	qt6-qtwebengine-devtools
Recommends:	python3-pygments
Recommends:	python3-adblock
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-qutebrowser = %{version}-%{release}
# /oreon:deps
%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It’s based on
Python, PyQt5 and QtWebEngine and free software, licensed under the GPL.
It was inspired by other browsers/addons like dwb and Vimperator/Pentadactyl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}

%build

a2x -f manpage doc/qutebrowser.1.asciidoc
find . -type f -iname "*.py" -exec sed -i '1s_^#!/usr/bin/env python3$_#!/usr/bin/python3_' {} +
%pyproject_wheel
%install
%pyproject_install
desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	misc/org.%{srcname}.%{srcname}.desktop
install -Dm644 misc/org.qutebrowser.qutebrowser.appdata.xml -t %{buildroot}%{_datadir}/metainfo
install -Dm644 doc/%{srcname}.1 -t %{buildroot}%{_mandir}/man1
install -Dm644 qutebrowser/icons/qutebrowser.svg \
	-t "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps"
for i in 16 24 32 48 64 128 256 512; do
	install -Dm644 "qutebrowser/icons/qutebrowser-${i}x${i}.png" \
		"%{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/qutebrowser.png"
done
chmod 755 %{buildroot}%{python3_sitelib}/%{srcname}/__main__.py
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files

%changelog

%autochangelog
