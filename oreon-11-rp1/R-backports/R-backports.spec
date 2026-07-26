%global source0_hash 0d3ed9db8f1505e88967f48d669b2a257e0c6b7e6320ea64b946c1bd40897ca2

Name:           R-backports
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Reimplementations of Functions Introduced Since R-3.0.0

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Functions introduced or changed since R v3.0.0 are re-implemented in this
package. The backports are conditionally exported in order to let R resolve
the function name to either the implemented backport, or the respective
base version, if available. Package developers can make use of new
functions or arguments by selectively importing specific backports to
support older installations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f backports/tests/test_dotlibPaths.R # wrong conditional

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
