%global source0_hash b08e894cb7063f06a980e61506064ecbfa1b373b7fdc49b4c82bd80c15aaed23
%global source1_hash 52b17527faa177ee5f9818f0ce9c9d2df8c0acf37afc8180f23372475068595b

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xurl
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Allow URL breaks at any alphanumerical character
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xurl.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xurl.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-xurl-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xurl-doc <= 11:%{version}
Provides:       tex(xurl.sty)

%description
Allow URL breaks at any alphanumerical character.

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
%doc %{_texmf_main}/doc/latex/xurl/
%{_texmf_main}/tex/latex/xurl/

%changelog
%autochangelog
