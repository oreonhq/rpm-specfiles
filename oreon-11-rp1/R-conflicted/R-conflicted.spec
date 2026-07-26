%global source0_hash c99b86bb52da3e7d1f4d96d70c77304d0434db5bd906edd8d743e89ac9223088

Name:           R-conflicted
Version:        %R_rpm_version 1.2.0
Release:        %autorelease
Summary:        An Alternative Conflict Resolution Strategy

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R's default conflict management system gives the most recently loaded
package precedence. This can make it hard to detect conflicts, particularly
when they arise because a package update creates ambiguity that did not
previously exist. 'conflicted' takes a different approach, making every
conflict an error and forcing you to choose which function to use.

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
