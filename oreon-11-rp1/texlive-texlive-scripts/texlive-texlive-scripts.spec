%global source0_hash c218dfde1b249e1466a12b7f7fef7764b7e644c58dbc5a700409711ce8871b36debd6cf730431ded663933c9d617ac836328ed5738d0b436bf8d486cb5d6eb22
%global source1_hash e4bda7d1f2e3f4bc783e44cd031222d6db03fe2bcc892b6ab0307117e9fd0d686b8fd90cb61963400cc6178db25fe8cec1c9fe3e7b6feeb56e41348d3e8b0813

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
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.r80099.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/texlive-scripts.doc.r80099.tar.xz
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
rm -rf %{buildroot}%{_texdir}/tlpkg
rm -f %{buildroot}%{_texdir}/doc.html
rm -f %{buildroot}%{_texdir}/install-tl

%files
%{_texmf_main}/scripts/texlive/
%{_texmf_main}/dvips/tetex/
%{_texmf_main}/fonts/enc/dvips/tetex/
%{_texmf_main}/fonts/map/dvips/tetex/
%{_texmf_main}/web2c/updmap.cfg
%doc %{_texmf_main}/doc/man/man1/fmtutil*
%doc %{_texmf_main}/doc/man/man1/install-tl*
%doc %{_texmf_main}/doc/man/man1/mktex*
%doc %{_texmf_main}/doc/man/man1/texhash*
%doc %{_texmf_main}/doc/man/man1/updmap*
%doc %{_texmf_main}/doc/man/man5/fmtutil.cnf*
%doc %{_texmf_main}/doc/man/man5/updmap*

%changelog
%autochangelog
