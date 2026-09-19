%global source0_hash 0e63ba2e1f624005fe25c67cdd403636a912e063d682eca07f2f1d65e9870d29

Name:           R-plogr
Version:        %R_rpm_version 0.2.0
Release:        %autorelease
Summary:        C++ Logging Library for R
Summary:        Devel files for R-plogr

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.2.0

%description
A simple header-only logging library for C++. Add 'LinkingTo: plogr' to
'DESCRIPTION', and '#include <plogr.h>' in your C++ modules to use it.

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
