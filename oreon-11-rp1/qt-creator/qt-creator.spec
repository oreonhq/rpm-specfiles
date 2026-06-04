%global source0_hash none

%define prerelease beta1

# We need avoid oython byte compiler to not crash over template .py file which
# is not a valid python file, only for the IDE
%global _python_bytecompile_errors_terminate_build 0

Name:           qt-creator
Version:        20.0.0
Release:        0.3%{?prerelease:.%prerelease}%{?dist}
Summary:        Cross-platform IDE for Qt

# 
ExcludeArch:    %{ix86}

License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://www.qt.io/ide/
Source0:        https://download.qt.io/%{?prerelease:development}%{?!prerelease:official}_releases/qtcreator/20.0/%{version}%{?prerelease:-%prerelease}/qt-creator-opensource-src-%{version}%{?prerelease:-%prerelease}.tar.xz
Source1:        qt-creator-Fedora-privlibs

# Fix leading whitespace in desktop file
Patch1:         qt-creator_desktop.patch
# Limit qmake names to avoid the rpm macro wrapper qmake-qt5.sh getting picked up (#1644989)
Patch2:         qt-creator_qmake-names.patch
# Fix debuginfod detection
Patch3:         qt-creator-debuginfod.patch

BuildRequires:  chrpath
BuildRequires:  cmake
#BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlModels)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6Quick3DAssetUtils)
BuildRequires:  cmake(Qt6QuickTimeline)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6WebSockets)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:	cmake(Qt6WebEngineWidgets)
%endif
# FIXME: qt6-qtdeclarative packaging bug?
# The imported target "Qt6::QmlDomPrivate" references the file
#    "/usr/lib64/libQt6QmlDom.a"
# but this file does not exist.
BuildRequires:  qt6-qtdeclarative-static
BuildRequires:  desktop-file-utils
BuildRequires:  diffutils
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-debuginfod-client-devel
# TODO, to remove -DBUILD_EXECUTABLE_CMDBRIDGE=OFF below
# BuildRequires:  golang-bin
# BuildRequires:  golang(github.com/fsnotify/fsnotify)
# BuildRequires:  golang(golang.org/x/sys)
# BuildRequires:  golang(github.com/fxamacker/cbor/v2)
BuildRequires:  libappstream-glib
BuildRequires:  libffi-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  litehtml-devel
BuildRequires:  libsecret-devel
BuildRequires:  ninja-build
BuildRequires:  python3
# tight dep on qt6-qtbase used to build, uses some private apis
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-mysql
BuildRequires:  qt6-qtbase-odbc
BuildRequires:  qt6-qtbase-postgresql
BuildRequires:  systemd-devel
BuildRequires:  yaml-cpp-devel

Requires:       hicolor-icon-theme
Requires:       xdg-utils

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Requires:       %{name}-translations = %{version}-%{release}

# we need gcc-c++ to compile programs using qt-creator
Recommends:       gcc-c++
Recommends:       gdb
Recommends:       cmake
Recommends:       git
Recommends:       qt6-qtbase-devel
Recommends:       qt6-doc

Provides:       qtcreator = %{version}-%{release}

# long list of private shared lib names to filter out
%include %{SOURCE1}
%global __provides_exclude ^(%{privlibs})\.so
%global __requires_exclude ^(%{privlibs})\.so


%description
Qt Creator is a cross-platform IDE (integrated development environment)
tailored to the needs of Qt developers.


%package data
Summary:        Application data for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
Application data for %{name}.


%package translations
Summary:        Translations for %{name}
Requires:       %{name}-data = %{version}-%{release}
Requires:       qt6-qttranslations
BuildArch:      noarch

%description translations
Translations for %{name}.


%package doc
Summary:        User documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
User documentation for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n qt-creator-opensource-src-%{version}%{?prerelease:-%prerelease}

# Remove some bundled libraries to be sure
rm -rf src/shared/qbs
rm -rf src/plugins/help/qlitehtml/litehtml
#rm -rf src/libs/3rdparty/syntax-highlighting/src
# rm -rf src/libs/3rdparty/yaml-cpp


%build
%cmake_qt6 \
    -DBUILD_PLUGIN_CLANGREFACTORING=ON \
    -DBUILD_PLUGIN_CLANGPCHMANAGER=ON \
    -DCLANGTOOLING_LINK_CLANG_DYLIB=ON \
    -DBUILD_EXECUTABLE_CMDBRIDGE=OFF \
    -DWITH_DOCS=ON \
    -Djournald=ON \
    -DBUILD_DEVELOPER_DOCS=ON \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%cmake_build -- qch_docs


%install
%cmake_install
%cmake_install --component qch_docs


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.qt-project.qtcreator.desktop
%if 0%{?fedora} || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.qt-project.qtcreator.appdata.xml
%endif
chrpath -l %{buildroot}%{_bindir}/qtcreator

# Output an up-to-date list of Provides/Requires exclude statements.
outfile=__Fedora-privlibs
i=0
sofiles=$(find %{buildroot}%{_libdir}/qtcreator -name \*.so\*|sed 's!^.*/\(.*\).so.*!\1!g'|sort|uniq)
for so in ${sofiles} ; do
    if [ $i == 0 ]; then
        echo "%%global privlibs $so" > $outfile
        i=1
    else
        echo "%%global privlibs %%{privlibs}|$so" >> $outfile
    fi
done
cat $outfile
# If there are differences, abort the build
diff -u %{SOURCE1} $outfile


%files
%doc README.md
%license LICENSES/LICENSE.GPL3-EXCEPT
%{_bindir}/qtcreator
%{_bindir}/qtcreator.sh
%{_libdir}/qtcreator
%{_libexecdir}/qtcreator/
%{_datadir}/applications/org.qt-project.qtcreator.desktop
%{_metainfodir}/org.qt-project.qtcreator.appdata.xml
%{_datadir}/icons/hicolor/*/apps/QtProject-qtcreator.png

%files data
%{_datadir}/qtcreator/
%exclude %{_datadir}/qtcreator/translations

%files translations
%{_datadir}/qtcreator/translations/

%files doc
# Please don't change this, it is where qt-creator expects the documentation to be!
%dir %{_defaultdocdir}/qtcreator/
%doc %{_defaultdocdir}/qtcreator/qtcreator.qch
%doc %{_defaultdocdir}/qtcreator/qtcreator-dev.qch


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20.0.0-0.3
- Import
