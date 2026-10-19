%global source0_hash d7415d7369a34b74b058eccfdb802b815592b349755ed1685ebff81e0d07b4dc
%bcond check 0
%bcond_with all_tests
%global goipath         entgo.io/ent
%global forgeurl        https://github.com/ent/ent
Version:                0.10.0
%gometa
%global goaltipaths     github.com/facebook/ent
%global common_description %{expand:
An entity framework for Go.}
%global golicenses      LICENSE
%global godocs          doc examples README.md README_jp.md\\\
                        CODE_OF_CONDUCT.md CONTRIBUTING.md README_zh.md\\\
                        entc/integration/README.md doc
Name:           %{goname}
Release:        1%{?dist}
Summary:        An entity framework for Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/ent-%{version}.tar.gz
ExcludeArch:    %{arm32} %{ix86}
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(ariga.io/atlas/sql/migrate)
BuildRequires:  golang(ariga.io/atlas/sql/mysql)
BuildRequires:  golang(ariga.io/atlas/sql/postgres)
BuildRequires:  golang(ariga.io/atlas/sql/schema)
BuildRequires:  golang(ariga.io/atlas/sql/sqlite)
BuildRequires:  golang(github.com/DATA-DOG/go-sqlmock)
BuildRequires:  golang(github.com/go-openapi/inflect)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/modern-go/reflect2)
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sync/semaphore)
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/go/packages/packagestest)
BuildRequires:  golang(golang.org/x/tools/imports)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
# rename integration doc to avoid name clash
mv entc/integration/README.md entc/integration/README-integration.md

%build

for cmd in cmd/ent* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%if %{without all_tests}
rm entc/internal/snapshot_test.go
rm entc/load/load_test.go
%endif
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
