%global source0_hash 6f8ccacebd0dc9ce050b2b23b715750c97938b3336fbbb80967920cb8c1dfaa7

%global framework syntax-highlighting

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary: KDE Frameworks 5 Syntax highlighting engine for Kate syntax definitions

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%autochangelog
