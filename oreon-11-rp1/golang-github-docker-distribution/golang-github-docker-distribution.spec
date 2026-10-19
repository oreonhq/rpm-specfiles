%global source0_hash c44841796ff59d8b4d62c7f86b58a0fb8f6e60b887a974758cc90079dca628ba
%bcond check 0
%global goipath         github.com/docker/distribution
Version:                2.8.3
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
The Docker toolset to pack, ship, store, and deliver content.
This repository's main product is the Docker Registry 2.0 implementation for
storing and distributing Docker images. It supersedes the docker/docker-registry
project with a new API design, focused around security and performance.}
%global golicenses      LICENSE
%global godocs          docs BUILDING.md CONTRIBUTING.md README.md ROADMAP.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Docker toolkit to pack, ship, store, and deliver container content
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/distribution-%{version}.tar.gz
Patch01:          0001-Partial-backport-of-8f9c809.patch
Patch02:          0002-Partial-backport-of-907e7be.patch
Patch03:          format-errors.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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

for test in "TestHTTPChecker" \
            "TestFileReaderSeek" \
            "TestListObjectsV2" \
            "TestGracefulShutdown" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%if 0%{?__isa_bits} == 32
%gocheck -d registry/storage/driver/inmemory \
         -d registry/handlers \
         -d registry/storage/driver/swift \
         -d registry/storage/driver/filesystem
%else
%gocheck -d registry/storage/driver/inmemory \
         -d registry/handlers
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
