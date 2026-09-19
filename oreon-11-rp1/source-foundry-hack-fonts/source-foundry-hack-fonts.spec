%global source0_hash d9ed5d0a07525c7e7bd587b4364e4bc41021dd668658d09864453d9bb374a78d

Version: 3.003
Release: 7%{dist}
URL: https://sourcefoundry.org/hack/

%global foundry           source-foundry
%global fontlicense       MIT AND Bitstream-Vera
%global fontlicenses      LICENSE.md
%global fontdocs          README.md
%global fontdocsex        %{fontlicenses}

%global fontfamily Hack
%global fontsummary A typeface designed for source code

%global fonts             *.ttf
%global fontconfs         45-Hack.conf

%global fontdescription   %{expand:
Hack is designed to be a workhorse typeface for source code. It has deep roots
in the free, open source typeface community and expands upon the contributions
of the Bitstream Vera & DejaVu projects.
The large x-height + wide aperture + low contrast design make it legible at
commonly used source code text sizes with a sweet spot that runs in the
8 - 14 range.

Hack is a derivative of upstream Bitstream Vera Sans Mono and DejaVu Sans Mono
source. The Hack changes are licensed under the MIT license.
Bitstream Vera Sans Mono is licensed under the Bitstream Vera license and
maintains reserved font names "Bitstream" and "Vera". The DejaVu changes to
the Bitstream Vera source were committed to the public domain.
}

Source0: https://github.com/source-foundry/Hack/releases/download/v%{version}/Hack-v%{version}-ttf.tar.xz
Source1: https://github.com/source-foundry/Hack/raw/v%{version}/LICENSE.md
Source2: https://github.com/source-foundry/Hack/raw/v%{version}/README.md

# https://github.com/source-foundry/Hack/pull/644
# Use systemId urn:fontconfig:fonts.dtd to reference the fonts.dtd type defintion #644
Patch0: https://github.com/source-foundry/Hack/pull/644.patch

Source10: https://github.com/source-foundry/Hack/raw/v%{version}/config/fontconfig/45-Hack.conf

BuildRequires: fontconfig

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE10} .
%patch -P0 -p3

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
