%global source0_hash fea5e1580dcca7f6581da2ebfec429da5f6bc7f8e5ead2c48e43c71e26c1363c
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/prometheus/common
Version:                0.61.0
%gometa -L -f
%global common_description %{expand:
This repository contains Go libraries that are shared across Prometheus
components and libraries.
 - config: Common configuration structures
 - expfmt: Decoding and encoding for the exposition format
 - log: A logging wrapper around logrus
 - model: Shared data structures
 - route: A routing wrapper around httprouter using context.Context
 - version: Version information and metrics}
%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md MAINTAINERS.md README.md
Name:           golang-github-prometheus-common
Release:        1%{?dist}
Summary:        Go libraries shared across Prometheus components and libraries
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/common-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

export GODEBUG=x509sha1=1
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
