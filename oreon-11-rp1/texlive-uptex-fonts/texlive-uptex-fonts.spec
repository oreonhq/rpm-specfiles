%global source0_hash 28541dbebc85163bcf7d8237a16f3b61f4f3803e18c555cc44d6c962db39ac65
%global source1_hash 2aafd45ceff308c32f5cae1856620850990163a97f2b1eb1502e9a5d7d6bfbac

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
