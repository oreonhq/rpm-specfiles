%global source0_hash 84b85d559d1a08c48d3250643f80f1685138334d8c267a9e952f3cab1c840ec2
%global source1_hash 6a73b90559914fb1947820ea25fa086348ddac81994b65fffda1eff27711a8bb

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-multirow
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Create tabular cells spanning multiple rows
License:        LPPL-1.3c OR LPPL-1.0
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multirow.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/multirow.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-multirow-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-multirow-doc <= 11:%{version}
Provides:       tex(bigdelim.sty)
Provides:       tex(bigstrut.sty)
Provides:       tex(multirow.sty)

%description
Create tabular cells spanning multiple rows.

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
%doc %{_texmf_main}/doc/latex/multirow/
%{_texmf_main}/tex/latex/multirow/

%changelog
%autochangelog
