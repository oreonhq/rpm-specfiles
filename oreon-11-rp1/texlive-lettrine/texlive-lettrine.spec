%global source0_hash d3cc16bff3c44d548e0b73eadcd3a9719659013ba110cf6a18b3eaafc25e1f27
%global source1_hash 8e086db6d42cf0f047b1d0d68ee7bcde00ceb441a9212a290497c3e3328b4a54
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist
Name:           texlive-lettrine
Epoch:          12
Version:        svn77053
Release:        1%{?dist}
Summary:        Typeset dropped capitals
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lettrine.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lettrine.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-lettrine-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lettrine-doc <= 11:%{version}
Provides:       tex(lettrine-2006-03-17.sty)
Provides:       tex(lettrine-2015-08-31.sty)
Provides:       tex(lettrine-2018-08-18.sty)
Provides:       tex(lettrine-2022-09-25.sty)
Provides:       tex(lettrine-2023-04-18.sty)
Provides:       tex(lettrine.cfg)
Provides:       tex(lettrine.sty)
%description
Typeset dropped capitals.
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
%doc %{_texmf_main}/doc/latex/lettrine/
%{_texmf_main}/tex/latex/lettrine/
%changelog
%autochangelog
