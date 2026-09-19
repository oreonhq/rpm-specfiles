%global source0_hash 2f1a2c5491d7305dffd3520c6375d2f3e14931ee35c6d8ae1e8f098bf1a7b3cc

# SPDX-License-Identifier: MIT
Version: 1.102
Release: %autorelease
URL:     https://software.sil.org/gentium/

%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt

%global common_description %{expand:
Gentium Basic and Gentium Book Basic are font families based on the
original Gentium design, but with additional weights. Both families come
with a complete regular, bold, italic and bold italic set of fonts.
These "Basic" fonts support only the Basic Latin and Latin-1 Supplement
Unicode ranges, plus a selection of the more commonly used extended Latin
characters, with miscellaneous diacritical marks, symbols and punctuation.
}

%global fontfamily0       Gentium Basic
%global fontsummary0      SIL Gentium Basic font family
%global fontpkgheader0    %{expand:
Obsoletes: sil-gentium-basic-fonts-common < %{version}-%{release}
}
%global fonts0            GenBas*
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This is the base variant.}

%global fontfamily2       Gentium Basic Book
%global fontsummary2      SIL Gentium Book Basic font family
%global fonts2            GenBkBas*
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%global fontpkgname2       sil-gentium-basic-book-fonts
%{common_description}

The "Book" family is slightly heavier.}

%global archivename GentiumBasic_1102

Source0:   https://software.sil.org/downloads/r/gentium/%{archivename}.zip
Source10:  59-%{fontpkgname}.conf
Source12:  59-%{fontpkgname2}.conf

%fontpkg -a

%fontmetapkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc FONTLOG.txt GENTIUM-FAQ.txt OFL-FAQ.txt

%changelog
%autochangelog
