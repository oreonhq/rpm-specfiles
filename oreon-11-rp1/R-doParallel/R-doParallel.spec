%global source0_hash b96a25ad105a654d70c7b4ca27290dc9967bc47f4668b2763927a886b178abd7

Name:           R-doParallel
Version:        %R_rpm_version 1.0.17
Release:        %autorelease
Summary:        Foreach Parallel Adaptor for the 'parallel' Package

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a parallel backend for the %%dopar%% function using the parallel
package.

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
