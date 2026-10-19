%global source0_hash f3e0d75dfe7cafa205809023ed7586c344123debc91275b80cde42426603dca9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/cheekybits/is
%global commit          68e9c0620927fb5427fda3708222d0edee89eae9
%gometa
%global common_description %{expand:
A mini testing helper for Go.
 - Simple interface (is.OK and is.Equal)
 - Plugs into existing Go toolchain (uses testing.T)
 - Obvious for newcomers and newbs
 - Also gives you is.Panic and is.PanicWith helpers - because testing panics is ugly}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Mini testing helper for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/is-%{commit}.tar.gz
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
