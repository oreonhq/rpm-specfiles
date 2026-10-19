%global source0_hash 35ef6e8956520279f44d538c613ff9605bc594fed46133200d61937828fc6b64
Name:           R-reshape
Version:        %R_rpm_version 0.8.10
Release:        1%{?dist}
Summary:        Flexibly Reshape Data
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=reshape&version=%{version}#/reshape_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Flexibly restructure and aggregate data using just two functions: melt and
cast.

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
