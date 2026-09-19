%global source0_hash 11672fd79d0ebd16ef90f94fda61054ea69ea9145ded03a8bdd7b304318f3aa5

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/uswds/public-sans/
Version:            1.008
%forgemeta

Release: 19%{?dist}
URL:     https://public-sans.digital.gov/

%global foundry           USWDS
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Public Sans
%global fontsummary       A strong, neutral, principles-driven, sans-serif Latin font family
%global fonts             binaries/otf/*otf binaries/variable/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Public Sans is a fork of the Libre Franklin font family. Libre Franklin is a
reinterpretation and expansion of the 1912 Morris Fuller Benton’s classic.
Public Sans has many similarities with its parent, but diverges enough in its
particulars that its effect is distinct.

Overall, Public Sans differs from Libre Franklin in its focus on long form
reading and neutral UI applicability. It takes inspiration from geometric sans
faces of the 20th century, as well as the original Franklins of the 19th,
resulting in something of a mongrel face that retains its American origin.

Public Sans is designed to work well with Apple and Google system fonts as the
base in its font stack. It’s designed to have metrics most similar to SF Pro
Text (the Apple system font) and to fall somewhere between SF Pro Text and
Roboto (the Google system font) in its overall size and appearance.}

Source0:  %{forgesource}
Source10: 58-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
