%global source0_hash bdf435db062ded71d4646bc30849d79c7741ccde6ca80f38888f29f6560bb318

# SPDX-License-Identifier: MIT
Version: 20060908
Release: 47%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Porson
%global fontsummary       GFS Porson, a 19th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
In England, during the 1790’s, Cambridge University Press decided to procure a
new set of Greek types. The university’s great scholar of Classics, Richard
Porson was asked to produce a typeface based on his handsome handwriting and
Richard Austin was commissioned to cut the types. The type was completed in
1808, after the untimely death of Porson the previous year. Its success was
immediate and since then the classical editions in Great Britain and the
U.S.A. use it, almost invariably.

In 1913, Monotype released the typeface with some corrections, notably
replacing the upright capitals suggested by Porson with inclined ones. In
Greece the typeface was used under the name Pelasgika type.

GFS Porson is based on the Monotype version, though using upright capitals, as
in the original.}

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
