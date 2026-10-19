%global source0_hash 251283e6fa2ff82c31145d43aabd54e83bb7e673bfc764376a2e0dc50e924889
Name:           R-showtext
Version:        %R_rpm_version 0.9-7
Release:        1%{?dist}
Summary:        Using Fonts More Easily in R Graphs
License:        Apache-2.0 AND Zlib
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=showtext&version=0.9-7#/showtext_0.9-7.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
# /oreon:deps
%description
Making it easy to use various types of fonts (TrueType, OpenType, Type 1, web
fonts, etc.) in R graphs, and supporting most output formats of R graphics
including PNG, PDF and SVG. Text glyphs will be converted into polygons or
raster images, hence after the plot has been created, it no longer relies on
the font files. No external software such as Ghostscript is needed to use this
package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
