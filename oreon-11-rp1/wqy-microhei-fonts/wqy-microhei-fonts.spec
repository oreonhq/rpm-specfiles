# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2802ac8023aa36a66ea6e7445854e3a078d377ffff42169341bd237871f7213e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# SPDX-License-Identifier: MIT

%global fontname wqy-microhei
%global archivename %{fontname}-%{version}-beta

Version: 0.2.0
Release: 0.39.beta%{?dist}
URL:     http://wenq.org/wqy2/index.cgi?MicroHei(en)

%global foundry           WQY
%global fontlicense       Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0
%global fontlicenses      LICENSE_Apache2.txt LICENSE_GPLv3.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        MicroHei
%global fontsummary       Compact Chinese fonts derived from Droid
%global fonts             *.ttc
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
A new Sans Serif CJK font derived from Google's "Droid Sans Fallback"
and covers the entire GBK code points (20932 Han glyphs).
}

Source0:  http://downloads.sourceforge.net/wqy/%{archivename}.tar.gz
Source10: 66-%{fontpkgname}.conf

%fontpkg

%prep
%oreon_verify_sources
%autosetup -n %{fontname}
%linuxtext -e iso8859-1 AUTHORS.txt README.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.0-0.39.beta
- Prepare for Oreon 11 (RP1)
