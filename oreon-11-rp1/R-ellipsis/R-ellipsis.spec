%global source0_hash a90266e5eb59c7f419774d5c6d6bd5e09701a26c9218c5933c9bce6765aa1558
Name:           R-ellipsis
Version:        %R_rpm_version 0.3.2
Release:        1%{?dist}
Summary:        Tools for Working with ...
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ellipsis&version=%{version}#/ellipsis_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
The ellipsis is a powerful tool for extending functions. Unfortunately this
power comes at a cost: misspelled arguments will be silently ignored. The
ellipsis package provides a collection of functions to catch problems and alert
the user.

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
