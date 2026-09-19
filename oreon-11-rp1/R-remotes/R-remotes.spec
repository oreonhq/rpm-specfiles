%global source0_hash 4d663f1426cd88d42f4070f23d969305c575e0499ed1397be6607b0770d2850c

Name:           R-remotes
Version:        %R_rpm_version 2.5.0
Release:        %autorelease
Summary:        R Package Installation from Remote Repositories

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Download and install R packages stored in GitHub, GitLab, Bitbucket,
Bioconductor, or plain subversion or git repositories. This package provides
the 'install_*' functions in devtools. Indeed most of the code was copied over
from devtools.

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
