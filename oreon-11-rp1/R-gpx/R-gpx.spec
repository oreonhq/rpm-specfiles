%global source0_hash b1582856c477fed3adfd18510209b79bfbb70e99df5b4e2848a6c6bc6c1d2b75

Name:           R-gpx
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Process GPX Files into R Data Structures

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Process open standard GPX files into data.frames
for further use and analysis in R.

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
