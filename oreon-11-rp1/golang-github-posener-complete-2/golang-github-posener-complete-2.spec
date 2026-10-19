%global source0_hash b189480c1b512de1015dd37fc6bf1cf6cfcb0775f14fc2de4af6fc8282fde9ed
%bcond check 0
%global goipath         github.com/posener/complete/v2
%global forgeurl        https://github.com/posener/complete
Version:                2.1.0
%gometa
%global extractdir      %(echo %{extractdir} | sed -e 's/~/-/g')
%global gosource        %(echo %{gosource} | sed -e 's/~/-/g')
%global common_description %{expand:
Bash completion written in go + bash completion for go command.}
%global golicenses      LICENSE.txt
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Bash completion written in go + bash completion for go command
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/complete-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/posener/autogen)
BuildRequires:  golang(github.com/posener/script)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in gocomplete; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d gocomplete
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
