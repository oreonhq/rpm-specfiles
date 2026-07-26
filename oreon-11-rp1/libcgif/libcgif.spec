%global source0_hash a5ec3b901950301981996a60a32b37f88aa44be59f8a0f5a2eb90fee8f117d5c

# remirepo/fedora spec file for libcgif
#
# SPDX-FileCopyrightText:  Copyright 2021-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit   48d28fe9f8c3a344b688bb10274447b6bb1bf0c2
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date     20211001
%global gh_owner    dloebl
%global gh_project  cgif
%global libname     libcgif
%global soname      0

Name:          %{libname}
Summary:       A fast and lightweight GIF encoder
Version:       0.5.2
Release:       1%{?dist}
License:       MIT

URL:           https://github.com/%{gh_owner}/%{gh_project}
Source0:       https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildRequires: gcc
BuildRequires: meson >= 0.56

%description
A fast and lightweight GIF encoder that can create GIF animations and images.

Summary of the main features:

- user-defined global or local color-palette with up to 256 colors
  (limit of the GIF format)
- size-optimizations for GIF animations:
  - option to set a pixel to transparent if it has identical color in the
    previous frame (transparency optimization)
  - do encoding just for the rectangular area that differs from the previous
    frame (width/height optimization)
- fast: a GIF with 256 colors and 1024x1024 pixels can be created in below
  50 ms even on a minimalistic system
- MIT license (permissive)
- different options for GIF animations: static image, N repetitions, infinite
  repetitions
- additional source-code for verifying the encoder after making changes
- user-defined delay time from one frame to the next (can be set independently
  for each frame)
- source-code conforms to the C99 standard

%package devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{libname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}*

%files devel
%doc README.md
%{_libdir}/pkgconfig/%{gh_project}.pc
%{_libdir}/%{libname}.so
%{_includedir}/%{gh_project}.h

%changelog
%autochangelog
