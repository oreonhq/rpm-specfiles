%global source0_hash f8d9e0df1350a834c169dc53ff75e5f630d0563802be51fbb60de283e2ea499c
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/godbus/dbus
Version:                5.2.2
%gometa
%global goaltipaths     github.com/godbus/dbus/v5
%global common_description %{expand:
Dbus is a simple library that implements native Go client bindings for the D-Bus
message bus system.}
%global golicenses      LICENSE
%global godocs          _examples CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Native Go bindings for D-Bus
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/dbus-%{version}.tar.gz
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
