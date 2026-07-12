%global source0_hash 4db59ef81229f2f836f4d96750850f8bb2729c1670e260e1c993b195073785b0
%global source1_hash 155aff1acdba79908de921307b810e1871b85d4ae1d359d387e08f8c90a8c353

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-bigfoot
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Footnotes for critical editions (provides perpage)
License:        GPL-2.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigfoot.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigfoot.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-bigfoot-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bigfoot-doc <= 11:%{version}
Provides:       tex(bigfoot.sty)
Provides:       tex(perpage.sty)
Provides:       tex(suffix.sty)

%description
Footnotes for critical editions (provides perpage).

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
%doc %{_texmf_main}/doc/latex/bigfoot/
%{_texmf_main}/tex/latex/bigfoot/

%changelog
%autochangelog
