%global source0_hash 351dea4f4a8d09945d5bfac4abf605b06697a6666463bf968068dfc3b034c0cbd137a2856847ef692351162da88f3d9da07eae4b6d25c1930ebaed16c0c8a728
%global source1_hash 01a12dd1aa191d53d34cc03ba24ca6513a454f3720675c2b41b551e72476fc25fbe8b7f55da92b2552d96af80516cde5d535b92667db03f77ada2eaca338de33

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-zhmetrics
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        TFM subfont metrics for Chinese
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/zhmetrics.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-zhmetrics-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-zhmetrics-doc <= 11:%{version}
Provides:       tex(zhwinfonts.tex)

%description
TFM subfont metrics for Chinese.

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
%doc %{_texmf_main}/doc/fonts/zhmetrics/
%{_texmf_main}/fonts/tfm/zhmetrics/cyberb/
%{_texmf_main}/fonts/tfm/zhmetrics/gbk/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkfs/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkhei/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkkai/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkli/
%{_texmf_main}/fonts/tfm/zhmetrics/gbksong/
%{_texmf_main}/fonts/tfm/zhmetrics/gbkyou/
%{_texmf_main}/fonts/tfm/zhmetrics/unifs/
%{_texmf_main}/fonts/tfm/zhmetrics/unihei/
%{_texmf_main}/fonts/tfm/zhmetrics/unikai/
%{_texmf_main}/fonts/tfm/zhmetrics/unili/
%{_texmf_main}/fonts/tfm/zhmetrics/unisong/
%{_texmf_main}/fonts/tfm/zhmetrics/uniyou/
%{_texmf_main}/tex/generic/zhmetrics/
%{_texmf_main}/tex/latex/zhmetrics/

%changelog
%autochangelog
