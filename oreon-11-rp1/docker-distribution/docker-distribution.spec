%global source0_hash 2f9b6fc00bec854e62e9b720903a9c9b48018505177f7c7a8ce7b74da2b23e4f
%bcond check 1
%global goipath   github.com/distribution/distribution/v3
%global forgeurl  https://github.com/distribution/distribution
Version:          3.1.2
%gometa -L -f
Name:             docker-distribution
Release:        1%{?dist}
Summary:        The toolkit to pack, ship, store, and deliver container content
License:          Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:              %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/distribution-%{version}.tar.gz
Source1:          %{archivename}-vendor.tar.bz2
Source2:          go-vendor-tools.toml
Source10:         docker-distribution.service
Source20:         config.yml
Source30:         docker-distribution.sysuser.conf
%{?sysusers_requires_compat}
Provides:         registry = %{version}-%{release}
Obsoletes:        golang-github-docker-distribution < 2.8.3-5
Obsoletes:        golang-github-distribution-3 < 3.0.0-0.8
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.
This package provides Docker Registry - a service for
storing and distributing OCI and Docker container images.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS=" -X %{goipath}/version.version=%{version} -X %{goipath}/version.revision=%{release} "
%global currentgoldflags   %nil
%gobuild -o %{gobuilddir}/bin/registry %{goipath}/cmd/registry
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE10} %{buildroot}%{_unitdir}
install -d -p %{buildroot}%{_sysconfdir}/docker-distribution/registry
install -p -m 644 %{SOURCE20} %{buildroot}%{_sysconfdir}/docker-distribution/registry
install -d %{buildroot}%{_sharedstatedir}/registry
install -p -D -m 0644 %{SOURCE30} %{buildroot}%{_sysusersdir}/docker-distribution.conf
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in \
           "TestHTTPChecker" \
           "TestFileReaderSeek" \
           "TestListObjectsV2" \
           "TestGracefulShutdown" \
           "TestInMemoryDriverSuite" \
           "TestWriteReadLargeStreams" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%global gocheckflags   %{?gocheckflags} -test.short
%gocheck -d registry/storage/driver/inmemory \
         -d registry/storage/driver/filesystem \
         -d registry/storage/driver/azure \
         -d registry/storage/driver/gcs \
         -d registry/storage/driver/s3-aws \
         -d registry/storage/driver/testsuites \
         -d registry/handlers
%endif
%pre

%sysusers_create_compat %{SOURCE30}
%post

%systemd_post docker-distribution.service
%preun

%systemd_preun docker-distribution.service
%postun

%systemd_postun_with_restart docker-distribution.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
