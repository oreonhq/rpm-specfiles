%global source0_hash 358149c060042968eb11748e778499c419eb68419a86842a4228c18b95cc1c474095d9ce75885bcf1493242fa11849bd209a7e0c21f4cfdfa09ebc3ebeaf0021
%global source1_hash 94089a84b829692a9edcb101e37655c039d86404cc7b0ec803ea955235233a1e3e2ae6f7a801190b7f33da436d53ad7bdfbe7b58eea1a75f13eaffabbee4f497

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-uptex-fonts
Epoch:          12
Version:        svn74119
Release:        1%{?dist}
Summary:        Fonts for use with upTeX
License:        BSD AND LicenseRef-Public-Domain AND Copyright-only
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-fonts.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-fonts.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-uptex-fonts-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-uptex-fonts-doc <= 11:%{version}
Provides:       texlive-uptex-fonts = %{epoch}:%{version}-%{release}

%description
Fonts for use with upTeX.

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
%doc %{_texmf_main}/doc/fonts/uptex-fonts/
%{_texmf_main}/fonts/cmap/uptex-fonts/
%{_texmf_main}/fonts/source/uptex-fonts/
%{_texmf_main}/fonts/tfm/uptex-fonts/
%{_texmf_main}/fonts/vf/uptex-fonts/

%changelog
%autochangelog
