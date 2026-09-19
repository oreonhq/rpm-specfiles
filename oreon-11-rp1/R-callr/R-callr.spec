%global source0_hash e4bce367e869e42eaeea05566d2033d8cee2103179b11cd9a401440b58a351f8

Name:           R-callr
Version:        %R_rpm_version 3.7.6
Release:        %autorelease
Summary:        Call R from R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
It is sometimes useful to perform a computation in a separate R process,
without affecting the current R process at all. This packages does exactly
that.

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
