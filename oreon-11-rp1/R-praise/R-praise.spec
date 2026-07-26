%global source0_hash 5c035e74fd05dfa59b03afe0d5f4c53fbf34144e175e90c53d09c6baedf5debd

Name:           R-praise
Version:        %R_rpm_version 1.0.0
Release:        %autorelease
Summary:        Praise Users

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Build friendly R packages that praise their users if they have done something
good, or they just need it to feel better.

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
