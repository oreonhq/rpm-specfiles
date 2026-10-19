%global source0_hash 5a36fabb6d62ba2533d3fc4cececd07891942cfb76fe689ec0d550d08762f61c
Name:           R-png
Version:        %R_rpm_version 0.1-8
Release:        1%{?dist}
Summary:        Read and write PNG images
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=png&version=0.1-8#/png_0.1-8.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libpng-devel
# /oreon:deps
%description
This package provides an easy and simple way to read, write and display
bitmap images stored in the PNG format. It can read and write both files
and in-memory raw vectors.

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
