%global source0_hash none

Name: hyphen-gl
Summary: Galician hyphenation rules
Version: 0.99
Release: 34%{?dist}
Source: https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://forxa.mancomun.org/projects/hyphenation-gl
License: GPL-3.0-only
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-gl)

%description
Galician hyphenation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2

%build
chmod -x dictionaries/gl/hyph_gl.dic

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/gl/hyph_gl.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_gl_ES.dic


%files
%doc dictionaries/gl/README_hyph_gl.txt
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.99-34
- Import
