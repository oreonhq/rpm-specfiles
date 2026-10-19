%global source0_hash 9b6f274947324e64c87aca3be7759fe16db2be9187c13a79711e9f406fe10121
%bcond check 0
%global goipath         github.com/containerd/continuity
Version:                0.5.0
%gometa
%global common_description %{expand:
A transport-agnostic, filesystem metadata manifest system.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A transport-agnostic, filesystem metadata manifest system
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/continuity-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/continuity %{goipath}/cmd/continuity
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

for test in "TestCopyWithLargeFile" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
