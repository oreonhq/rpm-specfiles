%global source0_hash 32a43f073aeb5c1d31c804014b95c2cb644bb4132119fcea313838b7ea4eb792
Name:           R-fansi
Version:        %R_rpm_version 1.0.7
Release:        1%{?dist}
Summary:        ANSI Control Sequence Aware String Functions
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=fansi&version=%{version}#/fansi_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Counterparts to R string manipulation functions that account for the
effects of ANSI text formatting control sequences.

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
