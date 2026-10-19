%global source0_hash 50c5fa7a67543f82cec6ccb348e1d8a52b692dea21d2258e54b9be50584d5bbd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xaionaro-go/spinlock
%global commit          30e6d1ce68a1e8ec39cc1388b1387626224cf52d
%gometa
%global common_description %{expand:
This package implements sync.Locker as a spinlock.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Spinlock implementation for golang
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/spinlock-%{commit}.tar.gz
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
