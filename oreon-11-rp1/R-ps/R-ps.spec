%global source0_hash 6f093c0beb87684afe098b71e16593366210d5d38992a7c3740ca1075da4df7d

Name:           R-ps
Version:        %R_rpm_version 1.9.1
Release:        %autorelease
Summary:        List, Query, Manipulate System Processes

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
List, query and manipulate all system processes, on 'Windows', 'Linux' and
'macOS'.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
