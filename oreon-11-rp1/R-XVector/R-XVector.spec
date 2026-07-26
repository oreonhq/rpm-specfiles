%global source0_hash c963d04bd4c5c0387c401158408e02a08f1e9051124cae4154045c903c8be390

Name:           R-XVector
Version:        %R_rpm_version 0.50.0
Release:        %autorelease
Summary:        Representation and manipulation of external sequences

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.50.0

%description
Memory efficient S4 classes for storing sequences "externally" (behind an R
external pointer, or on disk).

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
