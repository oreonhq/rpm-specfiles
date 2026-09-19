%global source0_hash c7860e371a1f8b04bc9c7eb5d1e4fae0fddb4cc4cb0565db30db205db464a840

# SPDX-License-Identifier: MIT
Version: 1.17
Release: 21%{?dist}
URL:     http://arkandis.tuxfamily.org/adffonts.html

%global foundry           ADF
%global fontlicense       GPL-2.0-only WITH Font-exception-2.0
%global fontlicenses      OTF/COPYING
%global fontdocs          *.txt

%global fontfamily        Tribun
%global fontsummary       ADF Tribun, a newsprint-like serif font family
%global fonts             OTF/*.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Hirwen Harendal started in 1999 the realization of a first font family, aiming
to create another “Times New Roman”… He does not consider this endeavor a huge
success. However, he transformed Tribun progressively since then to give it its
own character.

The idea was to achieve newsprint-like rendering. To this effect, the glyph
bodies, serifs, or even extenders are not normalized and use irregular strokes.
This is most visible in italics though those variations stay imperceptible at
small sizes.

Italics proved time-consuming. They are never an easy thing to draw.
Nevertheless, the designer considers them very close to those of “Times”, with
some variations.

The medium weight uses a stronger stroke. It can be used for emphasis, or for
effects in titles. That being said it has also been used for body copy. It is
also slightly expanded to complete the face offerings.

The condensed version is a bit unusual, since it stands in for both normal and
medium condensed. After several trials, Hirwen decided an intermediate weight
rendered much better both for document display and in print. Secondly, he took
great care to keep readability excellent, and this even for italics.

This font family is particularly well suited for text, display, or
presentations. It is also ideal for all Web publications. It can serve as
alternative to “Times New Roman” and other similar fonts.}

%global archivename Tribun-Std-20120228

Source0:  http://arkandis.tuxfamily.org/fonts/%{archivename}.zip
Source1:  http://arkandis.tuxfamily.org/docs/Tribun-Cat.pdf
Source10: 60-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} .
%linuxtext NOTICE.txt OTF/COPYING

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OTF/COPYING
%doc *.pdf

%changelog
%autochangelog
