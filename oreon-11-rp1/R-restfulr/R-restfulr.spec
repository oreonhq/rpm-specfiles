%global source0_hash 574fd11a3f23f494ff8e94ce84d767f49d3399600d617ad26fb71b8332e93725
Name:           R-restfulr
Version:        %R_rpm_version 0.0.16
Release:        1%{?dist}
Summary:        R Interface to RESTful Web Services
License:        Artistic-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=restfulr&version=%{version}#/restfulr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Models a RESTful service as if it were a nested R list.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
