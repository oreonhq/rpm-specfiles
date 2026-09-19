%global source0_hash 3854b130b1d6a45f39afc158033fecf478d2ab94ba70775935fdfee35f488239

Name:           R-rhub
Version:        %R_rpm_version 2.0.1
Release:        %autorelease
Summary:        Connect to 'R-hub'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Run 'R CMD check' on any of the 'R-hub' (<https://builder.r-hub.io/>)
architectures, from the command line. The current architectures include
Windows, macOS, Solaris and various Linux distributions.

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
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
