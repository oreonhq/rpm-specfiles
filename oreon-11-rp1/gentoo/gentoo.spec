%global source0_hash 9a50a139509a2f7e4540c8a093105bd8dd432596c9903db24891fbacf28ab1aa

Name:           gentoo
Version:        0.20.7
Release:        26%{?dist}
Summary:        Graphical file management program written in GTK+3
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://sourceforge.net/projects/gentoo/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        gentoo.desktop
# icons/gentoo.png is not within standard sizes
# Get here http://www.obsession.se/gentoo/gfx/logo.png (not in sources)
Source2:        gentoo.png
# Remove duplicated translations
Patch0:         %{name}-0.19.12-locales.patch
# https://salsa.debian.org/debian/gentoo/-/blob/master/debian/patches/gcc-15.patch
Patch1:         %{name}-0.20.7-c23-bool.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel >= 3.12
BuildRequires:  gettext
BuildRequires: make

%description
gentoo is a file manager written from scratch in pure C. It uses the GTK3 
toolkit for all of its interface needs. gentoo provides 100%% GUI 
configurability; no need to edit config files by hand and re-start the 
program. gentoo supports identifying the type of various files (using 
extension, regular expressions, and/or the 'file' command), and can display 
files of different types with different colors and icons. gentoo borrows 
some of its look and feel from the classic Amiga file manager 
"Directory OPUS"(TM) (written by Jonathan Potter).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
# Remove duplicated translations, keep only UTF-8
pushd po
mv ja{_JP.UTF-8,}.po
mv ja{_JP.UTF-8,}.gmo
mv ru{_RU.UTF-8,}.po
mv ru{_RU.UTF-8,}.gmo
rm -frv ru_RU.*.{po,gmo}
popd

%build
%configure
%make_build

%install
%make_install

# Included man page, not installed by default
install -pDm0644 docs/gentoo.1x %{buildroot}%{_mandir}/man1/gentoo.1
# Don't install the man page again in %doc
rm -frv docs/gentoo.1x
# Our own desktop entry, with its icon
install -pDm0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gentoo.png

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog CONFIG-CHANGES CREDITS docs/
%doc NEWS README* TODO
%license COPYING
%config %{_sysconfdir}/gentoo*
%{_bindir}/gentoo
%{_datadir}/applications/gentoo.desktop
%{_datadir}/gentoo/
%{_datadir}/icons/hicolor/64x64/apps/gentoo.png
%{_mandir}/man1/gentoo.1*

%changelog
%autochangelog
