%global source0_hash 48af93600d59c545db960e707291ce325d0fce551dedc6d2c3ffea14cec5edfc

# SPDX-License-Identifier: MIT
Version: 20070415
Release: 51%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Theokritos
%global fontsummary       GFS Theokritos, a 20th century decorative Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Yannis Kefallinos (1894–1958) was one of the most innovative engravers of his
generation and the first who researched methodically the aesthetics of book and
typographic design in Greece. He taught at the Fine Arts School of Athens and
established the first book design workshop from which many practicing artists
of the 60’s and 70’s had graduated.

In the late 50’s Kefallinos designed and published an exquisite book with
engraved illustrations of the ancient white funerary pottery in Attica in
collaboration with Varlamos, Montesanto, Damianakis. For the text of
Kefallinos’ Δέκα λευκαί λήκυθοι (1956) the artist used a typeface which he
himself had designed a few years before for an unrealized edition of
Theocritos’ Idyls. Its complex and heavily decorative design does point to
aesthetic codes which preoccupied his artistic expression and, although
impractical for contemporary text setting, it remains an original display
face, or it can be used as initials.

The book design workshop of the Fine Arts School of Athens has been recently
reorganized, under the direction of professor Leoni Vidali, and with her
collaboration George D. Matthiopoulos has redesigned digitally this historical
font which is now available as GFS Theokritos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 65-%{fontpkgname}.xml

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
