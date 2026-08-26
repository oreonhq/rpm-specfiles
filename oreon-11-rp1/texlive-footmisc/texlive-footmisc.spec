%global source0_hash d53877d3f17d2848be99ad9eb0a8986d31ad759db8a6834f6a8c6afa4eccc139
%global source1_hash 4b8334d9a5d7842dea9a677a7146397e22d215f062f5af2a7384e86c9d6c26c9

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-footmisc
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        A range of footnote options
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footmisc.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/footmisc.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-footmisc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-footmisc-doc <= 11:%{version}
Provides:       tex(footmisc-2011-06-06.sty)
Provides:       tex(footmisc-2022-02-14.sty)
Provides:       tex(footmisc.sty)

%description
A range of footnote options.

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
%doc %{_texmf_main}/doc/latex/footmisc/
%{_texmf_main}/tex/latex/footmisc/

%changelog
%autochangelog
