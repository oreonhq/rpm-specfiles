%global source0_hash 470174971c3a63361149a30f5b2d3a716a198afeb6cc71daa30712faa7293942
%bcond check 0
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(a\\)$
%global goipath         github.com/golang/mock
Version:                1.6.0
%gometa
%global common_description %{expand:
GoMock is a mocking framework for the Go programming language. It integrates
well with Go's built-in testing package, but can be used in other contexts too.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Gomock is a mocking framework for the go programming language
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mock-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/tools/go/packages)
BuildRequires:  golang(golang.org/x/tools/present)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in mockgen; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d mockgen
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
