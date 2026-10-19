%global source0_hash 596cb87d95aa3abfecd9ad741136562a6df3daf91c14ca4ac60698bcf1625437
%bcond check 0
%global goipath         github.com/j-keck/arping
Version:                1.0.3
%gometa
%global common_description %{expand:
Arping is a native Go library to ping a host per arp datagram, or query a host
mac address.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Native Go library to ping a host per arp datagram, or query a host mac address
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/arping-%{version}.tar.gz
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
