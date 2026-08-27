%global source0_hash b13712912e479dab68cab9027042be8cb11047ebf9c034f532c857e83d28f19dfea5a1748685cfe1847c7372f2d0982f79736525694d937c88962c5262094585
%global source1_hash a8c6b2d4d0899b841ccc32b378855d61bdaa65d5f68fd408df3894d386bcde18f384410f34e6f33ee2a5ce770e1e663a05ab038d9b7483012a3cb414739c3705

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-cjk
Epoch:          12
Version:        svn60865
Release:        1%{?dist}
Summary:        CJK language support macros
License:        GPL-2.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.tar.xz#/cjk.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.doc.tar.xz#/cjk.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-cjk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-cjk-doc <= 11:%{version}
Provides:       tex(CJK.sty)
Provides:       tex(CJKfntef.sty)
Provides:       tex(CJKnumb.sty)
Provides:       tex(CJKspace.sty)
Provides:       tex(CJKulem.sty)
Provides:       tex(CJKutf8.sty)
Provides:       tex(CJKvert.sty)
Provides:       tex(MULEenc.sty)
Provides:       tex(pinyin.sty)
Provides:       tex(pshan.sty)
Provides:       tex(ruby.sty)
Provides:       tex(c90enc.def)
Provides:       tex(pinyin.ldf)
Provides:       tex(thaicjk.ldf)

%description
CJK language support macros.

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
%doc %{_texmf_main}/doc/latex/cjk/
%{_texmf_main}/tex/latex/cjk/

%changelog
%autochangelog
