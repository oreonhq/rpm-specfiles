%global source0_hash 751d86bfc628ac94df05749de3ecf09cb63310ada3d384f50b6a30f0f161bd42
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/stretchr/objx
Version:                0.5.0
%gometa
%global common_description %{expand:
Objx provides the objx.Map type, which is a map[string]interface{} that exposes
a powerful Get method (among others) that allows you to easily and quickly get
access to data within the map, without having to worry too much about type
assertions, missing data, default values etc.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package for dealing with maps, slices, JSON and other data
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/objx-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
