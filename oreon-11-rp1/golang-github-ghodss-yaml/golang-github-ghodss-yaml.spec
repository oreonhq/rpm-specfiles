%global source0_hash 8a76b47cd171944612aae1cfa08bbb971b63fec16794c839252808392097de44
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/ghodss/yaml
Version:                1.0.0
%gometa
%global common_description %{expand:
In short, this library first converts YAML to JSON using go-yaml and then uses
json.Marshal and json.Unmarshal to convert to or from the struct. This means
that it effectively reuses the JSON struct tags as well as the custom JSON
methods MarshalJSON and UnmarshalJSON unlike go-yaml.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        YAML marshaling and unmarshaling support for Go
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/yaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/yaml.v2)
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
