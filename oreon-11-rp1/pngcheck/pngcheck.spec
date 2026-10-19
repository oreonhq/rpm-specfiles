%global source0_hash a24ac2348efca5895e9d6f53fd316f3d5c409ab92a74b2b8106541759304da53
Name:           pngcheck
Version:        4.0.1
Release:        1%{?dist}
Summary:        Command-line utility to check PNG image files
License:        HPND
SourceLicense:  %{license} AND BSL-1.0
URL:            https://github.com/pnggroup/pngcheck
Source0:        https://github.com/pnggroup/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      pngcheck-extras < 4.0.0-2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(zlib)
BuildRequires:  gcc
# /oreon:deps
%description
pngcheck is a command-line utility to check PNG image files, including animated
PNG, for validity and to give information about metadate inside the file (apart
from the actual image data).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Remove bundled libraries (currently: wildargs) that are not needed on this
# platform, in order to prove they do not contribute to the binary RPMs.
rm -rv third_party/

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
