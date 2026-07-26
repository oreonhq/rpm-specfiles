%global source0_hash c71874a6c116169e18bf12f023fdb79d63e92177aa7ae3858b30b60be5bc6030

Name:           R-RCurl
Version:        %R_rpm_version 1.98-1.17
Release:        %autorelease
Summary:        General network (HTTP/FTP) client interface for R

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  libcurl-devel

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

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
