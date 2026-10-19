%global source0_hash 96812bdb7a0dd99690d84e4b0a3def91389e4290f53f01919ef28a50554e31d1
Name:           R-sourcetools
Version:        %R_rpm_version 0.1.7-1
Release:        1%{?dist}
Summary:        Tools for Reading, Tokenizing and Parsing R Code
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sourcetools&version=0.1.7-1#/sourcetools_0.1.7-1.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel <= 0.1.7
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Tools for the reading and tokenization of R code. The 'sourcetools' package
provides both an R and C++ interface for the tokenization of R code, and
helpers for interacting with the tokenized representation of R code.

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
