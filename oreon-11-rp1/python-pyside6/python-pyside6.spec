%global source0_hash cba47efbaad1bedd529725cbc14e21f156c7a19366f07b3edfbb076ffd7afdf8
%global toolchain clang
%global _python_bytecompile_errors_terminate_build 0
%global pypi_name pyside6
%global camel_name PySide6
%global qt6ver 6.11.2
Name:           python-%{pypi_name}
Version:        6.11.2
Release:        1%{?dist}
Summary:        Python bindings for the Qt 6 cross-platform application and UI framework
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://wiki.qt.io/Qt_for_Python
Source0:        https://download.qt.io/official_releases/QtForPython/%{pypi_name}/%{camel_name}-%{version}-src/pyside-setup-everywhere-src-%{version}.tar.xz
%global docs 0
%global qt_module qtbase
%global  majmin %(echo %{version} | cut -d. -f1-2)
Patch:          0001-Fix-header-installation-path-to-follow-filesystem-st.patch
Patch:          0001-Fix-header-packaging-and-include-path-regressions.patch
Patch:          0001-Always-link-to-python-libraries.patch
%if 0%{?docs}
%endif
%ifarch %{qt6_qtwebengine_arches}
%endif
# oreon:deps
BuildRequires:  /usr/bin/wlheadless-run
BuildRequires:  clang-devel
BuildRequires:  clang-tools-extra
BuildRequires:  cmake
BuildRequires:  cmake(Qt63DAnimation)
BuildRequires:  cmake(Qt63DCore)
BuildRequires:  cmake(Qt63DExtras)
BuildRequires:  cmake(Qt63DInput)
BuildRequires:  cmake(Qt63DLogic)
BuildRequires:  cmake(Qt63DRender)
BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6DataVisualization)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6HttpServer)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Nfc)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Quick3D)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6RemoteObjects)
BuildRequires:  cmake(Qt6Scxml)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6SerialBus)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6SpatialAudio)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  llvm-devel
BuildRequires:  mesa-dri-drivers
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-packaging
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-wheel
BuildRequires:  qt6-assistant
BuildRequires:  qt6-designer
BuildRequires:  qt6-doctools
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-mysql
BuildRequires:  qt6-qtbase-odbc
BuildRequires:  qt6-qtbase-postgresql
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
# /oreon:deps
%description
PySide6 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 6+ framework.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Provides:       python%{python3_pkgversion}-%{camel_name} = %{version}-%{release}
Summary:        Python bindings for the Qt 6 cross-platform application and UI framework
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{camel_name}}
%description -n python%{python3_pkgversion}-%{pypi_name}
PySide6 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 6 framework.

%package -n     python%{python3_pkgversion}-%{pypi_name}-devel
Requires:       pyside6-tools
Requires:       shiboken6
Summary:        Development files related to %{name}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-devel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{camel_name}-devel}
%description -n python%{python3_pkgversion}-%{pypi_name}-devel
%{summary}.

%package -n pyside6-tools
Requires:       qt6-qtbase-devel
Requires:       qt6-qtdeclarative-devel
Requires:       qt6-assistant
Requires:       qt6-designer
Requires:       qt6-linguist
Requires:       python3-%{pypi_name}
Summary:        PySide6 tools for the Qt 6 framework
%description -n pyside6-tools
PySide6 provides Python bindings for the Qt6 cross-platform application
and UI framework.

%package -n shiboken6
Summary:        Python / C++ bindings generator for %camel_name
%description -n shiboken6
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

%package -n python%{python3_pkgversion}-shiboken6
Summary:        Python / C++ bindings libraries for %camel_name
%description -n python%{python3_pkgversion}-shiboken6
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

%package -n python%{python3_pkgversion}-shiboken6-devel
Summary:        Python / C++ bindings helper module for %camel_name
Requires:       shiboken6
Requires:       python%{python3_pkgversion}-shiboken6
%description -n python%{python3_pkgversion}-shiboken6-devel
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

%if 0%{?docs}
%package doc
Summary: Qt API Documentation in HTML and QCH format
%description doc
%{summary}.
%endif

%prep

%autosetup -p1 -n pyside-setup-everywhere-src-%{qt6ver}
# https://build.opensuse.org/package/view_file/KDE:Qt6/python3-pyside6/python3-pyside6.spec?expand=1
# Restore 6.6.1 RPATH value. rpmlint will complain otherwise
sed -i 's#${base}/../shiboken6/##' sources/pyside6/CMakeLists.txt

