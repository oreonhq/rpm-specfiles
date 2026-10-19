%global source0_hash 81106cbac93000812c194b4a2069dd32913ec18819b1e99e8436595ce4939413
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mitchellh/mapstructure
Version:                1.5.0
%gometa -L
%global common_description %{expand:
Mapstructure is a Go library for decoding generic map values to structures and
vice versa, while providing helpful error handling.
This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data until
you read a part of it. You can therefore read a map[string]interface{} and use
this library to decode it into the proper underlying native Go structure.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-mitchellh-mapstructure
Release:        1%{?dist}
Summary:        Go library for decoding generic map values into native go structures
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mapstructure-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
