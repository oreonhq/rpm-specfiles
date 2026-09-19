%global source0_hash b70127c420e1d8f72379cee4c70c809104b581f63c9da7c83ff344497934d796

Name: ghostwriter
Version: 25.12.3
Release: 1%{?dist}

License: GPL-3.0-or-later AND Apache-2.0 AND CC-BY-4.0 AND CC-BY-SA-4.0 AND MPL-1.1 AND BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-only AND MIT AND ISC
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://invent.kde.org/office/%{name}
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: hunspell-devel

BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Widgets)

Provides: bundled(cmark-gfm) = 0.29.0.gfm.6
Provides: bundled(fontawesome-fonts) = 5.10.2
Provides: bundled(nodejs-mathjax-full) = 3.1.2
Provides: bundled(nodejs-react) = 17.0.1
Provides: bundled(QtAwesome) = 5

Requires: hicolor-icon-theme

Recommends: cmark%{?_isa}
Recommends: multimarkdown%{?_isa}
Recommends: pandoc%{?_isa}

# Required qt6-qtwebengine is not available on some arches.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber’s website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%install
%cmake_install
%find_lang %{name} --all-name --with-qt --with-man

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license COPYING
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_mandir}/man1/ghostwriter.*

%changelog
%autochangelog
