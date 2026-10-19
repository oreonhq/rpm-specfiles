%global source0_hash b94ddacdfa43e9a36955ecf7d30fe9fc5a137a8209f6ab9303542a932ab61cda
%global _R_libdir_check %{nil}
Name:           R-data.table
Version:        %R_rpm_version 1.18.0
Release:        1%{?dist}
Summary:        Extension of `data.frame`
License:        MPL-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=data.table&version=%{version}#/data.table_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.18.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
fast add/modify/delete of columns by group using no copies at all, list
columns, friendly and fast character-separated-value read/write. Offers a
natural and flexible syntax, for faster development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%ifnarch i686
%R_check
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
