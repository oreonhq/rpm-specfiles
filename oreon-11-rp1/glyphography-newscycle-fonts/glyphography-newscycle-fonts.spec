%global source0_hash 6eaf4848e69ea65463aa1a398b43231a19bb77fd3d2db3061d04ec06946bf65c

Version:        0.5.2
Release:        17%{?dist}
URL:            https://launchpad.net/newscycle

%global foundry           glyphography
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        newscycle
%global fontsummary       A realist sans-serif font family based on News Gothic

%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
Inspired by the original News Gothic, which found an eminently useful
life in print media news coverage, the goal of this project is to design
a highly readable open font suitable for large bodies of text, even at
small sizes, and that is available at multiple weights. In addition to
the readability and weight, however, the project is extending News
Gothic's glyph coverage to alphabets derived from Latin, Cyrillic, and
Greek, including the accent marks and diacritics required by languages
outside of Western Europe.
}

Source0:        %{url}/trunk/%{version}/+download/%{fontfamily}-%{version}.zip
Source10:       61-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{fontfamily}-%{version}
rm -f *~ *.svg

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
