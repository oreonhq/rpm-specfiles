%global source0_hash ee7d8a46b584bd01b058cf39c1c50f36917074db6eaec6110a385bb39672c9f9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/erikstmartin/go-testdb
%global commit          8d10e4a1bae52cd8b81ffdec3445890d6dccab3d
%gometa
%global common_description %{expand:
Framework for stubbing responses from Go's driver.Driver interface.
This can be used to sit in place of your sql.Db so that you can stub responses
for sql calls, and remove database dependencies for your test suite.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Framework for stubbing responses from Go's driver.Driver interface
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-testdb-%{commit}.tar.gz
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
