%global source0_hash 766034ab5e9728609bd240c9954d23ca0cdb881a98a31b9d3e1c8767c7b7cbb0
Name:           R-xmlparsedata
Version:        %R_rpm_version 1.0.5
Release:        1%{?dist}
Summary:        Parse Data of 'R' Code as an 'XML' Tree
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=xmlparsedata&version=%{version}#/xmlparsedata_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Convert the output of 'utils::getParseData()' to an 'XML' tree, that one
can search via 'XPath', and easier to manipulate in general.

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
