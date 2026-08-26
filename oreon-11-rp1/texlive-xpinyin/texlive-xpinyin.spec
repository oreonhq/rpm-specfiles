%global source0_hash 424b7ba89128c2bf927ca52eb55fdb22d2b6a2cec71e537100958b81062de767e3a493c2b4cde875c72158ef0268934409555cb185df6807530e32b053a85bc0
%global source1_hash 84517026d64b2b756dd5c4507f053aeee2238036764bb7e46c044e5864fbe558f9e8831bac19efea3fbc8868636a499c8f9e7b3dd20a36fbbcddb47a90c01469

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xpinyin
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Automatic CJK pinyin annotations
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xpinyin.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-xpinyin-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xpinyin-doc <= 11:%{version}
Provides:       tex(xpinyin.sty)
Provides:       tex(xpinyin-database.def)

%description
Automatic CJK pinyin annotations.

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
%doc %{_texmf_main}/doc/latex/xpinyin/
%{_texmf_main}/tex/latex/xpinyin/

%changelog
%autochangelog
