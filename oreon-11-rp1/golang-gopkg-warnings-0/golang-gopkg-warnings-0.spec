%global source0_hash 4712c4ceae321433d8c1d9ebc6afd154d7932c849129ded48b1c4a51c21275e8
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/warnings.v0
%global forgeurl        https://github.com/go-warnings/warnings
Version:                0.1.2
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-gopkg-warnings-0-devel < 0.1.2-5
}
%global common_description %{expand:
A recurring programming pattern pattern is to allow interrupting the flow on any
received error. But what if there are errors that should be noted but still not
fatal, for which the flow should not be interrupted? Implementing such logic at
each if statement would make the code complex and the flow much harder to
follow.
Package Warnings provides the Collector type and a clean and simple pattern for
achieving such logic. The Collector takes care of deciding when to break the
flow and when to continue, collecting any non-fatal errors (warnings) along the
way. The only requirement is that fatal and non-fatal errors can be
distinguished programmatically.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements error handling with non-fatal errors (warnings)
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/warnings-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
