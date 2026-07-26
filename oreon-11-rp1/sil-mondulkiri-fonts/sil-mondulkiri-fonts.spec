%global source0_hash c2e5dc08f4835be9a0da5cf9dcf92105aff973e47fc31e075e8bc44bec632c85

# SPDX-License-Identifier: MIT
Version: 7.100
Release: 19%{?dist}
URL:     https://scripts.sil.org/Mondulkiri

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily0       Mondulkiri
%global fontsummary0      Khmer Mondulkiri, a Khmer script font family suited for very small print
%global fonts0            Mondulkiri*.ttf
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
The Khmer Mondulkiri font family provides Unicode support for the Khmer script.
It is very light and well suited for very small print.}

%global fontfamily1       Busra
%global fontsummary1      Khmer Busra, a Khmer script font family suited for normal text
%global fonts1            Busra*.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
The Khmer Busra font family provides Unicode support for the Khmer script. It
is probably the best SIL font family for Khmer normal text. The regular font
was formerly named “Khmer Mondulkiri Book” and the bold font was named “Khmer
Mondulkiri SemiBold”.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{fontfamily0}"), "[%p%s]+", "");print(t)}-%{version}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%package doc
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
%doc documentation/*pdf

%changelog
%autochangelog
