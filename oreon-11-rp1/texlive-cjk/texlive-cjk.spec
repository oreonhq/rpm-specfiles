%global source0_hash 744904abda9141fa1a448b6ad3ab6d1389e515e98dbad9489613d98194eee0f2
%global source1_hash 803b33ed94d274ce300468ce357f882a0bc7c82bc56c82a1b1eaed479004e843

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/cjk.doc.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
