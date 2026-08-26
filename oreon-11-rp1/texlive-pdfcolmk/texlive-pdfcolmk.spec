%global source0_hash 73018fd6fa70215b5ab2e5dafc94370e36457891034e7476a5cb1f0f993fc7bdd21c5d165095caf60f89495ac2ac847371e40cd44125bd51693f67b2c3fe319a
%global source1_hash d1d2ac7ec1936018773ec46c87e6960936928adb4686c4ed8271855ae00a71111e8c6be47302149f2a0de57a95275abefc774949ae9608bafba79cf5be9a726a

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolmk.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/pdfcolmk.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-pdfcolmk-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-pdfcolmk-doc <= 11:%{version}
Provides:       tex(pdfcolmk.sty)

%description
Improved colour support under pdfTeX (legacy stub).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; if test ${#%{source0_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; if test ${#%{source1_hash}} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
