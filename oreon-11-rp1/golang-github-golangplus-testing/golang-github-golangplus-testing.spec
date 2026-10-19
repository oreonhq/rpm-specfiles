%global source0_hash 09c60f1d23564068ea240d6955bae0c30fab82c8cbe90111c9a25ad382bde8f6
%bcond check 0
%bcond_with bootstrap
%global debug_package %{nil}
%global goipath         github.com/golangplus/testing
Version:                1.0.0
%gometa
%global common_description %{expand:
Package Testingp is a plus to standard "testing" package..}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Plus to the standard testing package
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/testing-%{version}.tar.gz
%if %{without bootstrap}
%if %{with check}
%endif
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golangplus/fmt)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
