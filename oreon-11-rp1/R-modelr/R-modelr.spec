%global source0_hash 94ebd506e9ccf3bf25318be6a182f8f89c3669a77b41864a0b9dbcc1d4337bd3

Name:           R-modelr
Version:        %R_rpm_version 0.1.11
Release:        %autorelease
Summary:        Modelling Functions that Work with the Pipe

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functions for modelling that help you seamlessly integrate modelling into a
pipeline of data manipulation and visualisation.

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
