%global source0_hash 374bd9c039ca795b3739fe28c12c58b814b23e112f9e46a4bf29cde751b23af1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/rackspace/gophercloud
Version:                1.0.0
%global commit          e00690e87603abe613e9f02c816c7c4bef82e063
%gometa
%global common_description %{expand:
Gophercloud is a flexible SDK that allows you to consume and work with OpenStack
clouds in a simple and idiomatic way using Golang. Many services are supported,
including Compute, Block Storage, Object Storage, Networking, and Identity. Each
service API is backed with getting started guides, code samples, reference
documentation, unit tests and acceptance tests.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md CONTRIBUTORS.md README.md\\\
                        UPGRADING.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Go SDK for OpenStack
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gophercloud-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(gopkg.in/yaml.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -t openstack/blockstorage \
         -t openstack/cdn/v1 \
         -d openstack/common/extensions \
         -t openstack/compute/v2 \
         -t openstack/db/v1 \
         -t openstack/identity/v2 \
         -t openstack/imageservice/v2 \
         -t openstack/networking/v2 \
         -t openstack/objectstorage/v1 \
         -t openstack/orchestration/v1 \
         -t openstack/telemetry/v2 \
         -t rackspace/autoscale/v1 \
         -t rackspace/blockstorage/v1 \
         -t rackspace/cdn/v1 \
         -t rackspace/compute/v2 \
         -t rackspace/db/v1 \
         -t rackspace/identity/v2 \
         -t rackspace/lb/v1 \
         -t rackspace/networking/v2 \
         -t rackspace/objectstorage/v1 \
         -t rackspace/orchestration/v1
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
