%global source0_hash 75eb910c82b350ec33f094779da0f87bff154c232e4ae39c9896a9b89f3ac82d
Name:           R-jsonlite
Version:        %R_rpm_version 2.0.0
Release:        1%{?dist}
Summary:        A Simple and Robust JSON Parser and Generator for R
License:        MIT and ISC
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=jsonlite&version=%{version}#/jsonlite_%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides:       bundled(yajl) = 2.1.1
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A reasonably fast JSON parser and generator, optimized for statistical data and
the web. Offers simple, flexible tools for working with JSON in R, and is
particularly powerful for building pipelines and interacting with a web API.
The implementation is based on the mapping described in the vignette (Ooms,
2014). In addition to converting JSON data from/to R objects, 'jsonlite'
contains functions to stream, validate, and prettify JSON data.  The unit tests
included with the package verify that all edge cases are encoded and decoded
consistently for use with dynamic data in systems and applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
