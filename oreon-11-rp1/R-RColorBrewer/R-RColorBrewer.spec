%global source0_hash 4f42f5423c45688b39f492c7892d93f37b4541831c8ffb140364d2bd89031ac0

Name:           R-RColorBrewer
Version:        %R_rpm_version 1.1-3
Release:        %autorelease
Summary:        ColorBrewer Palettes

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides color schemes for maps (and other graphics) designed by Cynthia
Brewer as described at http://colorbrewer2.org

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
