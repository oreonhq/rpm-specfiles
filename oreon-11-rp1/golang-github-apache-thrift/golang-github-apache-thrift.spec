%global source0_hash d3a60676b1df3fb9850f6ce1e8a3df9a0efac036ceb4bce8ce46ee3eca735d2d
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/apache/thrift
Version:                0.24.0
%gometa
%global goaltipaths     git.apache.org/thrift.git
%global common_description %{expand:
Thrift is a lightweight, language-independent software stack with an associated
code generation mechanism for point-to-point RPC. Thrift provides clean
abstractions for data transport, data serialization, and application level
processing. The code generation system takes a simple definition language as
input and generates code across programming languages that uses the abstracted
stack to build interoperable RPC clients and servers.}
%global golicenses      LICENSE NOTICE
%global godocs          lib/go/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Thrift Go Software Library
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/thrift-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/mock/gomock)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
# Remove files unrelated to the Go Library
find ./* -maxdepth 0 -type d -not -name "lib" -and -not -name "_build" -exec rm -rf "{}" \;
find ./lib -mindepth 1 -maxdepth 1 -type d -not -name "go" -exec rm -rf "{}" \;
rm -rf lib/go/test

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
