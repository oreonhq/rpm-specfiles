%global source0_hash 191799a80f3a833dcad0ffe0e6ea73bfce3c1a7cd4c6e00839687a0e695834ab
Name:           R-rle
Version:        %R_rpm_version 0.10.0
Release:        1%{?dist}
Summary:        Common Functions for Run-Length Encoded Vectors
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rle&version=%{version}#/rle_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Common 'base' and 'stats' methods for 'rle' objects, aiming to make it
possible to treat them transparently as vectors.

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
