%global source0_hash d49a5892022e6dfe4e00bfea0876ded20a061d0e8d13448aeebb7bc8d544ac34
%global source1_hash 9cc126e9dc4f10ab1823c348a2b210a546e2c673ad1249405271015d5d46b8d7
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist
Name:           texlive-datetime
Epoch:          12
Version:        svn36650
Release:        1%{?dist}
Summary:        Change format of dates and times
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/datetime.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/datetime.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-datetime-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-datetime-doc <= 11:%{version}
Provides:       tex(datetime-defaults.sty)
Provides:       tex(datetime.sty)
Provides:       tex(dt-UKenglish.def)
Provides:       tex(dt-USenglish.def)
Provides:       tex(dt-american.def)
Provides:       tex(dt-australian.def)
Provides:       tex(dt-austrian.def)
Provides:       tex(dt-bahasa.def)
Provides:       tex(dt-basque.def)
Provides:       tex(dt-breton.def)
Provides:       tex(dt-british.def)
Provides:       tex(dt-bulgarian.def)
Provides:       tex(dt-canadian.def)
Provides:       tex(dt-catalan.def)
Provides:       tex(dt-croatian.def)
Provides:       tex(dt-czech.def)
Provides:       tex(dt-danish.def)
Provides:       tex(dt-dutch.def)
Provides:       tex(dt-esperanto.def)
Provides:       tex(dt-estonian.def)
Provides:       tex(dt-finnish.def)
Provides:       tex(dt-french.def)
Provides:       tex(dt-galician.def)
Provides:       tex(dt-german.def)
Provides:       tex(dt-greek.def)
Provides:       tex(dt-hebrew.def)
Provides:       tex(dt-icelandic.def)
Provides:       tex(dt-irish.def)
Provides:       tex(dt-italian.def)
Provides:       tex(dt-latin.def)
Provides:       tex(dt-lsorbian.def)
Provides:       tex(dt-magyar.def)
Provides:       tex(dt-naustrian.def)
Provides:       tex(dt-newzealand.def)
Provides:       tex(dt-ngerman.def)
Provides:       tex(dt-norsk.def)
Provides:       tex(dt-polish.def)
Provides:       tex(dt-portuges.def)
Provides:       tex(dt-romanian.def)
Provides:       tex(dt-russian.def)
Provides:       tex(dt-samin.def)
Provides:       tex(dt-scottish.def)
Provides:       tex(dt-serbian.def)
Provides:       tex(dt-slovak.def)
Provides:       tex(dt-slovene.def)
Provides:       tex(dt-spanish.def)
Provides:       tex(dt-swedish.def)
Provides:       tex(dt-turkish.def)
Provides:       tex(dt-ukraineb.def)
Provides:       tex(dt-usorbian.def)
Provides:       tex(dt-welsh.def)
%description
Change format of dates and times.
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%build
%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
tar -xf %{SOURCE1} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg
%files
%doc %{_texmf_main}/doc/latex/datetime/
%{_texmf_main}/tex/latex/datetime/
%changelog
%autochangelog
