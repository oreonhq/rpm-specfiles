%global source0_hash 250677c929d3775a30913643594379af264ac2ef2801035aa1dcbe30b9be23a6

Version: 7.051
Release: 5%{?dist}
URL: https://github.com/alerque/libertinus

%global foundry alerque
%global fontlicense       OFL

%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily Libertinus
%global fontsummary The Libertinus Fonts project
%global fonts             static/OTF/*.otf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
The Libertinus Fonts project includes four main type families:

The Libertinus Serif family:

  * 6 serif typefaces cover three weights (Regular, Semibold, Bold) in each of two styles (Regular, Italic); originally forked from Linux Libertine.

The Libertinus Sans family:

  * 3 sans-serif typefaces cover Regular, a Bold weight, and an Italic style; originally forked from Linux Biolinum.

The Libertinus Mono family:

  * 1 monospace typeface derived from the serif family; originally forked from Linux Libertine Mono.

The Libertinus Math family:

  * 1 OpenType math typeface derived from the serif family with many extra glyphs and features for use in OpenType math-capable applications (such as LuaTeX, XeTeX, or MS Word 2007+).

Additionally included are 3 special-use families with a single typeface each:

  * Libertinus Serif Display: A derivative of Libertinus Serif Regular optimized for display at large sizes.

  * Libertinus Serif Initials: A derivative of Libertinus Serif with outlined variants of capital letter glyphs suitable for drop-caps or other decorations.

  * Libertinus Keyboard: A derivative of Libertinus Sans with keyboard key outlines around each character suitable for use in technical documentation.
}

Source0: https://github.com/alerque/libertinus/releases/download/v%{version}/Libertinus-%{version}.tar.zst

Source10: 60-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Libertinus-%{version}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
