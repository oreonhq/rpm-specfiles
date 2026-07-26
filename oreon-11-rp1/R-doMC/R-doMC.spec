%global source0_hash b2186f851448251ae6af5d14b9e3e7f9221f90887e5f8de6a68c91caf16619a3

Name:           R-doMC
Version:        %R_rpm_version 1.3.8
Release:        %autorelease
Summary:        Foreach Parallel Adaptor for 'parallel'

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a parallel backend for the %%dopar%% function using the multicore
functionality of the parallel package.

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
