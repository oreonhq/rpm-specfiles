%global source0_hash db0be3360dc3d6373866c9d27900f8dba9353bcf92d219f9f0b82532e2855210230a06b87d1ab6eef7e1f96c54e46884e6827395affb9375120b7cf8d2fbb99b
%global source1_hash 6a9958bc6ddf6d167b9d77a513d04f0077c9a8581109c51166410d60d5a243758da62b40bdf5cb1488a50b9ba76ca89261a2d31c3819d8b2738b4a7023ac3f90

%global _texdir /usr/share/texlive
%global _texmf_main %{_texdir}/texmf-dist

Name:           texlive-xcjk2uni
Epoch:          12
Version:        svn54958
Release:        1%{?dist}
Summary:        Convert CJK characters to Unicode
License:        LPPL-1.3c
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xcjk2uni.tar.xz#/xcjk2uni.or11.tar.xz
Source1:        https://texlive.info/tlnet-archive/2026/08/29/tlnet/archive/xcjk2uni.doc.tar.xz#/xcjk2uni.doc.or11.tar.xz
BuildRequires:  tar
Provides:       texlive-xcjk2uni-doc = %{epoch}:%{version}-%{release}
Obsoletes:      texlive-xcjk2uni-doc <= 11:%{version}
Provides:       tex(xCJK2uni.sty)
Provides:       tex(xCJK2uni-UBg5plus.def)
Provides:       tex(xCJK2uni-UBig5.def)
Provides:       tex(xCJK2uni-UGB.def)
Provides:       tex(xCJK2uni-UGBK.def)
Provides:       tex(xCJK2uni-UJIS.def)
Provides:       tex(xCJK2uni-UKS.def)

%description
Convert CJK characters to Unicode.

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
%doc %{_texmf_main}/doc/latex/xcjk2uni/
%{_texmf_main}/tex/latex/xcjk2uni/

%changelog
%autochangelog
