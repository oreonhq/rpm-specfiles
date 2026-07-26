%global source0_hash 7b191a54019c8c52d6c2211c14878c95564154ec4865f57007953742868cd813

Name:           R-ini
Version:        %R_rpm_version 0.3.1
Release:        %autorelease
Summary:        Read and Write '.ini' Files

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Parse simple '.ini' configuration files to an structured list. Users can
manipulate this resulting list with lapply() functions. This same structured
list can be used to write back to file after modifications.

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
