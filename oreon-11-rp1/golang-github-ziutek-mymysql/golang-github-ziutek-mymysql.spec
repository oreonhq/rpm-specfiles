%global source0_hash e28d68240bb16584abb869b94aa0f67b28499f83c7b07bebc85522a6a74ff114
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ziutek/mymysql
Version:                1.5.4
%global commit          adcfec29206e9f557b2873e46797cc7ceafc81ec
%gometa
%global common_description %{expand:
This package contains MySQL client API written entirely in Go. It is designed to
work with the MySQL protocol version 4.1 or greater. It definitely works well
with MySQL server version 5.0 and 5.1 (I use these versions of MySQL servers for
my applications).}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        MySQL Client API written entirely in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/mymysql-%{commit}.tar.gz
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

%gocheck -d autorc -d godrv -d native -d thrsafe
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
