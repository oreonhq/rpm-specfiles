# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 fd703c777712ad0e20a849f837c3ad7880eb82c1beb50196608cb326373f78e3
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global framework ktexteditor

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

%ifarch aarch64
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif

Name:    kf6-%{framework}
Version: 6.24.0
Release:	7%{?dist}
Summary: KDE Frameworks 6 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6TextToSpeech)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  pkgconfig(libgit2) >= 0.22.0
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(xkbcommon)
Requires: kf6-filesystem

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF6::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6Parts)
Requires:       cmake(KF6SyntaxHighlighting)
#Requires:       kf6-syntax-highlighting-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%oreon_verify_sources
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/ktexteditor
# Removing empty file
rm -f %{buildroot}%{_kf6_datadir}/katepart5/script/README.md

%files -f %{name}.lang
%dir %{_kf6_plugindir}/parts/
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.ktexteditor6.katetextbuffer.policy
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6TextEditor.so.*
%{_kf6_plugindir}/parts/katepart.so
%{_kf6_qtplugindir}/ktexteditor/
%{_kf6_libexecdir}/kauth/kauth_ktexteditor_helper
%{_kf6_bindir}/ktexteditor-script-tester6

%files devel
%{_kf6_datadir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/cmake/KF6TextEditor/
%{_kf6_libdir}/libKF6TextEditor.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-7
- aarch64: no LTO, -j2 to avoid OOM (cc1plus Killed)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

