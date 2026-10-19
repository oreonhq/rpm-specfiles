%global source0_hash 31fb1bc4a9028558f8c4f36edaef99ccc122accdb45ef73895f9727b34358e06
%bcond check 0
%global golang_arches x86_64 aarch64 ppc64le s390x
%global goipath         github.com/cockroachdb/pebble
%global commit          48f55301c5c4197021b030979007fe2fecf17380
%gometa
%global common_description %{expand:
RocksDB/LevelDB inspired key-value database in Go.}
%global golicenses      LICENSE
%global godocs          docs README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        RocksDB/LevelDB inspired key-value database in Go
License:        LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pebble-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/cespare/xxhash/v2)
BuildRequires:  golang(github.com/cockroachdb/errors)
BuildRequires:  golang(github.com/cockroachdb/errors/oserror)
BuildRequires:  golang(github.com/cockroachdb/redact)
BuildRequires:  golang(github.com/codahale/hdrhistogram)
BuildRequires:  golang(github.com/ghemawat/stream)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/exp/rand)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
sed -i 's|\[JOB 5\] WAL delete error: ‹×›|\[JOB 5\] WAL delete error: unredacted error: ‹×›|' event_listener_test.go

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

%gocheck -d internal/lint
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
