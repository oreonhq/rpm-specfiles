%global source0_hash 5b1633be7bc0ea796e2df5b24b2aec937a17359f2d86207359aa553328824d6b
Name:           R-curl
Version:        %R_rpm_version 7.0.0
Release:        1%{?dist}
Summary:        A Modern and Flexible Web Client for R
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=curl&version=%{version}#/curl_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(libcurl)
# /oreon:deps
%description
The curl() and curl_download() functions provide highly configurable drop-in
replacements for base url() and download.file() with better performance,
support for encryption (https, ftps), gzip compression, authentication, and
other 'libcurl' goodies. The core of the package implements a framework for
performing fully customized requests where data can be processed either in
memory, on disk, or streaming via the callback or connection interfaces. Some
knowledge of 'libcurl' is recommended; for a more-user-friendly web client see
the 'httr' package which builds on this package with http specific tools and
logic.

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
