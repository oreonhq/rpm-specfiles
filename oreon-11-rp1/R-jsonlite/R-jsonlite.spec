%global source0_hash 75eb910c82b350ec33f094779da0f87bff154c232e4ae39c9896a9b89f3ac82d

Name:           R-jsonlite
Version:        %R_rpm_version 2.0.0
Release:        %autorelease
Summary:        A Simple and Robust JSON Parser and Generator for R

License:        MIT and ISC
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

# https://github.com/jeroen/jsonlite/issues/201
Provides:       bundled(yajl) = 2.1.1

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

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
