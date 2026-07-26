%global source0_hash 496bedbe2e52d06db22a4d659b8e7dd9ad0f1d1f95ead459ec02d05d0ac2b3d6

Name:           R-futile.logger
Version:        %R_rpm_version 1.4.9
Release:        %autorelease
Summary:        A logging utility for R

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a simple yet powerful logging utility. Based loosely on log4j, 
futile.logger takes advantage of R idioms to make logging a convenient and
easy to use replacement for cat and print statements.

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
