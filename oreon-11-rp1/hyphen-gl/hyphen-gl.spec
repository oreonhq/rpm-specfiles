%global source0_hash none

Name: hyphen-gl
Summary: Galician hyphenation rules
Version: 0.99
Release: 34%{?dist}
Source: https://forxa.mancomun.org/frs/download.php/534/hyph_gl.oxt
URL: https://forxa.mancomun.org/projects/hyphenation-gl
License: GPL-3.0-only
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-gl)

%description
Galician hyphenation rules.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c -n hyphen-gl

%build
chmod -x *.dic *.txt

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_gl_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_gl_ES.dic


%files
%doc LEME-gl_ANY.txt LICENCES-gl.txt LICENSES-en.txt  
%{_datadir}/hyphen/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.99-34
- Import
