%global source0_hash c2ab361419bd4307c3b52d4b1348b9db1140ca805ce2393aad4a21a858fca748
%bcond check 0
%global goipath         github.com/olekukonko/tablewriter
Version:                1.1.5
%gometa
%global common_description %{expand:
ASCII Table Writer.}
%global golicenses      LICENSE.md
%global godocs          README.md README-csv2table.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        ASCII table in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/tablewriter-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-runewidth)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv csv2table/README.md README-csv2table.md

%build

for cmd in csv2table; do
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
