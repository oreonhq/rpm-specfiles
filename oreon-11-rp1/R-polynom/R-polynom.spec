%global source0_hash bc1edb7bb16c8b299103f80a52ab8c5fc200cd07a9056578c1f672e9f5019278

Name:           R-polynom
Version:        %R_rpm_version 1.4-1
Release:        %autorelease
Summary:        A Class for Univariate Polynomial Manipulations

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of functions to implement a class for univariate polynomial
manipulations.

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
