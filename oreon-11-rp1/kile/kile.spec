%global source0_hash 64fa2e45c97dbb6f613d10f7f9bb005bf86fbbaaff238185538ac5b896be632f
%global _changelog_trimtime %(date +%s -d "1 year ago")
Name:	 kile
Summary:        (La)TeX source editor and TeX shell
Version: 2.9.94
%global respin -1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://kile.sourceforge.io/
Source0:        https://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}%{respin}.tar.bz2
Patch0:  kile-2.9.94-fix-missing-icon.patch
Requires: konsole-part
%if %{undefined flatpak}
Requires: tex(latex)
%endif
# oreon:deps
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Okular6)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(poppler-qt6)
# /oreon:deps
%description
Kile is a user friendly (La)TeX editor.  The main features are:
  * Compile, convert and view your document with one click.
  * Auto-completion of (La)TeX commands
  * Templates and wizards makes starting a new document very little work.
  * Easy insertion of many standard tags and symbols and the option to define
    (an arbitrary number of) user defined tags.
  * Inverse and forward search: click in the DVI viewer and jump to the
    corresponding LaTeX line in the editor, or jump from the editor to the
    corresponding page in the viewer.
  * Finding chapter or sections is very easy, Kile constructs a list of all
    the chapter etc. in your document. You can use the list to jump to the
    corresponding section.
  * Collect documents that belong together into a project.
  * Easy insertion of citations and references when using projects.
  * Advanced editing commands.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?pre}
%patch -P 0 -p1 -b .fix-missing-icon

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kile.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kile.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
