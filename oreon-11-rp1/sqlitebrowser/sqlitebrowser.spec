%global source0_hash a5fa5acbe80201f3b45a39855870301554bd2f8fc06dfae583cdf4888c52e98f

%global commit ffe7e576c1c0f4b46ce710a79c89b6d7d9506e62
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           sqlitebrowser
Version:        3.13.1
Release:        5%{?commit:.git%shortcommit}%{?dist}
Summary:        Create, design, and edit SQLite database files

License:        GPL-3.0-or-later OR MPL-2.0
URL:            https://github.com/%{name}/%{name}
%if 0%{?commit:1}
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
# Fix sqlcipher detection
Patch0:         sqlitebrowser_sqlcipher.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qcustomplot-qt6-devel
BuildRequires:  qhexedit2-qt6-devel
BuildRequires:  sqlcipher-devel
BuildRequires:  qscintilla-qt6-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qt5compat-devel

Requires:       hicolor-icon-theme

%description
SQLite Database Browser is a high quality, visual, open source tool to create,
design, and edit database files compatible with SQLite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{version}
%endif
# Unbundle
rm -rf libs/{qcustomplot-source,qhexedit,qscintilla}

%build
%cmake \
    -DQT_MAJOR=Qt6 \
    -DENABLE_TESTING=1 \
    -DFORCE_INTERNAL_QCUSTOMPLOT=OFF \
    -DFORCE_INTERNAL_QHEXEDIT=OFF \
    -DQSCINTILLA_INCLUDE_DIR=%{_qt6_includedir} \
    -DQSCINTILLA_LIBRARY=%{_libdir}/libqscintilla2_qt6.so \
    -DQCustomPlot_LIBRARY=%{_libdir}/libqcustomplot-qt6.so \
    -DQHexEdit_INCLUDE_DIR=%{_includedir}/qhexedit2-qt6 \
    -DQHexEdit_LIBRARY=%{_libdir}/libqhexedit-qt6.so \
    -Dsqlcipher=ON
%cmake_build

%install
%cmake_install
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.desktop.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.desktop.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
%autochangelog
