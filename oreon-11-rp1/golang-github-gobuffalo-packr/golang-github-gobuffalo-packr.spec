%global source0_hash 67352bb3a73f6b183d94dd94f1b5be648db6311caa11dcfd8756193ebc0e2db9
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gobuffalo/packr
Version:                2.8.3
%gometa
%global goaltipaths     github.com/gobuffalo/packr/v2
%global common_description %{expand:
Packr is a simple solution for bundling static assets inside of Go binaries.
Most importantly it does it in a way that is friendly to developers while they
are developing.}
%global golicenses      LICENSE.txt
%global godocs          example README.md SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple and easy way to embed static files into Go binaries
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/packr-%{version}.tar.gz
Patch:          fix-test-failures.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gobuffalo/envy)
BuildRequires:  golang(github.com/gobuffalo/logger)
BuildRequires:  golang(github.com/gobuffalo/packd)
BuildRequires:  golang(github.com/karrick/godirwalk)
BuildRequires:  golang(github.com/markbates/errx)
BuildRequires:  golang(github.com/markbates/oncer)
BuildRequires:  golang(github.com/markbates/safe)
BuildRequires:  golang(github.com/rogpeppe/go-internal/modfile)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
