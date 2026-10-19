%global source0_hash 756e00e87207cb063d305b6e38bf56dba4d76586fbe40b7d6b657d22516d0f71
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/inf.v0
%global forgeurl        https://github.com/go-inf/inf
Version:                0.9.1
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-googlecode-go-decimal-inf-devel < 0.9.0-0.8
Obsoletes:      golang-googlecode-go-decimal-inf-unit-test < 0.9.0-0.8
}
%global common_description %{expand:
Package inf (type inf.Dec) implements "infinite-precision" decimal arithmetic.
"Infinite precision" describes two characteristics: practically unlimited
precision for decimal number representation and no support for calculating with
any specific fixed precision. (Although there is no practical limit on
precision, inf.Dec can only represent finite decimals.).}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        "Infinite-precision" decimal arithmetic
License:        BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/inf-%{version}.tar.gz
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
