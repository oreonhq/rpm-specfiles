%global source0_hash 8c47de766f965fcb50399e59d20f030e90a28e2aaac018ab1289a1a26b16cd6c9c7d3fd18f1d2b84fe86a99734bbf2ac9b58bfd723a7854bfe29141ab6acb874
%global source1_hash 3c4594f4023f6ae4dd6ac57841720a47f00ae65fcd6930d4e8ec94281a71bf97e7acea26c60d6866304b5018e866ae87554cc470e671d47ede6572da1ac2970d

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xits
Epoch:          12
Version:        svn55730
Release:        1%{?dist}
Summary:        Scientific Times-like font with OpenType math
License:        OFL-1.1
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xits.tar.xz#/xits.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/xits.doc.tar.xz#/xits.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-xits-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xits-doc <= 11:%{version}
Provides:       texlive-xits = %{epoch}:%{version}-%{release}

%description
Scientific Times-like font with OpenType math.

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
%doc %{_texmf_main}/doc/fonts/xits/
%{_texmf_main}/fonts/opentype/public/xits/

%changelog
%autochangelog
