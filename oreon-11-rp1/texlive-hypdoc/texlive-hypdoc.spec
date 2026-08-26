%global source0_hash 4a68820f9df7fdc39e5f253c6b0826a4d847cea8e7b6c262f76c5632e5f52935fbcf2eb53406c523237c4ec9157ee6f5389eb7f2324f76620a3ab077d0a53b37
%global source1_hash 1b2c55e41f128ede05f6c685df9a29100ca05fbc60bdbc9e04f5296090cd46fd052744eb61293a79ec6206030ee649d6bc5ca16be2663154348acf7606466099

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-hypdoc
Epoch:          12
Version:        svn68661
Release:        1%{?dist}
Summary:        Hyper extensions for doc.sty
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypdoc.r79461.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypdoc.doc.r79461.tar.xz
BuildRequires:  tar
Provides:       texlive-hypdoc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hypdoc-doc <= 11:%{version}
Provides:       tex(hypdoc.sty)

%description
Hyper extensions for doc.sty.

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
%doc %{_texmf_main}/doc/latex/hypdoc/
%{_texmf_main}/tex/latex/hypdoc/

%changelog
%autochangelog
