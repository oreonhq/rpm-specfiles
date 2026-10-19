%global source0_hash bb6e2ca1eb1f01e65c15aae26b8117488864955bf8c162580ffe9ab3f2f060c1
%bcond check 1
%global debug_package %{nil}
%global goipath         gopkg.in/redis.v6
%global forgeurl        https://github.com/go-redis/redis
Version:                6.15.9
%gometa
%global goaltipaths     github.com/go-redis/redis
%global common_description %{expand:
Type-safe Redis client for Golang.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Type-safe Redis client for Golang
License:        LicenseRef-Callaway-BSD AND Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/redis-%{version}.tar.gz
Patch0:         redis-testing-fixes.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  redis
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
sed -i "s|github.com/go-redis/redis|gopkg.in/redis.v6|" $(find . -iname "*.go" -type f)

%install
%gopkginstall
%global _testdata_redis_src %{_builddir}/redis-%{version}/testdata/redis/src
mkdir -p %{_testdata_redis_src}
ln -s %{_bindir}/redis-server %{_testdata_redis_src}/redis-server
%oreon_autofiles main
%if %{with check}
%check

redis-cli -p 28126 SHUTDOWN 2>/dev/null || true
redis-server --port 28126 &
sleep 0.2   # time to startup
redis-cli -p 28126 PING || exit 1
%gocheck
redis-cli -p 28126 SHUTDOWN || exit 1
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
