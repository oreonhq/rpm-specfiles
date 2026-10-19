%global source0_hash a9dda1397a16e49440102ba573d3f033059b01555d40a8d2e7073578b941010c
%bcond check 0
%global debug_package %{nil}
%global goipath         code.cloudfoundry.org/clock
%global forgeurl        https://github.com/cloudfoundry/clock
Version:        1.90.0
%gometa
%global common_description %{expand:
This package provides a Clock interface, useful for injecting time dependencies
in tests.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Time provider & rich fake for Go
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/clock-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%install
%gopkginstall
%go_vendor_license_install -c %{S:2}
%oreon_autofiles main

%check

export GOPATH=$PWD/_build
cd _build/src/%{goipath}
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%dir %{_licensedir}/%{name}
%{_licensedir}/%{name}/LICENSE
%{_licensedir}/%{name}/NOTICE
%{_licensedir}/%{name}/vendor/github.com/Masterminds/semver/v3/LICENSE.txt
%{_licensedir}/%{name}/vendor/github.com/go-logr/logr/LICENSE
%{_licensedir}/%{name}/vendor/github.com/go-task/slim-sprig/v3/LICENSE.txt
%{_licensedir}/%{name}/vendor/github.com/google/go-cmp/LICENSE
%{_licensedir}/%{name}/vendor/github.com/google/pprof/AUTHORS
%{_licensedir}/%{name}/vendor/github.com/google/pprof/LICENSE
%{_licensedir}/%{name}/vendor/github.com/onsi/ginkgo/v2/LICENSE
%{_licensedir}/%{name}/vendor/github.com/onsi/gomega/LICENSE
%{_licensedir}/%{name}/vendor/github.com/tedsuo/ifrit/LICENSE
%{_licensedir}/%{name}/vendor/go.yaml.in/yaml/v3/LICENSE
%{_licensedir}/%{name}/vendor/go.yaml.in/yaml/v3/NOTICE
%{_licensedir}/%{name}/vendor/golang.org/x/mod/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/mod/PATENTS
%{_licensedir}/%{name}/vendor/golang.org/x/net/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/net/PATENTS
%{_licensedir}/%{name}/vendor/golang.org/x/sync/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/sync/PATENTS
%{_licensedir}/%{name}/vendor/golang.org/x/sys/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/sys/PATENTS
%{_licensedir}/%{name}/vendor/golang.org/x/text/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/text/PATENTS
%{_licensedir}/%{name}/vendor/golang.org/x/tools/LICENSE
%{_licensedir}/%{name}/vendor/golang.org/x/tools/PATENTS
%{_licensedir}/%{name}/vendor/modules.txt
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
