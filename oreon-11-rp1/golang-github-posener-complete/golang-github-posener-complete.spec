%global source0_hash b189480c1b512de1015dd37fc6bf1cf6cfcb0775f14fc2de4af6fc8282fde9ed
%bcond check 0
%global goipath         github.com/posener/complete
Version:                2.1.0
%gometa
%global common_description %{expand:
Package Complete provides a tool for bash writing bash completion in go, and
bash completion for the go command line.
Writing bash completion scripts is a hard work. This package provides an easy
way to create bash completion scripts for any command, and also an easy way to
install/uninstall the completion of the command.}
%global golicenses      LICENSE.txt
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Bash completion written in go + bash completion for Go command
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/complete-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
