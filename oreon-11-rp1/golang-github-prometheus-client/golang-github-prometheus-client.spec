%global source0_hash 9435a701e8488b5a30586a2511e5b674c4d381cf154c9c43bc4ef47e45d64cc7
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/prometheus/client_golang
Version:                1.24.1
%gometa -f
%global common_description %{expand:
This is the Go client library for Prometheus. It has two separate parts, one for
instrumenting application code, and one for creating clients that talk to the
Prometheus HTTP API.}
%global golicenses      LICENSE NOTICE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        MAINTAINERS.md SECURITY.md CHANGELOG.md README.md\\\
                        README-prometheus.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Prometheus instrumentation library for Go applications
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/client_golang-%{version}.tar.gz
Patch:          0001-ADd-metrics-for-go1.23.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

# Avoid extra deps
rm -rf .bingo examples tutorial

%install
%gopkginstall
mv prometheus/README.md README-prometheus.md
%oreon_autofiles main
%if %{with check}
%check

for test in "TestSummaryDecay" "TestMemStatsEquivalence" "TestBuckets" "TestNativeHistogram" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%ifarch %{ix86} %{arm}
%gocheck -d api/prometheus/v1
%else
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
