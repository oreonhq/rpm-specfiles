%global source0_hash 8b550ce7ed404d0c159520426469fcf4baf55ee9956503a27f36269c2615f006
%global source1_hash b246662e053edc96a5e5e9e0d02b92d201ee0fcf9f1f0b1e4a0b42984c8d8354

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-tocvsec2
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Section numbering and table of contents control
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tocvsec2.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tocvsec2.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-tocvsec2-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-tocvsec2-doc <= 11:%{version}
Provides:       tex(tocvsec2.sty)

%description
Section numbering and table of contents control.

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
%doc %{_texmf_main}/doc/latex/tocvsec2/
%{_texmf_main}/tex/latex/tocvsec2/

%changelog
%autochangelog
