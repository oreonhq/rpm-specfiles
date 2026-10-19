%global source0_hash 01ca48a2beaeeda5b9fbca9c46bb9e9acc0e55354761d90e4beba5ca1c97aa8b
%bcond check 0
%global goipath         github.com/a8m/envsubst
Version:                1.4.3
%gometa
%global common_description %{expand:
Go package for substituting environment variables.}
%global golicenses      LICENSE
%global godocs          _example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Environment variables substitution for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/envsubst-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/goenvsubst %{goipath}/cmd/envsubst
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
