%global source0_hash c71874a6c116169e18bf12f023fdb79d63e92177aa7ae3858b30b60be5bc6030
Name:           R-RCurl
Version:        %R_rpm_version 1.98-1.17
Release:        1%{?dist}
Summary:        General network (HTTP/FTP) client interface for R
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=RCurl&version=1.98-1.17#/RCurl_1.98-1.17.tar.gz
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libcurl-devel
# /oreon:deps
%description
The package allows one to compose general HTTP requests and provides convenient 
functions to fetch URIs, get & post forms, etc. and process the results 
returned by the Web server. This provides a great deal of control over the 
HTTP/FTP/... connection and the form of the request while providing a 
higher-level interface than is available just using R socket connections. 
Additionally, the underlying implementation is robust and extensive, supporting 
FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS, telnet, dict, ldap, and also 
supports cookies, redirects, authentication, etc.

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
