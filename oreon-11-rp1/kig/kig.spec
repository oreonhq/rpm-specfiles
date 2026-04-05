%global _python3_include %(%{__python3} -Ic "from distutils.sysconfig import get_python_inc; print(get_python_inc())")
%global _python3_lib /usr/%{_lib}/lib%(basename %{_python3_include}).so


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kig
Summary: Interactive Geometry 
Version: 25.12.3
Release:	2%{?dist}

License: BSD-3-Clause AND GFDL-1.2-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-or-later
URL:     https://invent.kde.org/education/%{name}

Source0: http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

## upstream patches

BuildRequires: boost-devel
BuildRequires: boost-python3
BuildRequires: python3
BuildRequires: python3-rpm-macros
BuildRequires: python3-devel
# Added below for https://bugzilla.redhat.com/show_bug.cgi?id=2154864
BuildRequires: (python3-setuptools if python3-devel >= 3.12)

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6CoreAddons)

BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6PrintSupport)

# when split occurred
Conflicts: kdeedu-math < 4.7.0-10

%description
%{summary}.


%prep
%autosetup -p1

%py3_shebang_fix pykig/pykig.py


%build
%cmake_kf6 \
  -DPYTHON_EXECUTABLE:PATH=%{__python3} \
  -DPYTHON_INCLUDE_DIR=%{_python3_include} \
  -DPYTHON_LIBRARY=%{_python3_lib} \
  -DBoostPython_INCLUDE_DIRS="%{_python3_include};%{_includedir}/boost" \
%if 0%{?fedora} || 0%{?rhel} >= 9
  -DBoostPython_LIBRARIES="%{_python3_lib};%{_libdir}/libboost_python%{python3_version_nodots}.so"
%else
  -DBoostPython_LIBRARIES="%{_python3_lib};%{_libdir}/libboost_python3.so"
%endif

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}*
%{_kf6_bindir}/pykig.*
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_plugindir}/parts/kigpart.so
%{_kf6_datadir}/katepart5/syntax/python-kig.xml
%{_kf6_datadir}/metainfo/org.kde.%{name}.metainfo.xml
%{_mandir}/man1/kig.1*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
