%global source0_hash 55034575c854ed657e6701da278c0fdea251479624d06a963b2e58461a5f0f48
Name:           R-rjson
Version:        %R_rpm_version 0.2.23
Release:        1%{?dist}
Summary:        JSON for R
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rjson&version=%{version}#/rjson_%{version}.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Converts R object into JSON objects and vice-versa.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

chmod +x rjson/inst/rpc_server/server.r
chmod +x rjson/inst/rpc_server/start_server
# come on osx developer
sed -i 's|/usr/bin/r|/usr/bin/Rscript|g' rjson/inst/rpc_server/server.r

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
