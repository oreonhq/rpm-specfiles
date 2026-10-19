%global source0_hash 7e3e635f39d447398e4b5ed6963c03740b35e42479c370a36a27200a80e859ee
%{!?qt6_qtwebengine_arches:%global qt6_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}
Name:           frescobaldi
Version:        4.0.7
Release:        1%{?dist}
Summary:        Edit LilyPond sheet music with ease!
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://www.frescobaldi.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         pygame.patch
BuildArch:      noarch
ExclusiveArch: %{qt6_qtwebengine_arches}
Requires:       alsa-utils
Recommends:     lilypond
Requires:       portmidi
Requires:       python3-portmidi
Requires:       python3-ly >= 0.9.5
Requires:	python3-pyqt6-webengine
Requires:       python3-qpageview
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-frescobaldi = %{version}-%{release}
# /oreon:deps
%description
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful,
yet lightweight and easy to use. It features:

    * Enter LilyPond scores, build and preview them with a mouse-click
    * Point-and-click support: click on notes or error messages to jump to the
      correct position
    * A powerful Score Wizard to quickly setup a musical score
    * Editing tools to:
          o manipulate the rhythm
          o hyphenate lyrics
          o quickly enter or add articulations and other symbols to existing
            music
          o run the document through convert-ly to update it to a newer
            LilyPond version
    * Context sensitive auto-complete, helping you to quickly enter LilyPond
      commands
    * Expansion manager to enter larger snippets of LilyPond input using short
      mnemonics
    * Built-in comprehensive User Guide

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find -name "*.py"  -exec sed -i -e 's|#! python||' {} \;

%patch -P0 -p0

%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-install                                         \
   --dir=%{buildroot}%{_datadir}/applications                \
   --remove-category=Application                             \
   --add-category=AudioVideo                                 \
   --add-category=X-Notation                                 \
   --delete-original                                         \
   linux/org.frescobaldi.Frescobaldi.desktop
mkdir -p %{buildroot}%{_metainfodir}
install -m 0644 \
	linux/org.frescobaldi.Frescobaldi.metainfo.xml \
	%{buildroot}%{_metainfodir}/org.frescobaldi.Frescobaldi.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp frescobaldi/icons/org.frescobaldi.Frescobaldi.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%oreon_autofiles main

%files

%changelog

%autochangelog
