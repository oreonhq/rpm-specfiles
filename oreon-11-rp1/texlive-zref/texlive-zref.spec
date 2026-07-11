%global source0_hash fa4b5cede6e3e195e0aa4a3c86b1e65f6d6302e38a879dbe0fab9494814f9679
%global source1_hash ecbddf6c739b1ac34a9c063b38860047ba1805620ac33d6ee2cca36c5bee1a8d

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-zref
Epoch:          12
Version:        svn79461
Release:        1%{?dist}
Summary:        A new reference scheme for LaTeX
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zref.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zref.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-zref-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-zref-doc <= 11:%{version}
Provides:       tex(zref-abspage.sty)
Provides:       tex(zref-abspos.sty)
Provides:       tex(zref-base.sty)
Provides:       tex(zref-counter.sty)
Provides:       tex(zref-dotfill.sty)
Provides:       tex(zref-env.sty)
Provides:       tex(zref-hyperref.sty)
Provides:       tex(zref-lastpage.sty)
Provides:       tex(zref-marks.sty)
Provides:       tex(zref-nextpage.sty)
Provides:       tex(zref-pageattr.sty)
Provides:       tex(zref-pagelayout.sty)
Provides:       tex(zref-perpage.sty)
Provides:       tex(zref-runs.sty)
Provides:       tex(zref-savepos.sty)
Provides:       tex(zref-thepage.sty)
Provides:       tex(zref-titleref.sty)
Provides:       tex(zref-totpages.sty)
Provides:       tex(zref-user.sty)
Provides:       tex(zref-xr.sty)
Provides:       tex(zref.sty)

%description
A new reference scheme for LaTeX.

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
%doc %{_texmf_main}/doc/latex/zref/
%{_texmf_main}/tex/latex/zref/

%changelog
%autochangelog
