%global source0_hash 4589f8b72291329e70b7f3a8c20f2feb4e7764eebad2e6976bc9a3eee7686ce9
Name:           R-utf8
Version:        %R_rpm_version 1.2.6
Release:        1%{?dist}
Summary:        Unicode Text Processing
License:        Apache-2.0
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=utf8&version=%{version}#/utf8_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Process and print 'UTF-8' encoded international text (Unicode). Input,
validate, normalize, encode, format, and display.

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
