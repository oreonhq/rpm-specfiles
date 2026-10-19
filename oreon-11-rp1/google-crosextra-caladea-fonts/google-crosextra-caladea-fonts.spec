%global source3_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash c48d1c2fd613c9c06c959c34da7b8388059e2408d2bb19845dc3ed35f76e4d09
%global archivename crosextrafonts-20130214
Version:        1.002
Release:        1%{?dist}
Epoch:          1
URL:            http://code.google.com/p/chromium/issues/detail?id=168879
%global foundry           Google Crosextra
%global fontlicense       Apache-2.0
%global fontlicenses      LICENSE-2.0.txt
%global fontfamily        Caladea
%global fontsummary       Serif font metric-compatible with Cambria font
%global fonts             *.ttf
%global fontconfs         %{SOURCE1} %{SOURCE2}
%global fontdescription   %{expand:
Caladea is metric-compatible with Cambria font. This font is a serif
typeface family based on Lato.
}
Source0:        https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/crosextrafonts-20130214.tar.gz
Source1:        30-0-%{fontpkgname}.conf
Source2:        62-%{fontpkgname}.conf
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt
%global fontpkgheader     %{expand:
Obsoletes: ht-caladea-fonts < 1:1.001-10.20200428git336a529
}
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{archivename}
cp -p %{SOURCE3} .

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.002-0.22.20130214
- Import
