%global source0_hash c92e5604e1e149e00f49fd236c6ab8cd09d96106eb14479f7839e6996bf95e4e

Name:           R-wesanderson
Version:        %R_rpm_version 0.3.7
Release:        %autorelease
Summary:        Wes Anderson Palette Generator

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Palettes generated mostly from 'Wes Anderson' movies.

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
