%global source0_hash 1e434b13cf6cbaabb173b34334e046055366a9ec844207460a852a0066963fbdde6288e94979e873811b4e66140f07b6cf2e8526ec47a050efbfaf4836edfcb1
%global source1_hash fcf5434911390ee8f20f0feced15a627e001471b1867d57a7697edbfee557179250f0a01e9e20e0d442dcb0c4509174c504959e7a991e928e392d27515ff2d0b

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/was.tar.xz#/was.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/was.doc.tar.xz#/was.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-was-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-was-doc <= 11:%{version}
Provides:       tex(icomma.sty)
Provides:       tex(upgreek.sty)

%description
A collection of small packages by Walter Schmidt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
