%global source0_hash 7243a2192b663751f18aaa87348385e2945d75e4e7e111c651631331936754ed

# SPDX-License-Identifier: MIT
Version: 20070415
Release: 49%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/18th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Bodoni Classic
%global fontsummary       GFS Bodoni Classic, an 18th century oblique Greek font family
%global fontpkgheader     %{expand:
Suggests: font(gfsbodoni)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Giambattista Bodoni was the most prolific Italian type cutter of the 18th
century. While he worked in the Vatican Press he was involved in the
type cutting of “exotic” languages for which catholic literature was printed.
When he established his own press in Parma he did publish many books of the
classics with his own Greek typefaces in the last quarter of the 18th century.
He was among the first European type cutters to move away from the byzantine
cursive tradition with the numerous ligatures which was the norm until then.
His Greek types influenced many subsequent designers, yet they fell in disuse
by the middle of the 19th century.

GFS presented Bodoni’s original Greek typeface in the commemorative edition of
Pindar’s Olympian Odes (2004), in digital version by George D. Matthiopoulos,
and is now available as free ware for the general public. In the OpenType
features, under ligatures, one may alternately use diphthongs with the accents
placed in between the characters, as Giambattista Bodoni did when setting
Greek texts.
}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

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
