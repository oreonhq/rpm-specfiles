%global source0_hash 9649eef00381d3bde3d96928782e8792d78b9be0a2968e832728b54f5886fdbd

Name:           R-rstudioapi
Version:        %R_rpm_version 0.18.0
Release:        %autorelease
Summary:        Safely Access the RStudio API

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Access the RStudio API (if available) and provide informative error
messages when it's not.

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
