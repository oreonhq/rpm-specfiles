%global source0_hash 3dcd9aeeeb8c502cc0ee908838a5154f0ea03c810cbf5d4e5088c1eee44a4079
%global source1_hash 19a40c4a368342a11d731bc3ea6c100d47735eaebe7fe1672d751a4dcdfce23f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-stmaryrd
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        St Mary Road symbols for theoretical computer science
License:        LicenseRef-Public-Domain
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-stmaryrd-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-stmaryrd-doc <= 11:%{version}
Provides:       tex(stmaryrd.sty)

%description
St Mary Road symbols for theoretical computer science.

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
%doc %{_texmf_main}/doc/fonts/stmaryrd/
%{_texmf_main}/fonts/afm/public/stmaryrd/
%{_texmf_main}/fonts/map/dvips/stmaryrd/
%{_texmf_main}/fonts/source/public/stmaryrd/
%{_texmf_main}/fonts/tfm/public/stmaryrd/
%{_texmf_main}/fonts/type1/public/stmaryrd/
%{_texmf_main}/tex/latex/stmaryrd/

%changelog
%autochangelog
