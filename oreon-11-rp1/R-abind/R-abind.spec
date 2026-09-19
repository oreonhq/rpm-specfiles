%global source0_hash 264a051b523ceae1795a0879e7768949ea55c586ac8db0adf1f5ebeddd2623e1

Name:           R-abind
Version:        %R_rpm_version 1.4-8
Release:        %autorelease
Summary:        Combine multi-dimensional arrays

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Combine multi-dimensional arrays. This is a generalization of cbind and rbind. 
Takes a sequence of vectors, matrices, or arrays and produces a single array 
of the same or higher dimension.

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
