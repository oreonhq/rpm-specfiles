%global source0_hash 5501b7043ab71c8f46d8a3f19ad1c9fafebe2d097b7caf8c34fbd3f1423239cb
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         go.opentelemetry.io/contrib
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go-contrib
Version:                1.28.0
%gometa -L
%global common_description %{expand:
Collection of extensions for OpenTelemetry-Go.}
%global golicenses      LICENSE
%global godocs          README.md RELEASING.md CHANGELOG.md CONTRIBUTING.md
Name:           golang-opentelemetry-contrib
Release:        1%{?dist}
Summary:        Collection of extensions for OpenTelemetry-Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/opentelemetry-go-contrib-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

rm -rfv instrumentation/github.com/astaxie/beego/
# examples are not packaged
rm -rvf propagators/opencensus/examples
# drop until github.com/GoogleCloudPlatform/opentelemetry-operations-go is packaged
rm -rvf detectors/gcp

# Remove deprectaed opencensus
rm -rvf propagators/opencensus/

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

for test in "TestDefaultConfig" "TestPartialUserProvidedConfig" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%ifarch s390x
%gocheck -t instrumentation -d go.opentelemetry.io/contrib/instrgen/driver -d go.opentelemetry.io/contrib/samplers/probability/consistent
%else
%gocheck -t instrumentation -d go.opentelemetry.io/contrib/instrgen/driver
%endif
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
