%global source0_hash 6cd2773ffc1c5feaf2574653ec2c8a674eb1783c34b54a49469eecfaf0d10f3da000a555a382601ae32561233ca7f5011c0d42bd028d33fd437d547c3cf10501
%global source1_hash 3d6ad98e4826de522f5483357dcf772870962ebbc2844b8b2e3212a8b3b4b1fa195a6717a641324e2b103bf6903f38a86586e899e7045da7bbd55cbf1f3c6f02

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-algorithms
Epoch:          12
Version:        svn78101
Release:        1%{?dist}
Summary:        A suite of tools for typesetting algorithms in pseudo-code
License:        LGPL-2.1-only
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/algorithms.tar.xz#/algorithms.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/algorithms.doc.tar.xz#/algorithms.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-algorithms-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-algorithms-doc <= 11:%{version}
Provides:       tex(algorithm.sty)
Provides:       tex(algorithmic.sty)

%description
A suite of tools for typesetting algorithms in pseudo-code.

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
%license %{_texmf_main}/doc/latex/algorithms/COPYING
%doc %{_texmf_main}/doc/latex/algorithms/
%{_texmf_main}/tex/latex/algorithms/
%exclude %{_texmf_main}/doc/latex/algorithms/COPYING

%changelog
%autochangelog
