%global source0_hash 642f893b494b05299c66a02b3a8af218f60a179ec009843a96f4b12435616c1c6f570ff57ae439e3e8cfa1bb08fe56f15d259b599c35addadd0abcb806b8e1d6
%global source1_hash 3f8e0c256bb6b9200114f541f38c6b681574f32e7a0e87afc4a84de54982ba32e4638470af4d7e582380323e237e757a74aff501f8160859794d3cb102c2fc3f

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-sauerj
Epoch:          12
Version:        svn15878
Release:        1%{?dist}
Summary:        A bundle of utilities by Jonathan Sauer
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sauerj.r79618.tar.xz
Source1:        https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/sauerj.doc.r79618.tar.xz
BuildRequires:  tar
Provides:       texlive-sauerj-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-sauerj-doc <= 11:%{version}
Provides:       tex(collect.sty)
Provides:       tex(metainfo.sty)
Provides:       tex(optparams.sty)
Provides:       tex(parcolumns.sty)
Provides:       tex(processkv.sty)
Provides:       tex(zahl2string.sty)

%description
A bundle of utilities by Jonathan Sauer.

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
%doc %{_texmf_main}/doc/latex/sauerj/
%{_texmf_main}/tex/latex/sauerj/

%changelog
%autochangelog
