%global source0_hash a10578e9ad8a581bd8fe0d8a8370051f3cdcf12c7d282f3af2a18dacda566081

Name:           R-dichromat
Version:        %R_rpm_version 2.0-0.1
Release:        %autorelease
Summary:        Color Schemes for Dichromats

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Collapse red-green or green-blue distinctions to simulate the effects of
different types of color-blindness.

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
