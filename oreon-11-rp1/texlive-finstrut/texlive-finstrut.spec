%global source0_hash 67eef9a82be4a94e1d7f3072132bb3031c43c4d75e16b51b294e6170985f12a0
%global source1_hash 9fdfe3b2e9f350fb6f30c02606d4c10e35b41a845ee56d7845ef11bda62b7bbf

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-finstrut
Epoch:          12
Version:        svn21719
Release:        1%{?dist}
Summary:        Adjust behaviour of the ends of footnotes
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/finstrut.r21719.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/finstrut.doc.r21719.tar.xz
BuildRequires:  tar
Provides:       texlive-finstrut-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-finstrut-doc <= 11:%{version}
Provides:       tex(finstrut.sty)

%description
Adjust behaviour of the ends of footnotes.

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
%doc %{_texmf_main}/doc/latex/finstrut/
%{_texmf_main}/tex/latex/finstrut/

%changelog
%autochangelog
