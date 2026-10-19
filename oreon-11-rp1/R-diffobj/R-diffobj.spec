%global source0_hash b316d9c37177b19ce7f39ba32872d09ab600909709fd313c1e39398a4ae51287
Name:           R-diffobj
Version:        %R_rpm_version 0.3.6
Release:        1%{?dist}
Summary:        Diffs for R Objects
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=diffobj&version=%{version}#/diffobj_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Generate a colorized diff of two R objects for an intuitive visualization
of their differences.

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
