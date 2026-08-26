%global source0_hash 7db75b91663a5fa711d72fba2d1934580e0570c58d2937f5f54aa3ac7cf43e15
%global source1_hash fc62df329dea13ec25279afcb8676edeb2016af034a2138d8cdb2ac1982089af

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ipaex
Epoch:          12
Version:        svn61719
Release:        1%{?dist}
Summary:        IPAex fonts for Japanese
License:        IPA
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.r61719.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ipaex.doc.r61719.tar.xz
BuildRequires:  tar
Provides:       texlive-ipaex-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ipaex-doc <= 11:%{version}
Provides:       texlive-ipaex = %{epoch}:%{version}-%{release}

%description
IPAex fonts for Japanese.

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
%doc %{_texmf_main}/doc/fonts/ipaex/
%{_texmf_main}/fonts/truetype/public/ipaex/

%changelog
%autochangelog
