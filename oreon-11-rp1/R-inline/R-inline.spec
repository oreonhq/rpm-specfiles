%global source0_hash 7ef9410a933a47f6a346bc8c0e55b62931379b464b92696aee9865ec6378bc98

Name:           R-inline
Version:        %R_rpm_version 0.3.21
Release:        %autorelease
Summary:	    Functions to Inline C, C++, Fortran Function Calls from R

License:	    LGPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functionality to dynamically define R functions and S4 methods with
'inlined' C, C++ or Fortran code supporting the .C and .Call calling
conventions.

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
