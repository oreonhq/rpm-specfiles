%global source0_hash 2f8f03b3d972f14e1a5a33bab5d1539174e46c696bc91c5b8ac6d7f9036dde15
%ifarch x86_64
%bcond check 1
%else
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/x448/float16
Version:                0.8.4
%gometa -L -f
%global common_description %{expand:
x448/float16 package provides IEEE 754 half-precision floating-point
format (binary16) with IEEE 754 default rounding for conversions.
IEEE 754-2008 refers to this 16-bit floating-point format as binary16.
IEEE 754 default rounding ("Round-to-Nearest RoundTiesToEven") is
considered the most accurate and statistically unbiased estimate
of the true result.
All possible 4+ billion floating-point conversions with this library
are verified to be correct.
Lowercase "float16" refers to IEEE 754 binary16.
And capitalized "Float16" refers to exported Go data type.
}
%global golicenses      LICENSE
%global godocs          README.md SECURITY.md
Name:           golang-github-x448-float16
Release:        1%{?dist}
Summary:        Provides IEEE 754 half-precision format
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/float16-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
