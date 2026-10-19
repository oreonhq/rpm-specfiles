%global source0_hash f008aaa5b0181f311299eb085371cb343f3a4780a1ec1e538696ed26a011a86b
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/letsencrypt/pebble
Version:                2.10.1
%gometa -L -f
%global goaltipaths     github.com/letsencrypt/pebble/v2
%global common_description %{expand:
A miniature version of Boulder, Pebble is a small RFC 8555 ACME test server not
suited for a production certificate authority.}
%global golicenses      LICENSE
%global godocs          docs CODE_OF_CONDUCT.md README.md cmd/pebble-challtestsrv/challtestsrv-README.md
Name:           golang-github-letsencrypt-pebble
Release:        1%{?dist}
Summary:        Pebble is a miniature version of Boulder, a small RFC 8555 ACME test server
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pebble-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
mv cmd/pebble-challtestsrv/README.md challtestsrv-README.md

%if %{without bootstrap}
%build

export GO_LDFLAGS="-X 'main.version=%{version}'"
for cmd in cmd/p* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif
%install
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 docs/man1/pebble* -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
