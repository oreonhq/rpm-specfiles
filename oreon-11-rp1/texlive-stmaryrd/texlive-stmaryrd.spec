%global source0_hash 4d55d712d56aaae25c00b04e550a6e38feab04b12a4109d43a9a16007611df0124e1f1e975f5fd9f7d86aba2bef0e735af647fb7c3ddeee0c86cfe38ce7e5255
%global source1_hash c0ed953d18088fabeabbd41fb2559e2782ad9344208ae1b9c881124aba758ec2dba566727e45b26a9bcdf4cc5a293c0ee12d2e53ba53cb67201f508f64751979

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/stmaryrd.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-stmaryrd-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-stmaryrd-doc <= 11:%{version}
Provides:       tex(stmaryrd.sty)

%description
St Mary Road symbols for theoretical computer science.

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
%doc %{_texmf_main}/doc/fonts/stmaryrd/
%{_texmf_main}/fonts/afm/public/stmaryrd/
%{_texmf_main}/fonts/map/dvips/stmaryrd/
%{_texmf_main}/fonts/source/public/stmaryrd/
%{_texmf_main}/fonts/tfm/public/stmaryrd/
%{_texmf_main}/fonts/type1/public/stmaryrd/
%{_texmf_main}/tex/latex/stmaryrd/

%changelog
%autochangelog
