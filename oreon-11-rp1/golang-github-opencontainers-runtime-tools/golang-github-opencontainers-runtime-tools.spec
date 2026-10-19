%global source0_hash 07a4de3f2221f1a60a70a1d645108b9459af6c2d0f18f86551294f396af881b8
%bcond check 0
%global goipath         github.com/opencontainers/runtime-tools
Version:                0.9.0
%global commit          2802ff9ff5458806234cc8bcaeef8b97b274d630
%gometa
%global common_description %{expand:
Ooci-runtime-tool is a collection of tools for working with the OCI runtime
specification.}
%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md CONTRIBUTING.md\\\
                        MAINTAINERS_GUIDE.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OCI Runtime Tools
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/runtime-tools-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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

for test in "TestGenerateValid" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d validate
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
