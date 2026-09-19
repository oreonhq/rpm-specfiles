%global source0_hash 56338d8753f9f68f262cf532fd8a6d0fe25a71a2ff0107f3ce378feb926bafe4

Name:           R-foreach
Version:        %R_rpm_version 1.5.2
Release:        %autorelease
Summary:        Provides Foreach Looping Construct

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for the foreach looping construct.  Foreach is an idiom that allows for
iterating over elements in a collection, without the use of an explicit loop
counter.  This package in particular is intended to be used for its return
value, rather than for its side effects.  In that sense, it is similar to the
standard lapply function, but doesn't require the evaluation of a function.
Using foreach without side effects also facilitates executing the loop in
parallel.

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
