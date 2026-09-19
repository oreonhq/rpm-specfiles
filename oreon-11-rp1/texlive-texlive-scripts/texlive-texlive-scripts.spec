%global source0_hash d5c2bb72026aef59cac3fbd7533385d0cc8fba5a511dc4456dbe6b178cd26a541849acf918e158bd28d72d680f9cd26400b40cf31b053e892532cfd8266bae52
%global source1_hash 168039c29bf2434b1a7ee35f3a0a37bd9e7b7d7ab05d825c0a0dee43f573f01872f5000a3e19a06365fd610fe5e525be6896d486d2b6463da7ccfcb7270425ed

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
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-scripts.tar.xz#/texlive-scripts.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/texlive-scripts.doc.tar.xz#/texlive-scripts.doc.or11.tar.xz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
