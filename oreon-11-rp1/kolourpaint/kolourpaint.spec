
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kolourpaint
Summary: An easy-to-use paint program 
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD 
URL:     https://www.kde.org/applications/graphics/kolourpaint/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)

BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KSaneWidgets6)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package  libs
Summary:  Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
%description libs
%{summary}.


%prep
%autosetup


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

## unpackaged files
rm -fv %{buildroot}%{_libdir}/libkolourpaint_lgpl.so


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README.md
%license COPYING*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*

%files libs
%{_libdir}/libkolourpaint_lgpl.so.5


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
