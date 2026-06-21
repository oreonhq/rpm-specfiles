%global source0_hash 3f76753c0c6e3945686be56651179d9789ca62c2bac2cef8003148452b529155
%global source1_hash c8f65c028105366683acbb80a274162db8ecc2e7592398bd44a6cae7ed432af8

%global source_date 20260301
%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-texlive-scripts
Epoch:          12
Version:        %{source_date}
Release:        111%{?dist}
Summary:        TeX Live infrastructure scripts (bootstrap CTAN drop)
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-texlive-scripts = %{epoch}:%{version}-%{release}
Provides:       tex-texlive-scripts = %{epoch}:%{version}-%{release}
Provides:       texlive-texlive-scripts-bin = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-texlive-scripts-bin < 7:20170520

%description
CTAN script tree for texlive-texlive-scripts. Enough to satisfy texlive-base
bootstrap builddeps. fmtutil and friends land after texlive-base rebuilds this
subpackage from source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texdir}
tar -xf %{SOURCE0} -C %{buildroot}%{_texdir}
tar -xf %{SOURCE1} -C %{buildroot}%{_texdir}
rm -rf %{buildroot}%{_texmf_main}/tlpkg/tlpobj/*.tlpobj

%files
%{_texmf_main}/scripts/texlive/
%{_texmf_main}/dvips/tetex/
%{_texmf_main}/fonts/enc/dvips/tetex/
%{_texmf_main}/fonts/map/dvips/tetex/
%doc %{_texmf_main}/doc/man/man1/fmtutil*
%doc %{_texmf_main}/doc/man/man1/install-tl*
%doc %{_texmf_main}/doc/man/man1/mktex*
%doc %{_texmf_main}/doc/man/man1/updmap*
%doc %{_texmf_main}/doc/man/man5/updmap*

%changelog
%autochangelog
