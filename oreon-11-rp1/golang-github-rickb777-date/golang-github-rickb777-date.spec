%global source0_hash adace6ab26dce787e02947b36b62f06309c0793bc8aded8124af82332f46bf66
%bcond check 0
%global goipath         github.com/rickb777/date
Version:                2.4.1
%gometa
%global common_description %{expand:
A Go package for working with dates.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go package for working with dates
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/date-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(github.com/rickb777/plural)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/text/message)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in datetool; do
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
