%global source0_hash 847959e97723aa25513b73812f6a323ada28c616c02677838bdfcb4842bfd67a
%bcond check 1
%bcond check 1
%global goipath         github.com/GoogleCloudPlatform/cloudsql-proxy
Version:                2.26.0
%gometa
%global common_description %{expand:
The Cloud SQL Proxy allows a user with the appropriate permissions to connect
to a Second Generation Cloud SQL database without having to deal with IP
whitelisting or SSL certificates manually. It works by opening unix/tcp
sockets on the local machine and proxying connections to the associated
Cloud SQL instances when the sockets are used.}
%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS\\\
                        README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cloud SQL proxy client and Go library
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cloudsql-proxy-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
