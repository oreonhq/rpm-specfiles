%global source0_hash 116ab7d6e6090d973998f69ace133c247ae36373fbffe5cb3dce668615b31dea
%bcond check 0
%global goipath         github.com/jsonnet-bundler/jsonnet-bundler
Version:                0.6.0
%gometa
%global common_description %{expand:
A jsonnet package manager.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A jsonnet package manager
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jsonnet-bundler-%{version}.tar.gz
%if %{with check}
%endif
Requires:       git-core
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

export LDFLAGS="-X main.Version=%{version} "
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
