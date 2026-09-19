%global source0_hash f212a6d812d27b7d766d2b017ae0828f55b460e923161648ec46671c3477346f

Name:           R-bindr
Version:        %R_rpm_version 0.1.3
Release:        %autorelease
Summary:        Parametrized Active Bindings

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a simple interface for creating active bindings where the bound
function accepts additional arguments.

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
