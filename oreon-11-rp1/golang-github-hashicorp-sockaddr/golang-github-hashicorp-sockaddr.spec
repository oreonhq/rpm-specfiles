%global source0_hash a4cbf07256defca1489412cd5ce7d5fa064439b85bacb42b113ae97c61b17c93
%bcond check 1
%global goipath         github.com/hashicorp/go-sockaddr
Version:                1.0.7
%gometa -L -f
%global common_description %{expand:
Socket address convenience functions for Go. go-sockaddr is a convenience
library that makes doing the right thing with IP addresses easy. go-sockaddr is
loosely modeled after the UNIX sockaddr_t and creates a union of the family of
sockaddr_t types (see below for an ascii diagram). Library documentation is
available at https://godoc.org/github.com/hashicorp/go-sockaddr. The primary
intent of the library was to make it possible to define heuristics for selecting
the correct IP addresses when a configuration is evaluated at runtime. See the
docs, template package, tests, and CLI utility for details and hints as to how
to use this library.}
Name:           golang-github-hashicorp-sockaddr
Release:        1%{?dist}
Summary:        IP Address/UNIX Socket convenience functions for Go
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-sockaddr-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch01:	skip_tests.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
echo ">====<"
ls -l %{gobuilddir}/bin/*
echo ">====<"
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
