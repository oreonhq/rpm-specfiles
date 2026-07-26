%global source0_hash 2c255771b704cd2e57c6b2dc0133715195bb6a127373aca8bf79cbd6f7524959

# SPDX-License-Identifier: MIT
Version: 20100203
Release: 36%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Goschen
%global fontsummary       GFS Göschen, a 19th century neoclassical cursive Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Georg Joachim Göschen founded in 1782 the publishing house of G.J.
Göschensche Verlagsbuchhandlung in Leipzig and was one of the most active
publishers of the period in Germany. Göschen was very interested in
typography, influenced by the fame and quality of the editions of G. Bodoni
and F. Didot.

In 1797, he collaborated with the leading scholar of the period, Johann Jakob
Griesbach, to edit and publish the New Testament in Greek for which he formed
a committee of scholars to decide the new Greek type which were eventually
cut by Johann Prillwitz. The book appeared in 1803 and the types show many
influences from the Greek types of Bodoni. Their characteristic was the
neoclassical form of marked contrast between thick and thin strokes, the
cursive style and the large size of the font.

The design was too cumbersome to allow general use and can be considered
successful only for its indirect influence on the later cut Greek Leipzig
type. It is, however, part of the greater heritage of Greek type design and
therefore the type has been digitized by George D. Matthiopoulos in 2009 and
is part of GFS’ type library under the name GFS Göschen cursive, in
commemoration of the great German publisher.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 64-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
%autochangelog
