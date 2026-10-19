%global source0_hash e9b4dc74406f6eb8af447f22f5dbaabed6a94301e91e50142501c22c89871770
Name:           R-parsedate
Version:        %R_rpm_version 1.3.2
Release:        1%{?dist}
Summary:        Recognize and Parse Dates in Various Formats
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=parsedate&version=%{version}#/parsedate_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Parse dates automatically, without the need of specifying a format.  Currently
it includes the git date parser. It can also recognize and parse all ISO 8601
formats.

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
