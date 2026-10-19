%global source0_hash 7f9974d0c8461b704ef0baaa6689d05e0867f002279114052bd4c1829ceab101
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cucumber/gherkin-go
Version:                25.0.2
%gometa
%global goaltipaths     github.com/cucumber/gherkin-go/v21
%global common_description %{expand:
Gherkin parser/compiler for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Gherkin parser/compiler for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gherkin-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/cucumber/messages-go/v17)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
sed -i 's|"github.com/cucumber/common/gherkin/go/v21|"github.com/cucumber/gherkin-go|' $(find . -iname "*.go" -type f)
sed -i 's|"github.com/cucumber/common/messages/go/v17|"github.com/cucumber/messages-go/v17|' $(find . -iname "*.go" -type f)

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
