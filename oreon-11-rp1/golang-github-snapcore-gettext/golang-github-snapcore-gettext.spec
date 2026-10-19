%global source0_hash edfd67cc1064c1327adca7785d3e29e9bb6f9d727d5a5ec3634407a0e9261e88
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/snapcore/go-gettext
%global commit          38740d1bd3d2503e569b3e79deddd8770ecf424c
%gometa
%global common_description %{expand:
A native Go library for accessing gettext internationalization files.
}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Native Go library for accessing gettext internationalization files
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-gettext-%{commit}.tar.gz
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
