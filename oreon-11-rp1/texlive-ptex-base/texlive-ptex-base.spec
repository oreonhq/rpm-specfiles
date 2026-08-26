%global source0_hash 90329aebe0f38c5468317526ca8f16a2a576c533500efae46cd61ba5b3198ebb
%global source1_hash e74a02f2655d708db49e155f363878648de4251756ee86f8da271bcf22989459

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-ptex-base
Epoch:          12
Version:        svn64072
Release:        1%{?dist}
Summary:        Plain TeX format and docs for pTeX base
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.r64072.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/ptex-base.doc.r64072.tar.xz
BuildRequires:  tar
Provides:       texlive-ptex-base-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-ptex-base-doc <= 11:%{version}
Provides:       tex(ascii-jplain.tex)
Provides:       tex(kinsoku.tex)
Provides:       tex(ptex.tex)

%description
Plain TeX format and docs for pTeX base.

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
%doc %{_texmf_main}/doc/ptex/ptex-base/
%{_texmf_main}/tex/ptex/ptex-base/

%changelog
%autochangelog
