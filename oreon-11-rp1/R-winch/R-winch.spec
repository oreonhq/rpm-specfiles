%global source0_hash 13e8f71a5cb8d1984e45fb53970c61511f4b3cba6041817602d3c83ef8d8dbba

Name:           R-winch
Version:        %R_rpm_version 0.1.2
Release:        %autorelease
Summary:        Portable Native and Joint Stack Traces

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libunwind)

Provides:       bundled(libbacktrace) = 1.0

%description
Obtain the native stack trace and fuse it with R's stack trace for easier
debugging of R packages with native code.

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
