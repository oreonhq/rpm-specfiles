%global source0_hash 2139efbd48fbcc590a401e40215573f4a214432536bc8967caa163a833b03729
Name:           R-jpeg
Version:        %R_rpm_version 0.1-11
Release:        1%{?dist}
Summary:        Read and write JPEG images
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=jpeg&version=0.1-11#/jpeg_0.1-11.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libjpeg-devel
# /oreon:deps
%description
This package provides an easy and simple way to read, write and display
bitmap images stored in the JPEG format. It can read and write both files
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
