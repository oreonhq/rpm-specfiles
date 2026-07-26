%global source0_hash 5a36fabb6d62ba2533d3fc4cececd07891942cfb76fe689ec0d550d08762f61c

Name:           R-png
Version:        %R_rpm_version 0.1-8
Release:        %autorelease
Summary:        Read and write PNG images

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  libpng-devel

%description
This package provides an easy and simple way to read, write and display
bitmap images stored in the PNG format. It can read and write both files
and in-memory raw vectors.

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