%if 0%{?docs}
# Generate documentation, requires qtbase sources as parameter
# sphinx-build output accepts several options of the format, default is html, use qthelp which calls qhelpgenerator for qch file generation
tar xf %{SOURCE1}
%endif

%build

%cmake_qt6 %["%{?_lib}" == "lib64" ? "-DLIB_SUFFIX=64" : ""] \
    -DCMAKE_BUILD_TYPE=None \
    -DSHIBOKEN_PYTHON_LIBRARIES=`pkgconf python3-embed --libs` \
    -DBUILD_TESTS=OFF \
    -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DFORCE_LIMITED_API=no \
%if 0%{?docs}
    -DBUILD_DOCS:BOOL=ON \
    -DQT_SRC_DIR= %{qt_module}-everywhere-src-%{qt6ver} \
    -DFULLDOCSBUILD:BOOL=ON \
    -DDOC_OUTPUT_FORMAT=qthelp \
%endif
    -DNO_QT_TOOLS=yes
TODAY=$(date -Id)
mkdir build_history/$TODAY
echo $PWD/%{_vpath_builddir}/sources > build_history/$TODAY/build_dir.txt
export PYTHONPATH=$PWD/%{_vpath_builddir}/sources
%cmake_build
%if 0%{?docs}
cd %{_vpath_builddir}
ninja apidoc
%endif
%install
%cmake_install
%if 0%{?docs}
cd %{_vpath_builddir}
ninja apidocinstall
%endif
cp %{_vpath_builddir}/sources/shiboken6/shibokenmodule/{*.py,*.txt} sources/shiboken6/shibokenmodule/
cp %{_vpath_builddir}/sources/pyside6/PySide6/*.py sources/pyside6/PySide6/
%{__python3} setup.py --qtpaths=/usr/%{_lib}/qt6/bin/qtpaths install_scripts --install-dir=%{buildroot}%{_bindir}
for name in PySide6 shiboken6 shiboken6_generator; do
  mkdir -p %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info
  cp -p $name.egg-info/{PKG-INFO,top_level.txt} \
        %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  if [ -f $name.egg-info/entry_points.txt ]; then
    cp -p $name.egg-info/entry_points.txt %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  fi
done
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec
ln -sf /usr/%{_lib}/qt6/libexec/{qmlcachegen,qmlimportscanner,qmltyperegistrar,rcc,uic} %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec
ln -sf /usr/%{_lib}/qt6/bin/{assistant,balsam,balsamui,designer,linguist,lrelease,lupdate,qmlformat,qmllint,qmlls,qsb} %{buildroot}%{python3_sitelib}/%{camel_name}
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mv %{buildroot}%{_bindir}/{android_deploy.py,deploy_lib,deploy.py,metaobjectdump.py,project_lib,project.py,pyside_tool.py,qml.py,qtpy2cpp_lib,qtpy2cpp.py,requirements-android.txt} %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mkdir -p %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts
mv %{buildroot}%{_bindir}/shiboken_tool.py %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts
mv %{_vpath_builddir}/sources/shiboken6_generator/generator/shiboken6 %{buildroot}%{python3_sitelib}/shiboken6_generator
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
%py3_shebang_fix %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts
grep -rl 'share/PySide6/share/PySide6/typesystems' %{buildroot}%{_libdir}/cmake/PySide6/ | xargs -r sed -i 's|share/PySide6/share/PySide6/typesystems|share/PySide6/typesystems|g'
%oreon_autofiles pyside6-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles shiboken6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
%py3_check_import PySide6
%py3_check_import shiboken6
%files -f %{oreon_filedir}/main.list
%files -n python3-pyside6 -f %{oreon_filedir}/python3-pyside6.list
%files -n python3-pyside6-devel -f %{oreon_filedir}/python3-pyside6-devel.list
%files -n pyside6-tools -f %{oreon_filedir}/pyside6-tools.list
%files -n shiboken6 -f %{oreon_filedir}/shiboken6.list
%files -n python3-shiboken6 -f %{oreon_filedir}/python3-shiboken6.list
%files -n python3-shiboken6-devel -f %{oreon_filedir}/python3-shiboken6-devel.list

%changelog

* Tue Aug 25 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.2-1
- 6.11.2

* Wed Jul 22 2026 Python Maint <python-maint@redhat.com> - 6.11.1-6
- Rebuilt for Python 3.15.0b4 ABI change

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Jun 08 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.1-4
- Remove cmake config path sed and replace patches with upstream cherry-picks

* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 6.11.1-3
- Rebuilt for Python 3.15

* Thu May 14 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.1-2
- Remove cmake config file fix

* Wed May 13 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.1-1
- Update to 6.11.1

* Thu Apr 16 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.0-2
- Restore shiboken6_generator

* Wed Apr 15 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.0-1
- Update to 6.11.0

* Thu Apr 02 2026 Jan Grulich <jgrulich@redhat.com> - 6.10.3-1
- 6.10.3

* Tue Feb 10 2026 Jan Grulich <jgrulich@redhat.com> - 6.10.2-1
- 6.10.2

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Dec 02 2025 Jan Grulich <jgrulich@redhat.com> - 6.10.1-2
- Fix cmake config files

* Mon Dec 01 2025 Jan Grulich <jgrulich@redhat.com> - 6.10.1-1
- 6.10.1

* Sat Nov 22 2025 Jan Grulich <jgrulich@redhat.com> - 6.9.2-4
- Rebuild (qt6)

* Tue Sep 30 2025 Jan Grulich <jgrulich@redhat.com> - 6.9.2-3
- Rebuild (qt6)

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 6.9.2-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Mon Sep 01 2025 Jan Grulich <jgrulich@redhat.com> - 6.9.2-1
- 6.9.2

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 6.9.1-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 08 2025 Python Maint <python-maint@redhat.com> - 6.9.1-2
- Rebuilt for Python 3.14

* Fri Jun 06 2025 Jan Grulich <jgrulich@redhat.com> - 6.9.1-1
- 6.9.1

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 6.9.0-2
- Rebuilt for Python 3.14

* Wed Apr 02 2025 Jan Grulich <jgrulich@redhat.com> - 6.9.0-1
- 6.9.0

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 6.8.2.1-3
- Rebuild (qt6)

* Sun Mar 16 2025 Marie Loise Nolden <loise@kde.org> - 6.8.2.1-2
- fix build due to %cmake macro change after removal of -DLIB_SUFFIX in rawhide
- prepare documentation build

* Fri Feb 07 2025 Marie Loise Nolden <loise@kde.org> - 6.8.2.1-1
- 6.8.2.1

* Mon Feb 03 2025 Jan Grulich <jgrulich@redhat.com> - 6.8.1.1-3
- Rebuild (qt6)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 05 2025 Marie Loise Nolden <loise@kde.org> - 6.8.1-1
- 6.8.1.1

* Sun Dec 08 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.0-2
- Rebuild (qt6.8.1)

* Tue Oct 15 2024 Jan Grulich <jgrulich@redhat.com> - 6.8.0-1
- 6.8.0

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.2-5
- Rebuild (qt6)

* Fri Aug 09 2024 Federico Pellegrin <fede@evolware.org> - 6.7.2-4
- Fix pyside6-tools dependencies on python3-pyside

* Wed Jul 31 2024 LuK1337 <priv.luk@gmail.com> - 6.7.2-3
- unbreak python console scripts

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 LuK1337 <priv.luk@gmail.com> - 6.7.2-1
- 6.7.2

* Tue Jun 18 2024 LuK1337 <priv.luk@gmail.com> - 6.7.1-3
- fix Python 3.13 build

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 6.7.1-2
- Rebuilt for Python 3.13

* Wed May 29 2024 LuK1337 <priv.luk@gmail.com> - 6.7.1-1
- 6.7.1

* Fri Apr 12 2024 Jan Grulich <jgrulich@redhat.com> - 6.7.0-1
- 6.7.0

* Sun Mar 24 2024 Marie Loise Nolden <loise@kde.org> - 6.6.2-2
- add  -DFORCE_LIMITED_API=no for freecad building (thanks to nvwarr@hotmail.com) (in rhbz #2266591)
- set toolchain to clang for correct build (rhbz #2271188)

* Mon Feb 19 2024 Marie Loise Nolden <loise@kde.org> - 6.6.2-1
- Initial package
