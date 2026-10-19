%global source0_hash 62b0b5eb38f76c9b4b87869ad544edff4dc8376ca6b941b475ccbbe07514acdc
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pierrec/cmdflag
Version:                0.0.2
%gometa
%global common_description %{expand:
Building on top of the excellent flag package from the standard library, cmdflag
adds a simple way of specifying nested commands. Its intent is to blend with the
usage of flag by keeping its idioms and simply augment it with commands.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Augment the flag package with commands
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cmdflag-%{version}.tar.gz
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
