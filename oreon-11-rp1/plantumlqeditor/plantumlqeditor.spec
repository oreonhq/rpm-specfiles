%global source0_hash faa6734b7689db0f31e7b05265efc6d3c6096f7d2eeedc30f5d85faf7858b1d9
%global date 20170403
%global commit0 964d4ef967618e0f43322ea4d4a67e74c06b13dd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:           plantumlqeditor
Version:        1.2.0
Release:        1%{?dist}
Summary:        Simple editor for PlantUML
License:        GPL-3.0-or-later
URL:            https://sourceforge.net/projects/plantumlqeditor/
Source0:        https://github.com/borco/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
Patch0:         %{name}-use-system-wide-qtsingleapplication-library.patch
Requires:       shared-mime-info
Requires:       hicolor-icon-theme
Requires:       graphviz
Requires:       plantuml
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  javapackages-filesystem
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qtsingleapplication-qt5-devel
# /oreon:deps
%description
PlantUML QEditor is a simple editor written in Qt5 for PlantUML.

At a glance:

- simple PlantUML editor, with a preview,
- update the diagram while editing,
- code assistant to insert ready-made code snippets,
- written in Qt5, so it should run on all platforms supported by Qt5 and
  PlantUML.

The editor is quite simple: it monitors the editor for changes, and, if any,
runs plantuml to regenerate the image.

The editor also supports an assistant that allows easy insertion of code
snippets into the editor. The assistant is defined by a simple XML and a bunch
of icons, one for each snippet.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n %{name}-%{commit0}
# remove bundled qtsingleapplication library sources
rm -rf thirdparty/qtsingleapplication

# Set the default configuration values
# so it's ready to use without any extra configuration steps
sed -i "s#/usr/bin/plantuml#%{_javadir}/plantuml.jar#g" settingsconstants.h
sed -i "s#\(reloadAssistantXml(settings.value(SETTINGS_ASSISTANT_XML_PATH\)\().toString());\)#\1, QVariant(\"%{_datadir}/%{name}/assistant.xml\")\2#g" mainwindow.cpp
sed -i "s#\"translations\"#\"%{_datadir}/%{name}/translations\"#g" main.cpp

%build

%{qmake_qt5}
%make_build
lrelease-qt5 translations/*.ts
%install
install -p -m 0755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 0644 -D assistant.xml %{buildroot}%{_datadir}/%{name}/assistant.xml
cp -ar icons %{buildroot}%{_datadir}/%{name}/
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{name}.desktop
install -p -m 0644 -D icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -p -m 0644 -D plantumlqeditor-mime.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml
mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
cp -a translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
%find_lang %{name} --with-qt --without-mo
install -p -m 0644 -D %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
