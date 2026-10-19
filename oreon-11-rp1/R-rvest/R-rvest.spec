%global source0_hash 1e7c34a0b4467887195b1cd66388919989e82ca096d08df283c675d87e53bc00
Name:           R-rvest
Version:        %R_rpm_version 1.0.5
Release:        1%{?dist}
Summary:        Easily Harvest (Scrape) Web Pages
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rvest&version=%{version}#/rvest_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Wrappers around the 'xml2' and 'httr' packages to make it easy to download,
then manipulate, HTML and XML.

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
