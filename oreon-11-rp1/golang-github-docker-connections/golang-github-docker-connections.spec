%global source0_hash c6d34d93ce0c9dfebbce0c6ec947b7607a47983ba7d28ab3f1e8924da3da7e90
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docker/go-connections
Version:                0.8.1
%global commit          58542c764a1173ea3dac965d89146c931a2946f7
%gometa
%global common_description %{expand:
Go-connections provides common package to work with network connections.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Utility package to work with network connections
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-connections-%{commit}.tar.gz
Patch0:         0001-update-expired-Lets-Encrypt-CA-fixture.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
