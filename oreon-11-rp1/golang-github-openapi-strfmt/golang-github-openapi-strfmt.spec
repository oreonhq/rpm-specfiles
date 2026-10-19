%global source0_hash a987dda628ce70988daa8e35f34020d0184358e3ceabc811863dbf51c33532d5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/strfmt
Version:                0.27.2
%gometa
%global common_description %{expand:
This package exposes a registry of data types to support string formats in the
Go-openapi toolkit.
Strfmt represents a well known string format such as credit card or email. The
go toolkit for OpenAPI specifications knows how to deal with those.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Openapi toolkit common string formats
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/strfmt-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/asaskevich/govalidator)
BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/oklog/ulid)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson/bsontype)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson/primitive)
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
