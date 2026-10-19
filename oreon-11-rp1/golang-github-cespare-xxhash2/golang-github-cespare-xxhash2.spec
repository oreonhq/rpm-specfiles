%global source0_hash 0e3dda07b03a5f3733506218860ecb2d50c0f01f16299b5d60902ef5158cbde5
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/cespare/xxhash/v2
Version:                2.3.0
%gometa -L -f
%global common_description %{expand:
A Go implementation of the 64-bit xxHash algorithm (XXH64).}
%global golicenses      LICENSE.txt
%global godocs          README.md
Name:           golang-github-cespare-xxhash2
Release:        1%{?dist}
Summary:        A Go implementation of the 64-bit xxHash algorithm (XXH64)
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/cespare/xxhash/archive/v%{version}/xxhash-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%build

%gobuild -o %{gobuilddir}/bin/goxxhsum %{goipath}/xxhsum
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
