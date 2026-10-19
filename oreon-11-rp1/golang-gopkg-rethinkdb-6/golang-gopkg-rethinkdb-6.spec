%global source0_hash 2b47ee53346517c3f314dce6eb5a2cb415f7defaf4dd6d80dae45299939b6f41
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/rethinkdb/rethinkdb-go.v6
%global forgeurl        https://github.com/rethinkdb/rethinkdb-go
Version:                6.2.1
%gometa
%global common_description %{expand:
Go language driver for RethinkDB.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go language driver for RethinkDB
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/rethinkdb-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/cenkalti/backoff/v4)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/hailocab/go-hostpool)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/opentracing/opentracing-go/mocktracer)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(gopkg.in/check.v1)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
sed -i 's|gopkg.in/cenkalti/backoff.v2|github.com/cenkalti/backoff/v4|' $(find . -iname "*.go" -type f)

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -t internal/integration
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
