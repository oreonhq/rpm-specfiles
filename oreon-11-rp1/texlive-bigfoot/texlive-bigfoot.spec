%global source0_hash bbd39341a6f1de3a75a8f29884043b1b43b0ed76a74854abcbdd4f91170067cdc2466803e46d140b4460e6526ba4879a2fc97a7d4e1919b29b97886a9e6b5da7
%global source1_hash 04a329ab42c010d2e6c2fc2b55992577d2d20c9e0f902f4fc32dbbe5be18f9c693b979aaa501284f77970c975d7022b23349675d89ec9114f2471d8bb6afe334

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-bigfoot
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Footnotes for critical editions (provides perpage)
License:        GPL-2.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigfoot.tar.xz#/bigfoot.or11.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/bigfoot.doc.tar.xz#/bigfoot.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-bigfoot-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-bigfoot-doc <= 11:%{version}
Provides:       tex(bigfoot.sty)
Provides:       tex(perpage.sty)
Provides:       tex(suffix.sty)

%description
Footnotes for critical editions (provides perpage).

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
%doc %{_texmf_main}/doc/latex/bigfoot/
%{_texmf_main}/tex/latex/bigfoot/

%changelog
%autochangelog
