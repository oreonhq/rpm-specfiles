%global source0_hash ae68c492db156dd0320dbbe64719585cdc028a420f8e42ac71c4352c4891e309

%global commit fb73260e86dd301b383cf6cc9ca8e726ef806535
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ghowner theleagueof
%global ghproject junction

Version: 0^20140329gitfb73260
Release: 8%{?dist}

URL: https://www.theleagueofmoveabletype.com/junction

%global foundry  LOMT
%global fontlicense  OFL-1.1
%global fontlicenses  OpenFontLicense.markdown

%global fontfamily  Junction
%global fontsummary A humanist sans-serif typeface
%global fontdescription  %{expand:Junction is a a humanist sans-serif,
and the first open-source type project started by The League of Moveable
Type. It has been updated (2014) to include additional weights (light/bold)
and expanded international support.}

%global fonts  *.otf
%global fontconfs  %{SOURCE10}

Source0: https://github.com/%{ghowner}/%{ghproject}/archive/%{commit}/%{ghproject}-%{shortcommit}.tar.gz
Source10: 60-%{fontpkgname}.xml
# https://github.com/theleagueof/junction/issues/16
Source11: update-names.pe
Source12: update-foundry.pe 

BuildRequires: fontforge

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{ghproject}-%{commit}
mv 'Open Font License.markdown' OpenFontLicense.markdown
mv 'Open Font License FAQ.markdown' OpenFontLicenseFAQ.markdown

%build
cp %{SOURCE11} .
cp %{SOURCE12} .
fontforge -script update-names.pe Junction-bold.otf Junction "Junction Bold" Bold temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-bold.otf
fontforge -script update-names.pe Junction-regular.otf Junction "Junction" Regular temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-regular.otf
fontforge -script update-names.pe Junction-light.otf Junction "Junction Light" Light temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-light.otf

rm temp.sfd
rm update-names.pe
rm update-foundry.pe

%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles
%doc readme.markdown
%doc OpenFontLicenseFAQ.markdown

%changelog
%autochangelog
