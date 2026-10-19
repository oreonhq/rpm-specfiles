%global source0_hash b752c97a44f5dbfc01a156c7a8c3de76d461af6686f61f7a01e13162be19c511
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/go-zookeeper/zk
Version:                1.0.2
%gometa
%global common_description %{expand:
Native ZooKeeper client for Go.}
%global golicenses      LICENSE
%global godocs          _examples CONTRIBUTION.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Native ZooKeeper client for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/zk-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
