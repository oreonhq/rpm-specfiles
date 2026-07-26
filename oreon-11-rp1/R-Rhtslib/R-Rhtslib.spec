%global source0_hash 8b5fc0dfba39efb7371b5b0f930445047c7e06238d07c2293a50317612da6692

Name:           R-Rhtslib
Version:        %R_rpm_version 3.6.0
Release:        %autorelease
Summary:        HTSlib high-throughput sequencing library as an R package

License:        LGPL-2.0-or-later
URL:            %{bioc_url}
Source:         %{bioc_source}
Patch:          R-Rhtslib-buildroot-fix.patch

BuildRequires:  R-devel
BuildRequires:  libcurl-devel
Obsoletes:      %{name}-devel <= 3.6.0

# Do not check for Provides in internal shared libraries
%global __provides_exclude_from ^%{_R_libdir}/Rhtslib/usrlib/.*\\.so.*$

%description
This package provides version 1.15.1 of the 'HTSlib' C library for
high-throughput sequence analysis. The package is primarily useful to
developers of other R packages who wish to make use of HTSlib. Motivation and
instructions for use of this package are in the vignette,
vignette(package="Rhtslib", "Rhtslib").

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

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
