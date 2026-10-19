%global source0_hash 10bc78fa7b15715a34f35d2ee207bfe0729b7864b093f526ec3cbbf5fa61bd6f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/matrix-org/gomatrixserverlib
%global commit          c2391f7113a5020d28d9fa5680ae025c20062126
%gometa -L -f
%global common_description %{expand:
Go library for matrix federation.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-matrix-org-gomatrixserverlib
Version:        0
Release:        1%{?dist}
Summary:        Go library for matrix federation
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gomatrixserverlib-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

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
