%global source0_hash 1e0caa85414f9d857531da65de2edeb47d9a45f5889a7692330e86cacaae1e697cf04b8a70fef2698c3260a376b516599ebe8c812860208565c2870407e9f33a
%global source1_hash 05752f37111971b768f7e967f63d01b394cf169f629b9e05e5495280ef0e25d7a435383960c7af4d94ced24f3e3f6205ca3f6a468a08c7b5f92f8bc67d7482f9

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fmtcount.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fmtcount.doc.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
