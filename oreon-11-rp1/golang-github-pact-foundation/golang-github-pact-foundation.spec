%global source0_hash 744c556f3e264ecc423802ad055ab057d723a2f66928aee8352fc92632a29b9e
%bcond check 0
%global goipath         github.com/pact-foundation/pact-go
Version:                2.8.0
%gometa
%global common_description %{expand:
Pact Go enables consumer driven contract testing, providing a mock service and
DSL for the consumer project, and interaction playback and verification for the
service provider project.}
%global golicenses      LICENSE
%global godocs          examples RELEASING.md CHANGELOG.md CONTRIBUTING.md\\\
                        README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Contract testing framework for HTTP APIs and non-HTTP messaging systems for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pact-go-%{version}.tar.gz
%if %{with check}
%endif
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

%gobuild -o %{gobuilddir}/bin/pact %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d dsl -d command
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
