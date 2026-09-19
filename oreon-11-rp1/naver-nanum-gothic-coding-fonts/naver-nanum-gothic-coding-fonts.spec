%global source0_hash 177317f060e305fa1dca079d453584d9ca7880153c992b188128c6b3b75ece2a

# SPDX-License-Identifier: MIT

Version: 2.000
Release: 28%{?dist}
URL:     http://dev.naver.com/projects/nanumfont/

%global foundry           Naver
%global fontlicense       OFL-1.1

%global fontfamily        Nanum Gothic Coding
%global fontsummary       Nanum Gothic Coding family of Korean TrueType fonts
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Nanum Gothic Coding fonts are set of Gothic Korean font faces suitable
for source code editing, designed by Sandoll Communication and
published by NAVER Corporation.
}

# NanumGothic_Coding has a mirror redirector for its downloads
# You can get this zip archive by following a link from:
# http://dev.naver.com/projects/nanumfont/download/note/214
Source0:  NanumGothicCoding-2.0.zip
Source10: 67-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
for i in *.ttf; do
  case $i in
    *-Bold.ttf)
      mv $i NanumGothic_Coding_Bold.ttf
      ;;
    *)
      mv $i NanumGothic_Coding.ttf
  esac
done

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
