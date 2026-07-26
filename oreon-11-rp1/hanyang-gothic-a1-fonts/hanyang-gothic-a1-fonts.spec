%global source0_hash 829a1455077398f7d379bcd5567ff2a9bed7b0f6eea80026699c4581a8e4b7d0

%global git_date   20180313
%global git_commit 16680f8688ffcd467d2eb2146a9ce0343404581d
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:8}")

Version: 163840
Release: 16.%{git_date}git%{git_commit_short}%{?dist}

URL: https://www.hanyang.co.kr/hygothic/

%global foundry  HanYang
%global fontlicense  OFL-1.1
%global fontlicenses  OFL.txt

%global fontfamily  Gothic A1
%global fontsummary  HanYang Gothic A1, an elegant Korean and Latin font

%global fontdescription  %{expand:HanYang I&C Co's Gothic A1 is an elegant font for Korean and Latin text,
available in 9 weights.}

%global fonts  *.ttf
%global fontconfs  %{SOURCE10}

# Archive created by running the gothicA1-fetch.sh script (see Source99)
%global archivename HanYang-GothicA1-%{git_commit}
Source0: %{archivename}.zip

Source10: 60-%{fontpkgname}.xml

# A script to fetch the font files from Google Fonts repo on GitHub
Source99: gothicA1-fetch.sh

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
