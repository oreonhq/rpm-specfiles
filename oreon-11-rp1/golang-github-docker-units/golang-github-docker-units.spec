%global source0_hash db0a1d3e4deaa52401423bf76cce0a5100cf2e51db3c33cf3c70b7953c7d6234
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docker/go-units
Version:                0.5.0
%gometa
%global common_description %{expand:
Go-units is a library to transform human friendly measurements into machine
friendly values.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parse and print size and time units in human-readable format
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-units-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
