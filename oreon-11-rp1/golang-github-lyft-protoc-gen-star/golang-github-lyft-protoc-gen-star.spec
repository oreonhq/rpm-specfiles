%global source0_hash 754b158a86b6df3be0cbb63cccf75c27d08493482a0cdc993063ab849d2b2ad8
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/lyft/protoc-gen-star
Version:                2.0.4
%gometa
%global common_description %{expand:
Protoc plugin library for efficient proto-based code generation.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Protoc plugin library for efficient proto-based code generation
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/protoc-gen-star-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/protobuf/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires:  golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/any)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
