%global source1_hash b26f7a8dbd48a0f429422c3a0bdf02d4c6ab7dc38126766223fcc9f22ddce2b4
%global source0_hash d90f24e33a7aa0e6a179af253dfdeca0977992adb62bf1b6f7ad11537ab6e3e7
%global framework ktexteditor
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
%ifarch aarch64
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 with advanced embeddable text editor
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires: kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6TextToSpeech)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
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
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang %{name} --all-name
mkdir -p %{buildroot}%{_kf6_qtplugindir}/ktexteditor
rm -f %{buildroot}%{_kf6_datadir}/katepart5/script/README.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-ktexteditor-devel -f %{oreon_filedir}/kf6-ktexteditor-devel.list

%changelog

%autochangelog
