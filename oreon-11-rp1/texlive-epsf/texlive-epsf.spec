%global source0_hash fcfc33e82157175049af4353ef88f2f68d0a37f3a285c8c2eb458b36fadd079297b0c4e3a67d1866c2cee04bce8a3e7b2741e29d0f274d702d05c5e8c2ca65c9
%global source1_hash 8fbfa86597fff6e126f7510378d408cb0b7681e6643bf047a98753161be8c0ae86fec1870377c91237634c46aef976f8d5756ae50ebb0f1056614af363bdd08a

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-epsf
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Simple macros for EPS inclusion
License:        Public Domain
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/epsf.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-epsf-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-epsf-doc <= 11:%{version}
Provides:       tex(epsf.sty)
Provides:       tex(epsf.tex)

%description
Simple macros for EPS inclusion.

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
%license %{_texmf_main}/doc/generic/epsf/LICENSE
%doc %{_texmf_main}/doc/generic/epsf/
%{_texmf_main}/tex/generic/epsf/
%exclude %{_texmf_main}/doc/generic/epsf/LICENSE

%changelog
%autochangelog
