%global source0_hash 6ef0ee6876fbbed01ecf5c6150ad2d38709fcb83560b7acd5860e381371ae1d6
Name:           R-geepack
Version:        %R_rpm_version 1.3.13
Release:        1%{?dist}
Summary:        Generalized Estimating Equation Package
License:        GPL-3.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=geepack&version=%{version}#/geepack_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.3.13
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Generalized estimating equations solver for parameters in mean, scale, and
correlation structures, through mean link, scale link, and correlation
link. Can also handle clustered categorical responses.

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
