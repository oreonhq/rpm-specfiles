%global source0_hash b69b0781318e175532ad2d4f2840553bade9637e04de215b581704b5635c45d3
Name:           R-itertools
Version:        %R_rpm_version 0.1-3
Release:        1%{?dist}
Summary:        Iterator Tools
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=itertools&version=0.1-3#/itertools_0.1-3.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Various tools for creating iterators, many patterned after functions in
the Python itertools module, and others patterned after functions in the
'snow' package.

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
