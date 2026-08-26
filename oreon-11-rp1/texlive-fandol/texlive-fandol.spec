%global source0_hash 309b19d6bff9d3e009610d698a73ba191da70cabd57157f274dfca7583a9e9b31fc30ea52b2b2ab3386be7290a680f8eb47dc92381c3da8251b01d8c6a65c3ff
%global source1_hash d74e78a1c863d3865ec4b21a4c762bf6e2c30a8656fe0ec830d1e56b9fcb48861f316ccf8d8641e7c674e25f1ac2292d10ff2127315275347096ad325828d7e5

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-fandol
Epoch:          12
Version:        svn37889
Release:        1%{?dist}
Summary:        Four basic fonts for CJK typesetting
License:        GPL-3.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-fandol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fandol-doc <= 11:%{version}
Provides:       texlive-fandol = %{epoch}:%{version}-%{release}

%description
Four basic fonts for CJK typesetting.

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
%doc %{_texmf_main}/doc/fonts/fandol/
%{_texmf_main}/fonts/opentype/public/fandol/

%changelog
%autochangelog
