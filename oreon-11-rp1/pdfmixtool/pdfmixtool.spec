%global source0_hash 5feccbc7d797920bede35a39526cb0093052f38e2bfc17c0c609e6129aba82de

%global appid eu.scarpetta.PDFMixTool

Name:           pdfmixtool
Version:        1.2.2
Release:        %autorelease
Summary:        An application to split, merge, rotate and mix PDF files

License:        GPL-3.0-or-later
URL:            https://scarpetta.eu/pdfmixtool
Source0:        https://gitlab.com/scarpetta/pdfmixtool/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libqpdf)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
PDF Mix Tool is a simple and lightweight application that allows you to
perform common editing operations on PDF files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop

%files
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS.md TRANSLATORS.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/%{appid}.appdata.xml

%changelog
%autochangelog
