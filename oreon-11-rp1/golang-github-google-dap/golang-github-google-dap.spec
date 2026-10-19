%global source0_hash b0f12c884c613ba6cb5cd086c8acae90d062fae086e8bf0f5a6c6ce5b14da326
%bcond check 0
%global goipath         github.com/google/go-dap
Version:                0.12.0
%gometa
%global common_description %{expand:
Go implementation of the Debug Adapter Protocol.}
%global golicenses      LICENSE
%global godocs          docs README.md cmd/gentypes/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of the Debug Adapter Protocol
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-dap-%{version}.tar.gz
Patch0001:      0001-Disable-TestServer.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
