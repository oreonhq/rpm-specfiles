%global source0_hash 4181f7334e032ae0775c5dec49d6137eb25d5430ca3792d321793307b3dda38f

Name:           R-brew
Version:        %R_rpm_version 1.0-10
Release:        %autorelease
Summary:        Templating Framework for Report Generation

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
brew implements a templating framework for mixing text and R code for
report generation. brew template syntax is similar to PHP, Ruby's erb
module, Java Server Pages, and Python's psp module.

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
