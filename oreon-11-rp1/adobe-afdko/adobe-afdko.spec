%global source0_hash 083b504a1cd865e8bfbb42134a34318ce42ef5130daebfc5b0e2f2fb444326c5
%global source1_hash 0ed13668906e86dbc0dcddf30fdee68c10203dea4e83852b4edb810821bee3c4
%global antl4_ver 4.13.2
Name:		adobe-afdko
Version:	5.0.1
Release:        1%{?dist}
Summary:        Adobe Font Development Kit for OpenType
License:	Apache-2.0
URL:		https://github.com/adobe-type-tools/afdko
Source0:        https://github.com/adobe-type-tools/afdko/releases/download/%{version}/afdko-%{version}.tar.gz
Source1:        https://www.antlr.org/download/antlr4-cpp-runtime-4.13.2-source.zip
Provides: bundled(antlr4-project) = %{antl4_ver}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  python3-devel
BuildRequires:  utf8cpp-devel
# /oreon:deps
%description
Adobe Font Development Kit for OpenType (AFDKO).
The AFDKO is a set of tools for building OpenType font files
from PostScript and TrueType font data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir afdko-%{version}
%oreon_prep
%build

%set_build_flags
export XFLAGS="${CFLAGS} ${LDFLAGS}"
%cmake \
  -DANTLR4_ZIP_REPOSITORY:PATH=%{SOURCE1} \
  -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
  -DAFDKO_USE_SYSTEM_LIBXML2=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
