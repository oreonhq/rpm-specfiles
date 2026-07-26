%global source0_hash 4472052371147cfbf91d223eb15f3b030d236de9b4bba6b58a205c368d53884d

Name:           R-preprocessCore
Version:        %R_rpm_version 1.72.0
Release:        %autorelease
Summary:        A collection of pre-processing functions

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.72.0

%description
A library of core preprocessing routines

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
