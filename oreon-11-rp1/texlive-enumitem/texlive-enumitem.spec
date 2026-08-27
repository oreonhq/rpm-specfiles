%global source0_hash 6bbdd89a92a18e8b59c9a9f1a2da203da7c34a73fefd4974a5b4dcd8c9ab457c20e8555a2f6c01eb55ef722ae8ee4a943dbca41b905d83c8eceba2b87917baa0
%global source1_hash 3fa51446d8a8dd7860b96770faeb3197d59055683fe42263ddaaab9f0b0c1af43ec8e886d84cc49ec09655496b4b5af98b32496d45ab1266fee4911dacdcbbf1

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-enumitem
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        Control layout of itemize, enumerate, description
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enumitem.tar.xz#/enumitem.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/enumitem.doc.tar.xz#/enumitem.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-enumitem-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-enumitem-doc <= 11:%{version}
Provides:       tex(enumitem.sty)

%description
Control layout of itemize, enumerate, description.

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
%doc %{_texmf_main}/doc/latex/enumitem/
%{_texmf_main}/tex/latex/enumitem/

%changelog
%autochangelog
