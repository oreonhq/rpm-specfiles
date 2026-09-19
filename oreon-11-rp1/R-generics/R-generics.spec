%global source0_hash bbe95a097792d38fc3b7e677738af1b95b66ea5e5017e33b8beac6a6088d0801

Name:           R-generics
Version:        %R_rpm_version 0.1.4
Release:        %autorelease
Summary:        Common S3 Generics not Provided by Base R Methods Related to Model Fitting

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
In order to reduce potential package dependencies and conflicts, generics
provides a number of commonly used S3 generics.

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
