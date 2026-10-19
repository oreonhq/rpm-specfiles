%global source0_hash 3d9cdb189ee932f326cccfd580ebd1202cb12cf6e37154be13f000fb5cec3d23
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cucumber/messages-go
Version:                20.0.0
%gometa
%global goaltipaths     github.com/cucumber/messages-go/v17
%global common_description %{expand:
Cucumber Messages for Go (Protocol Buffers).}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cucumber Messages for Go (Protocol Buffers)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/messages-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gofrs/uuid)
BuildRequires:  golang(github.com/gogo/protobuf/io)
BuildRequires:  golang(github.com/gogo/protobuf/jsonpb)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
