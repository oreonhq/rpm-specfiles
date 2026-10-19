%global source0_hash 6dd5727d7aee0822ee04fbe378ceaefdba410557d833a9af47e33ff0b6d31235
Name:           R-cpp11
Version:        %R_rpm_version 0.5.3
Release:        1%{?dist}
Summary:        A C++11 Interface for R's C Interface
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=cpp11&version=%{version}#/cpp11_%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-devel <= 0.5.2
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a header only, C++11 interface to R's C interface.  Compared to
other approaches 'cpp11' strives to be safe against long jumps from the C
API as well as C++ exceptions, conform to normal R function semantics and
supports interaction with 'ALTREP' vectors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
