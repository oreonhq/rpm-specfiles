%global source0_hash f654b51046e241ef76efe76bb5c60bbbb49296c2f32e71c764222c7c006be258cc7b8a89247bf56df7757cac1af733298e72b4d4f8e6022c351cf60a50734453

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-chicago
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Chicago bibliography style
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/chicago.tar.xz
BuildRequires:  tar
Provides:       tex(chicago.bst)
Provides:       tex(chicago.sty)

%description
Chicago bibliography style.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%build

%install
mkdir -p %{buildroot}%{_texmf_main}
tar -xf %{SOURCE0} -C %{buildroot}%{_texmf_main}
rm -rf %{buildroot}%{_texmf_main}/tlpkg

%files
%{_texmf_main}/bibtex/bst/chicago/
%{_texmf_main}/tex/latex/chicago/

%changelog
%autochangelog
