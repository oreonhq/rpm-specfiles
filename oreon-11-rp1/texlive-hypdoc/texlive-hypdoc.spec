%global source0_hash a82da717521644f01ef3a23879af30c25c22cd47a451c065a3ed65ad965b1834
%global source1_hash ad2af8a4edc95ee8bf26f8076522454a5153fab2246eec24d5478bd148420168

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-hypdoc
Epoch:          12
Version:        svn68661
Release:        1%{?dist}
Summary:        Hyper extensions for doc.sty
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypdoc.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/hypdoc.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-hypdoc-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-hypdoc-doc <= 11:%{version}
Provides:       tex(hypdoc.sty)

%description
Hyper extensions for doc.sty.

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
%doc %{_texmf_main}/doc/latex/hypdoc/
%{_texmf_main}/tex/latex/hypdoc/

%changelog
%autochangelog
