%global source0_hash 3c128942ba4158a49d8c03ed040f3e0687b13a49fff976d7b6f54a7bd6fbad25
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/h2non/parth
Version:                2.0.1
%gometa
%global common_description %{expand:
Package Parth provides path parsing for segment unmarshaling and slicing. In
other words, parth provides simple and flexible access to (URL) path parameters.
Along with string, all basic non-alias types are supported. An interface is
available for implementation by user-defined types. When handling an int, uint,
or float of any size, the first valid value within the specified segment will be
used.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Path parsing for segment unmarshaling and slicing
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/parth-%{version}.tar.gz
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
