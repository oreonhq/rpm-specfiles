%global source0_hash 0714edcc578c6a09f2cce3ac7afeec92d54b4dd06ce67bb2bc564311abaf6d60
%bcond check 0
%global goipath         github.com/oklog/ulid
Version:                2.1.2
%gometa -L
%global goaltipaths     %{goipath}/v2
%global common_description %{expand:
Universally Unique Lexicographically Sortable Identifier (ULID) in Go.}
%global golicenses      LICENSE
%global godocs          AUTHORS.md CHANGELOG.md CONTRIBUTING.md README.md
Name:           golang-github-oklog-ulid
Release:        1%{?dist}
Summary:        Universally Unique Lexicographically Sortable Identifier (ULID) in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/ulid-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/ulid %{buildroot}%{_bindir}/ulid-go
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
