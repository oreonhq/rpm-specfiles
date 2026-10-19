%global source0_hash 6064047f18179f8c3b4abf4c31d06f5896051a63af94533fbdb5d8722a42e08a
%global forgeurl    https://github.com/cvfosammmm/Setzer
%global uuid        org.cvfosammmm.Setzer
Name:           setzer
Version:        66
Release:        1%{?dist}
Summary:        LaTeX editor written in Python with Gtk
%forgemeta
License:        GPL-3.0-or-later
URL:            https://www.cvfosammmm.org/setzer/
Source0:        %{forgeurl}/archive/v%{version}/Setzer-%{version}.tar.gz
BuildArch:      noarch
Requires:       gtk4
Requires:       gtksourceview5
Requires:       libadwaita
Requires:       libportal
Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       pango
Requires:       poppler-glib
Requires:       python3-bibtexparser
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-numpy
Requires:       python3-pexpect
Requires:       python3-willow
Requires:       webkitgtk6.0
Requires:       texlive
Requires:       texlive-synctex
Requires:       texlive-xetex
Recommends:     latexmk
Recommends:     texlive-pdftex
Recommends:     texlive-luatex
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gspell-devel
BuildRequires:  gtk4-devel
BuildRequires:  gtksourceview5-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  libportal-devel
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  python3-bibtexparser
BuildRequires:  python3-cairo
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pexpect
BuildRequires:  python3-willow
BuildRequires:  webkitgtk6.0
# /oreon:deps
%description
Write LaTeX documents with an easy to use yet full-featured editor.

- Buttons and shortcuts for many LaTeX elements and special characters.
- Document creation wizard.
- Dark mode.
- Helpful error messages in the build log.
- Looks great on the Gnome desktop.
- Good screen to content ratio.
- Arguably the best .pdf viewer of any LaTeX editor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

find ./setzer -name "*.py" -type f -exec sed -i '1d' {} \;
%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
