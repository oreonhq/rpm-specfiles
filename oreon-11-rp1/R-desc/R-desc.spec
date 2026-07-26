%global source0_hash 54468da73dd78fc9e7c565c41cfe3331802c2134b2e61a9ad197215317092f26

Name:           R-desc
Version:        %R_rpm_version 1.4.3
Release:        %autorelease
Summary:        Manipulate DESCRIPTION Files

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Tools to read, write, create, and manipulate DESCRIPTION files. It is
intended for packages that create or manipulate other packages.

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
