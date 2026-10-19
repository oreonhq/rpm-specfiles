%global source0_hash 264a051b523ceae1795a0879e7768949ea55c586ac8db0adf1f5ebeddd2623e1
Name:           R-abind
Version:        %R_rpm_version 1.4-8
Release:        1%{?dist}
Summary:        Combine multi-dimensional arrays
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=abind&version=1.4-8#/abind_1.4-8.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Combine multi-dimensional arrays. This is a generalization of cbind and rbind. 
Takes a sequence of vectors, matrices, or arrays and produces a single array 
of the same or higher dimension.

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
