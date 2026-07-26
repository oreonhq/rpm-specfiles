%global source0_hash c20bc9259399bfbee21cd46f21c4ce6d8ef078449063febba093e852fea1dca5

Name:           R-whoami
Version:        %R_rpm_version 1.3.0
Release:        %autorelease
Summary:        Username, Full Name, Email Address, 'GitHub' Username of the Current User

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Look up the username and full name of the current user, the current user's
email address and 'GitHub' username, using various sources of system and
configuration information.

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
