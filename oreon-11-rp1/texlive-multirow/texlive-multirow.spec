%global source0_hash 8997335f17c8820bac7daa385166c7c5dad5b7cb6107c5962bbe2b3dd42a3f0851f64ad664d538207222361dc33718d8c367198e5a0d10efa9478fc9fef19332
%global source1_hash d2ac97bc04518b277669c02afddba938b7eeb7b68ed85f9e14c13fdcb758e871cbf23a998f6463d85163ff596ae6247d89240a0dee3745b4994f7a74a448b975

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
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/multirow.tar.xz#/multirow.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/multirow.doc.tar.xz#/multirow.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-multirow-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-multirow-doc <= 11:%{version}
Provides:       tex(bigdelim.sty)
Provides:       tex(bigstrut.sty)
Provides:       tex(multirow.sty)

%description
Create tabular cells spanning multiple rows.

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
%doc %{_texmf_main}/doc/latex/multirow/
%{_texmf_main}/tex/latex/multirow/

%changelog
%autochangelog
