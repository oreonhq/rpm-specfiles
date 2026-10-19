%global source0_hash d66e25cdf5b4b6fc1cbf7b067213e5d891ce416810099c38052fe374c78af24d
%bcond check 0
%global debug_package %{nil}
%global goipath         go4.org
%global forgeurl        https://github.com/go4org/go4
%global commit          214862532bf518db360e7ecc2b8a94b66a10c176
%gometa
%global common_description %{expand:
Go4 hosts the go4.org packages.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Collection of packages for Go programmers
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/go4-%{commit}.tar.gz
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

rm -rfv sort/example_multi_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
