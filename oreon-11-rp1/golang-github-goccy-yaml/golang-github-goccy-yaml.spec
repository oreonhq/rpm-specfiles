%global source0_hash 2cd611523019b61580a7f42056f92b1543c33f10bf5cda5d393608732577d6f9
%bcond check 0
%global goipath         github.com/goccy/go-yaml
Version:                1.19.2
%gometa -L -f
%global common_description %{expand:
Go package similar to github.com/go-yaml/yaml with some additional
features.}
%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md
Name:           golang-github-goccy-yaml
Release:        1%{?dist}
Summary:        YAML support for the Go language
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-yaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
