%global source0_hash 2320ebc9ef3b1a32a1e63f94a6ce2c1c34d66782221a6531e786804f681abc66

Name:           R-rappdirs
Version:        %R_rpm_version 0.3.4
Release:        %autorelease
Summary:        Application Directories: Determine Where to Save Data, Caches, and Logs

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
An easy way to determine which directories on the users computer you should
use to save data, caches and logs. A port of Python's 'Appdirs'
(<https://github.com/ActiveState/appdirs>) to R.

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
