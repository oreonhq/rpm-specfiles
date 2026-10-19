%global source0_hash 7a9cc974e09598077b242a1069f7fbf4fa7f85ffe25067f6c4c32314ef532570
Name:           R-futile.options
Version:        %R_rpm_version 1.0.1
Release:        1%{?dist}
Summary:        Futile options management
License:        LGPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=futile.options&version=%{version}#/futile.options_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A scoped options management framework.

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
