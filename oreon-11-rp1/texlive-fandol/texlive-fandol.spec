%global source0_hash 0b71eebb1c9b9fbd1eb4281f8af3f6c1a556a394ba2b6eae69ed9bb76c5fa56a
%global source1_hash bc612f810ba56397700b678adecd43613f35a6fce9f4204c3357b874709843d0

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-fandol
Epoch:          12
Version:        svn37889
Release:        1%{?dist}
Summary:        Four basic fonts for CJK typesetting
License:        GPL-3.0-or-later
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/fandol.doc.tar.xz
BuildRequires:  tar
Provides:       texlive-fandol-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-fandol-doc <= 11:%{version}
Provides:       texlive-fandol = %{epoch}:%{version}-%{release}

%description
Four basic fonts for CJK typesetting.

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
%doc %{_texmf_main}/doc/fonts/fandol/
%{_texmf_main}/fonts/opentype/public/fandol/

%changelog
%autochangelog
