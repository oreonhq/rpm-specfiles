%global source0_hash 81bec7a85a866f1c4c2f361bba718bc2d6ba7dc7e6d662787a44c4e89c0d4b3d
%bcond check 0
%global goipath         github.com/nilslice/protolock
Version:                0.17.0
%gometa -f
%global common_description %{expand:
Protocol Buffer companion tool. Track your .proto files and prevent changes to
messages and services which impact API compatibility.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Protocol Buffer companion tool
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/protolock-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       protolock
Summary:        Protocol Buffer companion tool
BuildArch:      noarch

%description -n protolock
Protocol Buffer companion tool

%description %{common_description}

%package -n     protolock
Summary:        Protocol Buffer companion tool
%description -n protolock %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%if 0%{?el9}
export GOPATH="%{gobuilddir}:%{gopath}"
export GO111MODULE=off
%endif
%gobuild -o %{gobuilddir}/bin/protolock %{goipath}/cmd/protolock
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles protolock usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

rm order_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n protolock -f %{oreon_filedir}/protolock.list

%changelog

%autochangelog
