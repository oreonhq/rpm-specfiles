%global source0_hash 9c03383219868c0ca2aabcdd3e0bb8b22e942ccf03f3221cd8270dbaaf54bb92

# SPDX-License-Identifier: MIT
Version: 20161102
Release: 19%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Orpheus Sans
%global fontsummary       GFS Orpheus Sans, a 21st century mono-linear Greek font family
%global fontpkgheader     %{expand:
Suggests: font(gfsorpheus)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS Orpheus Sans is a mono-linear version of GFS Orpheus. The experiment of
designing a mono-linear typeface based on the original, contrasted typeface,
clearly shows the innovative design ideas that were incorporated in the
original typeface; ideas similar to those of a modern sans serif typeface with
clean mono-linear strokes and balanced proportions.

GFS Orpheus Sans was designed by George Triantafyllakos.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
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
