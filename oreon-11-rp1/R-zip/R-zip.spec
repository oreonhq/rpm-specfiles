%global source0_hash d0450b24f8b7b937033ad748b5fad76d23e9464f3e8c0c57a256d64829249a52

Name:           R-zip
Version:        %R_rpm_version 2.3.3
Release:        %autorelease
Summary:        Cross-Platform 'zip' Compression

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Cross-Platform 'zip' Compression Library. A replacement for the 'zip'
function, that does not require any additional external tools on any
platform.

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
