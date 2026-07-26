%global source0_hash fb511779777f69d2e1729e7de0fad6de86ab30a28738dff0524dffeb31f3eba4

Name:           R-nanotime
Version:        %R_rpm_version 0.3.12
Release:        %autorelease
Summary:        Nanosecond-Resolution Time Support for R

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.3.12

%description
Full 64-bit resolution date and time functionality with nanosecond granularity
is provided, with easy transition to and from the standard 'POSIXct' type.
Three additional classes offer interval, period and duration functionality for
nanosecond-resolution timestamps.

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
