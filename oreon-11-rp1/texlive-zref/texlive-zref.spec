%global source0_hash d90f2f2a1ab889078332eabdb23aa9c88f3fb079b73a21efb80ccb9f8e7b5a09d08b21b8a9c8473007d7dfd2cea1c4af9acdd5bc3f41ae7a7f2a3aebc1f1a917
%global source1_hash 61b5245f97b0d3441062b17bd94221124608d6eee2100447b05648cbcf879adeaaa2c77e859b6ad8221c950eb420c0df0cbbd0be982dec1dfc277b0324069725

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
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zref.tar.xz#/zref.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/zref.doc.tar.xz#/zref.doc.or11.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
