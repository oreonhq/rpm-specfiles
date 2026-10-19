%global source0_hash 50389c3e984f8154e6988dcd49a50f31abbe758573f4fb4bd52a686c73d2cb56
%bcond check 0
%global goipath         github.com/coreos/go-semver
Version:                0.3.1
%global commit          167f5da54033088a1d6b3049504828fa2ff8b116
%gometa
%global common_description %{expand:
Go-semver is a semantic versioning library for Go. It lets you parse and compare
two semantic version strings.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md code-of-conduct.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Semver library in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-semver-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/go-semver %{goipath}
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
