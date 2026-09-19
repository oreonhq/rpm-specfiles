%global source0_hash e3b278b8c324a1aa2650141dd89d01253eea5c2555007422c797915689b29aec

Name:           R-xopen
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Open System Files, 'URLs', Anything

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
BuildRequires:  /usr/bin/xdg-open
Requires:       /usr/bin/xdg-open

%description
Cross platform solution to open files, directories or 'URLs' with their
associated programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Depend on system executable instead.
rm xopen/inst/xdg-open

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
