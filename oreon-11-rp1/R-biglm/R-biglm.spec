%global source0_hash 805d483dc58c041f1616267abeb39cecaaf7271a34e90668a5439383bf9a0d58

Name:           R-biglm
Version:        %R_rpm_version 0.9-3
Release:        %autorelease
Summary:        Bounded memory linear and generalized linear models

License:        GPL-1.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Regression for data too large to fit in memory.

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
