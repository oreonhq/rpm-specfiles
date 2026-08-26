%global source0_hash 3e30ef7f14bb136c8ba3029077502f4c854c6d231e4776a412a0c02926d9475225c54af2d897445506e5cbf719ef37177898798513db5108f5a5c96c10ce10f2
%global source1_hash 1974cf5e8ba3989e72a59b250012b880da357d08756a2a13dda7fad56623a3bad4b5b2d16494db51a6cef924a1e6b872f8fd59a39d62a792f6e15a3497c61904

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-uptex-base
Epoch:          12
Version:        svn77840
Release:        1%{?dist}
Summary:        Plain TeX formats and documents for upTeX
License:        BSD
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/uptex-base.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-uptex-base-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-uptex-base-doc <= 11:%{version}
Provides:       tex(ukinsoku.tex)
Provides:       tex(uptex.tex)

%description
Plain TeX formats and documents for upTeX.

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
%doc %{_texmf_main}/doc/uptex/uptex-base/
%{_texmf_main}/tex/uptex/uptex-base/

%changelog
%autochangelog
