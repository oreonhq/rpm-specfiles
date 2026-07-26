%global source0_hash 7f6b97dbb7cd762f76f7319b3e2b38f3d4206fe625d363da1b5f96c928da92bb

Name:           R-zeallot
Version:        %R_rpm_version 0.2.0
Release:        %autorelease
Summary:        Multiple, Unpacking, and Destructuring Assignment

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a %<-% operator to perform multiple, unpacking, and destructuring
assignment in R. The operator unpacks the right-hand side of an assignment into
multiple values and assigns these values to variables on the left-hand side of
the assignment.

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
