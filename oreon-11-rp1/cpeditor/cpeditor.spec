%global source0_hash 0b4b7ee51f6ae6a135386a864e717249e7833cad70c6e1f515d7cf6cd07f5130

Name:           cpeditor
Version:        7.0.1
Release:        %autorelease
Summary:        The Missing Editor for Competitive Programmers

# Most source code of the application is under GPL-3.0-or-later, except:
# the following source code file:
# src/Editor/CodeEditor.cpp: GPL-3.0-or-later AND MIT
# src/Editor/CodeEditor.hpp: GPL-3.0-or-later AND MIT
# src/Editor/CodeEditorSideBar.cpp: GPL-3.0-or-later AND MIT
# src/Editor/CodeEditorSideBar.hpp: GPL-3.0-or-later AND MIT
# src/Editor/HighLighter.cpp: GPL-3.0-or-later AND MIT
# src/Editor/HighLighter.hpp: GPL-3.0-or-later AND MIT
# the following bundled third-party libraries:
# diff_match_patch - Apache-2.0
# lsp-cpp - Apache-2.0
# qhttp - MIT
# QtFindReplaceDialog - LGPL-2.1-only
# singleapplication - MIT (not sure)
License:        GPL-3.0-or-later AND Apache-2.0 AND LGPL-2.1-only AND MIT
URL:            https://cpeditor.org/
Source0:        https://github.com/cpeditor/cpeditor/releases/download/%{version}/cpeditor-%{version}-full-source.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  python3-devel
BuildRequires:  cmake(KF5SyntaxHighlighting)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

Provides:       bundled(singleapplication)
Provides:       bundled(QtFindReplaceDialog)
Provides:       bundled(lsp-cpp)
Provides:       bundled(qhttp)
Provides:       bundled(diff_match_patch)

%description
CP Editor is designed for competitive programming. It helps you focus on your
algorithms and automates compilation, execution and testing of your code. It can
fetch test cases from different platforms and submit solutions to Codeforces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cpeditor-%{version}-full-source

rm -r third_party/{extra-cmake-modules,syntax-highlighting}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \

%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/cpeditor
%{_datadir}/applications/cpeditor.desktop
%{_datadir}/icons/hicolor/512x512/apps/cpeditor.png
%{_datadir}/metainfo/cpeditor.appdata.xml
%dir %{_datadir}/cpeditor
%{_datadir}/cpeditor/translations/

%changelog
%autochangelog
