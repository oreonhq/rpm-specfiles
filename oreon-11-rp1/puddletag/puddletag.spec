%global source0_hash aa04bd796a78ca726c91c28ade0b64a9d693cac307713728359dfc551d250815

Summary:        Feature rich, easy to use tag editor
Name:           puddletag
Version:        2.5.0
Release:        4%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://docs.puddletag.net/
Source0:        https://github.com/puddletag/puddletag/archive/refs/tags/%{version}.tar.gz
Patch0:         puddletag-2.5.0-req.patch
BuildArch:      noarch
BuildRequires:  chromaprint-tools
BuildRequires:  desktop-file-utils
BuildRequires:  python3-acoustid
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-qt5
BuildRequires:  quodlibet
Requires:       PyQt5
Requires:       python3-pyparsing >= 1.5.5
Requires:       python3-acoustid
Requires:       python3-mutagen
Requires:       python3-configobj
Requires:       python3-Levenshtein
%description
Puddletag is an audio tag editor.

Unlike most taggers, it uses a spreadsheet-like layout so that all the
tags you want to edit by hand are visible and easily editable.

The usual tag editor features are supported like extracting tag
information from filenames, renaming files based on their tags by
using patterns (that you define, not crappy, uneditable ones).

Then there are Functions, which can do things like replace text, trim,
change the case of tags, etc. Actions can automate repetitive
tasks. You can import your QuodLibet library, lookup tags using
AcoustID, MusicBrainz, FreeDB or Amazon (though it is only good for
cover art) and more.

Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.),
VorbisComments (ogg, flac), Musepack (mpc), Monkeys Audio (.ape) and
WavPack (wv).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Stray files
rm puddlestuff/mainwin/teststuff.py
rm puddlestuff/tagsources/example.py

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files puddlestuff
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
chmod 0644 %{buildroot}%{python3_sitelib}/puddlestuff/data/{menus,shortcuts}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license copyright
%doc NEWS THANKS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
