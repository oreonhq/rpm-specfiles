%global source0_hash 37653daab1324326caacea2d16ab93a0ecbf2b6be78e7acc1948aa4aeb73925b
Name:           cpeditor
Version:        7.1.1
Release:        1%{?dist}
Summary:        The Missing Editor for Competitive Programmers
License:        GPL-3.0-or-later AND Apache-2.0 AND LGPL-2.1-only AND MIT
URL:            https://cpeditor.org/
Source0:        https://github.com/cpeditor/cpeditor/releases/download/%{version}/cpeditor-%{version}-full-source.tar.gz
Requires:       hicolor-icon-theme
Provides:       bundled(singleapplication)
Provides:       bundled(QtFindReplaceDialog)
Provides:       bundled(lsp-cpp)
Provides:       bundled(qhttp)
Provides:       bundled(diff_match_patch)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
