%global source0_hash 3113324f2249e9a135eea008c75f56b7cb39e9625e0a3e0bff5e764211c5f76a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/unknwon/com
Version:                1.0.1
%gometa
%global goaltipaths     github.com/Unknwon/com
%global common_description %{expand:
This is an open source project for commonly used functions for the Go
programming language.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Epoch:          1
Release:        1%{?dist}
Summary:        Commonly used functions for the Go programming language
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/com-%{version}.tar.gz
Patch0:         no-internet-access.patch
Patch1:         0001-Convert-int-to-string-using-rune.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
%patch -P1 -p1

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
