%global source0_hash cfccabec368df2e2489175d5261329c6b1d7e18606fa5eb251a4819848e28dbf
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/cornelk/hashmap
Version:                1.0.8
%gometa
%global common_description %{expand:
A Golang lock-free thread-safe HashMap optimized for fastest read access.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Golang lock-free thread-safe HashMap optimized for fastest read access
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/hashmap-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/dchest/siphash)
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
