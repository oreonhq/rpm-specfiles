%global source0_hash 776d4544a9cff766fdbd3f447c29fde78fb1f3f6798fa5bc8e9263da0742ce26

Name:           R-DynDoc
Version:        %R_rpm_version 1.88.0
Release:        %autorelease
Summary:        Functions for dynamic documents

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A set of functions to create and interact with dynamic documents and
vignettes.

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
