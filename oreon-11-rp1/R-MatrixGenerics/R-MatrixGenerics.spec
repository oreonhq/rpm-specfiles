%global source0_hash b53dcb3c9ac7e1e6e0a297f90c1603ab2a39e052718bd70d76aeed6f6110557a

Name:           R-MatrixGenerics
Version:        %R_rpm_version 1.22.0
Release:        %autorelease
Summary:        S4 Generic Summary Statistic Functions that Operate on Matrix-Like Objects

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
S4 generic functions modeled after the 'matrixStats' API for alternative matrix
implementations. Packages with alternative matrix implementation can depend on
this package and implement the generic functions that are defined here for a
useful set of row and column summary statistics. Other package developers can
import this package and handle a different matrix implementations without
worrying about incompatibilities.

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
