%global source0_hash 32f7cd5dc0c182c4e5b86afe9e39bd6e9c1348f60de9c8511ff84ac1fcc295d8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/otiai10/copy
Version:                1.14.1
%gometa
%global common_description %{expand:
Go copy directory recursively.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go copy directory recursively
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/copy-%{version}.tar.gz
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
