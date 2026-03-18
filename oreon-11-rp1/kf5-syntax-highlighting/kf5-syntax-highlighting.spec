%global framework syntax-highlighting

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Syntax highlighting engine for Kate syntax definitions

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream fixes (lookaside cache)

BuildRequires: extra-cmake-modules >= %{majmin}
BuildRequires: kf5-rpm-macros

BuildRequires: perl-interpreter
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: cmake(Qt5LinguistTools)
# optional deps
%if ! 0%{?bootstrap}
BuildRequires: qt5-qtxmlpatterns-devel
%endif

Requires:      kf5-filesystem >= %{majmin}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang_kf5 syntaxhighlighting5_qt


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 300" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files -f syntaxhighlighting5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_bindir}/kate-syntax-highlighter
%{_kf5_libdir}/libKF5SyntaxHighlighting.so.*
%{_kf5_qmldir}/org/kde/syntaxhighlighting/

%files devel
%{_kf5_libdir}/libKF5SyntaxHighlighting.so
%{_kf5_libdir}/cmake/KF5SyntaxHighlighting/

%{_kf5_includedir}/KSyntaxHighlighting/
%{_kf5_archdatadir}/mkspecs/modules/qt_KSyntaxHighlighting.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
