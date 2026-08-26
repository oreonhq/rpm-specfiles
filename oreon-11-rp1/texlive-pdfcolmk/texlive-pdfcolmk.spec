%global source0_hash 3056360ae3ec967c4a47b976371e628c70fae3b3a11196087373654b477c365a
%global source1_hash 15d697f507c5ca7bd99e15669549ae60f483043ef1631c39ba4fda0b1307f91e

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-pdfcolmk
Epoch:          12
Version:        svn78793
Release:        1%{?dist}
Summary:        Improved colour support under pdfTeX (legacy stub)
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolmk.r78793.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolmk.doc.r78793.tar.xz
BuildRequires:  tar
Provides:       texlive-pdfcolmk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pdfcolmk-doc <= 11:%{version}
Provides:       tex(pdfcolmk.sty)

%description
Improved colour support under pdfTeX (legacy stub).

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
%doc %{_texmf_main}/doc/latex/pdfcolmk/
%{_texmf_main}/tex/latex/pdfcolmk/

%changelog
%autochangelog
