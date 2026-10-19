%global source0_hash aa7a13505b7669c30d64149803295f206bdf0d2fb028a4200c9f5f5541ee607d
%bcond check 0
%global goipath         github.com/tscholl2/siec
%global commit          9bdfc483d4990dd77892b0e8206906b8c7c0f0ad
%gometa
%global common_description %{expand:
Super-Isolated Elliptic Curve Implementation in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Super-Isolated Elliptic Curve Implementation in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/siec-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in search; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

rm search/search_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
