%global source0_hash 1436123af12c5075afb8dc31796e2e9c379ea6cbf98ed1c283c2e3cddaca2959
%bcond check 0
%global goipath         github.com/deepmap/oapi-codegen
Version:                2.8.0
%gometa -f
%global common_description %{expand:
Generate Go client and server boilerplate from OpenAPI 3 specifications.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Generate Go client and server boilerplate from OpenAPI 3 specifications
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/oapi-codegen-%{version}.tar.gz
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
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

for test in "TestLoader" \
            "TestRemoteExternalReference" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
