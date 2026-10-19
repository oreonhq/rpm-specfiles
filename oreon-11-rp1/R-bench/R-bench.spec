%global source0_hash b822f5b7648deecc6b516dcca4e932ce92e65eb166b997b04355218aceb1d083
Name:           R-bench
Version:        %R_rpm_version 1.1.4
Release:        1%{?dist}
Summary:        High Precision Timing of R Expressions
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=bench&version=%{version}#/bench_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Tools to accurately benchmark and analyze execution times for R expressions.

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
