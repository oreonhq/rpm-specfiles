%global source0_hash 473989bbef45fd9cd68f68dc317b14c9f42de5cea4b55fd6ba9011f25e0517e9

Name:           R-rprojroot
Version:        %R_rpm_version 2.1.1
Release:        %autorelease
Summary:        Finding Files in Project Subdirectories

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Robust, reliable and flexible paths to files below a project root. The
'root' of a project is defined as a directory that matches a certain
criterion, e.g., it contains a certain regular file.

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
