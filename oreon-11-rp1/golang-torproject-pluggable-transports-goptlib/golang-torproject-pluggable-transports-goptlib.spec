%global source0_hash eb8a5a534ad9e1d5ebb19d1eed8aed055f63c7ea9d1cda2dd2066d497a095ae9
%bcond check 0
%global debug_package %{nil}
%global goipath         git.torproject.org/pluggable-transports/goptlib.git
Version:                1.4.0
%global repo            goptlib
%global archivename     %{repo}-%{version}
%global archiveext      tar.gz
%global archiveurl      %{nil}
%global topdir          %{repo}-%{version}
%global extractdir      %{repo}-%{version}
%global scm             git
%gometa
%global common_description %{expand:
Goptlib is a library for writing Tor pluggable transports in Go.}
%global golicenses      COPYING
%global godocs          examples ChangeLog README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for writing Tor pluggable transports in Go
License:        CC0-1.0
URL:            https://gitweb.torproject.org/pluggable-transports/goptlib.git
Source0:        goptlib-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
