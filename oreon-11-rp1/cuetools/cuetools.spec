%global source0_hash 24a2420f100c69a6539a9feeb4130d19532f9f8a0428a8b9b289c6da761eb107
Name:    cuetools
Version: 1.4.1
Release:        1%{?dist}
Summary:        Utilities to work with cue and TOC files
License: GPL-2.0-only
URL:     https://github.com/svend/cuetools
Source0:        https://github.com/svend/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  %{url}/commit/fa3b2f4.patch#/cueprint-fix-typo-in-performer-tag.patch
Patch3:  0003-cuetag.sh-Correct-typo-in-error-output.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Cuetools is a set of utilities for working with cue files and TOC files.
It includes programs for conversion between the formats, file renaming based
on cue/TOC information, and track breakpoint printing. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
