%global source0_hash 2ad957bc338cf44b86531f883ba7a44158457faa32807c34b35d5969bb95f160
%global source1_hash 9b4635a5757529f42027125330dd4acae32ec2a61c18bf919d40eb213a151578

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-fmtcount
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Display the value of a LaTeX counter in formatting
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fmtcount.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fmtcount.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-fmtcount-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fmtcount-doc <= 11:%{version}
Provides:       tex(fcnumparser.sty)
Provides:       tex(fcprefix.sty)
Provides:       tex(fmtcount.sty)
Provides:       tex(fc-UKenglish.def)
Provides:       tex(fc-USenglish.def)
Provides:       tex(fc-american.def)
Provides:       tex(fc-brazilian.def)
Provides:       tex(fc-british.def)
Provides:       tex(fc-dutch.def)
Provides:       tex(fc-english.def)
Provides:       tex(fc-francais.def)
Provides:       tex(fc-french.def)
Provides:       tex(fc-frenchb.def)
Provides:       tex(fc-german.def)
Provides:       tex(fc-germanb.def)
Provides:       tex(fc-italian.def)
Provides:       tex(fc-ngerman.def)
Provides:       tex(fc-ngermanb.def)
Provides:       tex(fc-portuges.def)
Provides:       tex(fc-portuguese.def)
Provides:       tex(fc-spanish.def)

%description
Display the value of a LaTeX counter in formatting.

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
%doc %{_texmf_main}/doc/latex/fmtcount/
%{_texmf_main}/scripts/fmtcount/
%{_texmf_main}/tex/latex/fmtcount/

%changelog
%autochangelog
