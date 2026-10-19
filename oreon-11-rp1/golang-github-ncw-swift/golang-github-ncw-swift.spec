%global source0_hash 0df8051da1eb861412489fc680e4835f6daa322c85bc220ab6a5af3c70ff00fe
%ifnarch aarch64
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/ncw/swift
Version:                1.0.52
%gometa
%global common_description %{expand:
This package provides an easy to use library for interfacing with Swift /
Openstack Object Storage / Rackspace cloud files from the Go Language.}
%global golicenses      COPYING
%global godocs          notes.txt README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go language interface to swift
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/swift-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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

%gocheck -d rs
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
