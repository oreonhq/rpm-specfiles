%global source0_hash af55c5885336d989368410256a57a0e917cf4b3a486d4592f0d0587767f23481

Name:           R-fortunes
Version:        %R_rpm_version 1.5-4
Release:        %autorelease
Summary:        R Fortunes

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of fortunes from the R community.

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
