%global source0_hash 12258065ecfaced4d3d46800964284b9de14b93e8df5107a9f7ac18745f75c4c
%global source1_hash 20fec7026f1cbca8a1f9f581936973dce8241fd0d99988a9e7fcd1b4d5a97977

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-subfigure
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Deprecated package for subfigures
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfigure.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/subfigure.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-subfigure-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-subfigure-doc <= 11:%{version}
Provides:       tex(subfigure.sty)
Provides:       tex(subfigure.cfg)

%description
Deprecated package for subfigures.

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
%doc %{_texmf_main}/doc/latex/subfigure/
%{_texmf_main}/tex/latex/subfigure/

%changelog
%autochangelog
