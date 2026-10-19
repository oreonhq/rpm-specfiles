%global source0_hash a3bc0443933e0b9e21b2c905e6ec012f3f0cfc12291394616095c2ca58d1d3af
%bcond check 0
%global goipath         github.com/knq/sysutil
%global commit          15668db23d08158adb81783bf9e1617e7ca99c10
%gometa
%global common_description %{expand:
Package sysutil provides cross platform system utilities.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           sysutil
Version:        0
Release:        1%{?dist}
Summary:        Provides cross platform system utilities
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
