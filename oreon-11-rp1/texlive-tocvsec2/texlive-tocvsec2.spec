%global source0_hash 0f4a81257702c1facedce68b2f49fdf020f17d1accdbb8c472d82023fa20b6e295c97fb73216e9aeb6539601ab3b0e73a61b988f87b7105135e2512fcda1a7d5
%global source1_hash c31cb6bb9372cf34ecbee22e1cb7e6910794a84ce1cbdb00094bce2e74a682a79339c669abc6902c788cecbf3536171720060e9c0f8a4e7feaf24353e5ecdfb8

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h_expected="%{source0_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h_expected="%{source1_hash}"; if test ${#h_expected} -eq 128; then h=$(sha512sum "$f" | awk '{print $1}'); else h=$(sha256sum "$f" | awk '{print $1}'); fi; test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }

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
