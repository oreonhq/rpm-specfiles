%global source0_hash 8fa3bdafff38cc5997f9e7235c8f8359825ed8f9a0ec06c6fe75c9f798ed9fec

Name:           R-globals
Version:        %R_rpm_version 0.18.0
Release:        %autorelease
Summary:        Identify Global Objects in R Expressions

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Identifies global ("unknown" or "free") objects in R expressions by code
inspection using various strategies (ordered, liberal, or conservative). The
objective of this package is to make it as simple as possible to identify
global objects for the purpose of exporting them in parallel, distributed
compute environments.

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
%R_check

%files -f %{R_files}

%changelog
%autochangelog
