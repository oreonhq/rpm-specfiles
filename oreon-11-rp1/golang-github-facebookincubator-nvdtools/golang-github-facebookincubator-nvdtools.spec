%global source0_hash 78265d34f934df76407019dfe242424587b6c87f3bd359141d0ffef7c48172a8
%bcond check 0
%global goipath         github.com/facebookincubator/nvdtools
Version:                0.1.5
%gometa
%global common_summary %{expand: A collection of tools for working with National Vulnerability Database feeds}
%global common_description %{expand:
A set of tools to work with the feeds (vulnerabilities, CPE dictionary etc.)
distributed by National Vulnerability Database (NVD)}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md HOWTO.md README.md\\\
                        cmd/fireeye2nvd/README.md cmd/flexera2nvd/README.md\\\
                        cmd/idefense2nvd/README.md cmd/nvdsync/README.md\\\
                        cmd/rbs2nvd/README.md cmd/snyk2nvd/README.md\\\
                        cmd/vfeed2nvd/README.md cvss2/README.md\\\
                        cvss3/README.md\\\
                        vulndb/sqlutil/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A collection of tools for working with National Vulnerability Database feeds
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/nvdtools-%{version}.tar.gz
ExcludeArch:    i686 armv7hl
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/andreyvit/diff)
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/facebookincubator/flog)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/clientcredentials)
BuildRequires:  golang(golang.org/x/sync/errgroup)
# /oreon:deps
%description
%{common_description}

%package -n    nvdtools
Summary:       %{common_summary}
%description -n nvdtools
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
for cmd in cmd/* cvss2 cvss3 vulndb/sqlutil; do
  if [ -f $cmd/README.md ]; then
    mv $cmd/README.md $cmd/$(basename $cmd).md
  fi
done

%build

for cmd in cmd/* vulndb/sqlutil/b64schema; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles nvdtools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n nvdtools -f %{oreon_filedir}/nvdtools.list

%changelog

%autochangelog
