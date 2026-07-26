%global source0_hash cef3075a0930e1408c764e4da56bbadd4f7d14315809df8f38dd51f80ccc677b

Name:           R-iterators
Version:        %R_rpm_version 1.0.14
Release:        %autorelease
Summary:        Provides Iterator Construct

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for iterators, which allow a programmer to traverse through all the
elements of a vector, list, or other collection of data.

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
