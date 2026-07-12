%global source0_hash 227c57de96cc8ade23e158b475ccfaa534150f9c63f973454bdc5a30e4ccd0f1
%global source1_hash eaccbdc11d687f2a7068f635727ab5761a734b7d46c4b7212d14c2270b8eb260

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-was
Epoch:          12
Version:        svn64691
Release:        1%{?dist}
Summary:        A collection of small packages by Walter Schmidt
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/was.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/was.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-was-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-was-doc <= 11:%{version}
Provides:       tex(icomma.sty)
Provides:       tex(upgreek.sty)

%description
A collection of small packages by Walter Schmidt.

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
%doc %{_texmf_main}/doc/latex/was/
%{_texmf_main}/tex/latex/was/

%changelog
%autochangelog
