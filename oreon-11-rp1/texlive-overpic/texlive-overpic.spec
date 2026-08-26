%global source0_hash 23e3f8e5afff9f4284f46020fb1e57fd747a4c96d4ecbc2ec0e0761253f2993d
%global source1_hash b37495750fb57edaa7ed277fe7c2425b81f4543d58af2f003f0e6e160f410e91

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-overpic
Epoch:          12
Version:        svn77682
Release:        1%{?dist}
Summary:        Combine LaTeX commands over included graphics
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overpic.r77682.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/overpic.doc.r77682.tar.xz
BuildRequires:  tar
Provides:       texlive-overpic-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-overpic-doc <= 11:%{version}
Provides:       tex(overpic.sty)

%description
Combine LaTeX commands over included graphics.

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
%doc %{_texmf_main}/doc/latex/overpic/
%{_texmf_main}/tex/latex/overpic/

%changelog
%autochangelog
