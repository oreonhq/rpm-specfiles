%global source0_hash 5abec0e8c27865ef0880f1d19c9f9ca7cc0fd24eadaa72bcd270c3fb4075fd1c

Name:           R-xtable
Version:        %R_rpm_version 1.8-4
Release:        %autorelease
Summary:        Export Tables to LaTeX or HTML

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Coerce data to LaTeX and HTML tables.

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
