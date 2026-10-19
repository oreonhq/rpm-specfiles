%global source0_hash 4d71419902d04b18e6d0fe5d9e295edffcfa88e7282ab42fe3410b000feb5f1e
%bcond check 0
%global goipath         github.com/cucumber/godog
Version:                0.16.0
%gometa
%global common_description %{expand:
Cucumber for golang.}
%global golicenses      LICENSE
%global godocs          _examples CHANGELOG.md CHANGELOG_OLD.md\\\
                        CONTRIBUTING.md README.md release-notes/v0.10.0.md\\\
                        release-notes/v0.11.0.md release-notes/v0.12.0.md\\\
                        release-notes/v0.9.0.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cucumber for golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/godog-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/cucumber/gherkin-go/v21)
BuildRequires:  golang(github.com/cucumber/messages-go/v17)
BuildRequires:  golang(github.com/hashicorp/go-memdb)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
sed -i 's|github.com/cucumber/gherkin-go/v19|github.com/cucumber/gherkin-go/v21|' $(find . -iname "*.go" -type f)
sed -i 's|github.com/cucumber/messages-go/v16|github.com/cucumber/messages-go/v17|' $(find . -iname "*.go" -type f)

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d . -t internal
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
