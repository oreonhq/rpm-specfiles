%global source0_hash ed87cfa478f9e4c398288963cf7b0e1a66ba08f54d909b261a4a6c35944f50ab
Name:           R-xml2
Version:        %R_rpm_version 1.5.2
Release:        1%{?dist}
Summary:        Parse XML
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=xml2&version=%{version}#/xml2_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 1.5.1
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libxml2-devel
# /oreon:deps
%description
Work with XML files using a simple, consistent interface. Built on top of
the 'libxml2' C library.

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
