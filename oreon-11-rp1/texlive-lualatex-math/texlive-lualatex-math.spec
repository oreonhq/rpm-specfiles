%global source0_hash d20188549889ac56c1f3f886f56ca787247a7e323d4d0a1664bd0a95427ef70228e3ae0fe316faacf2107f37c22fe81f7945fdaee4be9ee7613216f95bc73f1e
%global source1_hash 585bfea74421522fd22643165cdf4a14b675d6ea44e5e1ae4410a49c8718dff7d945cf1b21834e9b59341dcf497669a840231e3e465cb4403c4064d27d22387e

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-lualatex-math
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Fixes for mathematics-related LuaLaTeX issues
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-math.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualatex-math.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-lualatex-math-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-lualatex-math-doc <= 11:%{version}
Provides:       tex(lualatex-math.lua)
Provides:       tex(lualatex-math.sty)

%description
Fixes for mathematics-related LuaLaTeX issues.

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
%doc %{_texmf_main}/doc/lualatex/lualatex-math/
%{_texmf_main}/tex/lualatex/lualatex-math/

%changelog
%autochangelog
