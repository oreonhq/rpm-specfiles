%global source0_hash 3a958424e908ec7e29a224c1754218970225ea019e959ee688d64215bebc64d4

Name:           R-mockery
Version:        %R_rpm_version 0.4.5
Release:        %autorelease
Summary:        Mocking Library for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
The two main functionalities of this package are creating mock objects
(functions) and selectively intercepting calls to a given function that
originate in some other function. It can be used with any testing framework
available for R. Mock objects can be injected with either this package's own
stub() function or a similar with_mock() facility present in the testthat
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
