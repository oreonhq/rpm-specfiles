%global source0_hash 8ea8d881137662de3172fabeb656cdb4303e67d40619fae7c5c66228b0e294e5

Name:           R-lmodel2
Version:        %R_rpm_version 1.7-4
Release:        %autorelease
Summary:        Model II Regression

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Computes model II simple linear regression using ordinary least squares
(OLS), major axis (MA), standard major axis (SMA), and ranged major axis

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
