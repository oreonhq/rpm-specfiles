%global source0_hash 867c8ffc592e672ca8f10e10a6a1860d716b03d03d915484bf7b73adbe6ae18d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/d2g/hardwareaddr
%global commit          e7d9fbe030e4b7b08e3bdd128e2e81809e4389fd
%gometa
%global common_description %{expand:
Generate Hardware Addresses.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Generate Hardware Addresses
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/hardwareaddr-%{commit}.tar.gz
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
