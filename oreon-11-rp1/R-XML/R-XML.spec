%global source0_hash f5fbb829a763c81b35571227cbeba346dee9713ff9c6c0c1a73f73256d51707c
Name:           R-XML
Version:        %R_rpm_version 3.99-0.20
Release:        1%{?dist}
Summary:        Tools for Parsing and Generating XML Within R and S-Plus
License:        BSD-3-Clause
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=XML&version=3.99-0.20#/XML_3.99-0.20.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  libxml2-devel
# /oreon:deps
%description
Many approaches for both reading and creating XML (and HTML) documents
(including DTDs), both local and accessible via HTTP or FTP.  Also offers
access to an XPath "interpreter".

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
