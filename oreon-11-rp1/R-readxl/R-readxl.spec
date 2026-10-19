%global source0_hash 09d70d7bbafbe129ce687b8743dbf6b9d0f201205b30dc515a00b35fcc1bdedf
Name:           R-readxl
Version:        %R_rpm_version 1.4.5
Release:        1%{?dist}
Summary:        Read Excel Files
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=readxl&version=%{version}#/readxl_%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides:       bundled(rapidxml-devel) = 1.13
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libxls-devel
# /oreon:deps
%description
Import excel files into R. Supports '.xls' via the 'libxls' C library
<https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <http://rapidxml.sourceforge.net>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Remove bundled libxls.
rm -rf readxl/src/{Makevars.win,libxls,unix,windows}
sed -i '5,$d' readxl/src/Makevars
echo "PKG_LIBS=-lxlsreader" > readxl/src/Makevars
find readxl/src -type f -exec sed -i 's@include "libxls/xls.h"@include <xls.h>@g' {} \;

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
