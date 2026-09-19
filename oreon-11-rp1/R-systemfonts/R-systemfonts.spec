%global source0_hash 4392cbf7f97d335b61f7a70257faead2d45a3beeb76249d75a41e9ed82e4456d

Name:           R-systemfonts
Version:        %R_rpm_version 1.3.1
Release:        %autorelease
Summary:        System Native Font Finding

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
Obsoletes:      %{name}-devel <= 1.3.1

%description
Provides system native access to the font catalogue. As font handling
varies between systems it is difficult to correctly locate installed fonts
across different operating systems. The 'systemfonts' package provides
bindings to the native libraries on Windows, macOS and Linux for finding
font files that can then be used further by e.g. graphic devices. The main
use is intended to be from compiled code but 'systemfonts' also provides
access from R.

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
