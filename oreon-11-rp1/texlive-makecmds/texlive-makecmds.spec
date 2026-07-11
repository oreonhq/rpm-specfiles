%global source0_hash fedccafd77cd62889a9d9947003b49a762756d9cdaa104618247f5045a00ba37
%global source1_hash e99ea4717a91e13354503a4f2cf4933d60d2ebd1c7b77bf5e78e05b4144bb7f5

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-makecmds
Epoch:          12
Version:        svn79618
Release:        1%{?dist}
Summary:        The makecmds package
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makecmds.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/makecmds.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-makecmds-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-makecmds-doc <= 11:%{version}
Provides:       tex(makecmds.sty)

%description
The makecmds package.

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
%doc %{_texmf_main}/doc/latex/makecmds/
%{_texmf_main}/tex/latex/makecmds/

%changelog
%autochangelog
