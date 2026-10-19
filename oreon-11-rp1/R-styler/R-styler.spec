%global source0_hash f08760782b2ead047dd8f166a7cd5e01ace8d713087712bf61d193f610fbfe18
Name:           R-styler
Version:        %R_rpm_version 1.11.0
Release:        1%{?dist}
Summary:        Non-Invasive Pretty Printing of R Code
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=styler&version=%{version}#/styler_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Pretty-prints R code without changing the user's formatting intent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
