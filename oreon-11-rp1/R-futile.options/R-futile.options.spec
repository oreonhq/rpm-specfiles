%global source0_hash 7a9cc974e09598077b242a1069f7fbf4fa7f85ffe25067f6c4c32314ef532570

Name:           R-futile.options
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Futile options management

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A scoped options management framework.

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
