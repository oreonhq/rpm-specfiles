%global source0_hash a02b90a8a6c49a499d972cebc5a15ab44e729b232d00516cb168414701e1c650

Name:           R-sessioninfo
Version:        %R_rpm_version 1.2.3
Release:        %autorelease
Summary:        R Session Information

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Query and print information about the current R session. It is similar to
'utils::sessionInfo()', but includes more information about packages, and where
they were installed from.

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
