%global source0_hash 2dcd0ec453f5ec4d96f69b0c472569d57d3c5f9956a82a48492ee02f12071137

Name:           R-filelock
Version:        %R_rpm_version 1.0.3
Release:        %autorelease
Summary:        Portable File Locking

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Place an exclusive or shared lock on a file. It uses 'LockFile' on Windows and
'fcntl' locks on Unix-like systems.

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
