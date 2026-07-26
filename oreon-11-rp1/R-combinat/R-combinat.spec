%global source0_hash fc6dae73266e69891b59e6e11661247fe44c9a3f56277c8bbe0c10bb79382f67

Name:           R-combinat
Version:        %R_rpm_version 0.0-8
Release:        %autorelease
Summary:        R routines for combinatorics

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R routines for combinatorics

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
[ -f combinat/NAMESPACE ] || echo 'exportPattern("^[^\\.]")' > combinat/NAMESPACE

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
