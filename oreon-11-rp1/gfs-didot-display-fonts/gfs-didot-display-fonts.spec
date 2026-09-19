%global source0_hash 7dfe83c5a0155f9c7764dce7493b45ba2f1358ce251f9c621387a3a252cd08a6

# SPDX-License-Identifier: MIT
Version: 20160225
Release: 19%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Didot Display
%global fontsummary       GFS Didot Display, a 20th century Greek decorative font family
%global fontpkgheader     %{expand:
Requires: font(gfsdidot)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription %{expand:
GFS Didot Display is a fat version of the Greek Didot. Found in several
publications, mainly as a headline font since the 1840s. At certain occasions
it was used in text columns for newspaper typesetting. The typeface was
digitized by George Triantafyllakos based on samples found in Greek newspapers
from the ’50s and from the Specimens Catalogue of Linotype Co.}

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
