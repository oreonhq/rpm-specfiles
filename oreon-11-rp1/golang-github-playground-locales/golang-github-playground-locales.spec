%global source0_hash a6d61ce717bbaa4add94eee1e41522d5d43b7685b133284fb1d833c38c79d511
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-playground/locales
Version:                0.14.2
%gometa
%global common_description %{expand:
A set of locales generated from the CLDR Project which can be
used independently or within an i18n package; these were built for use with,
but not exclusive to https://github.com/go-playground/universal-translator.}
%global golicenses      LICENSE
%global godocs          README.md cmd/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Set of locales generated from the CLDR Project
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/locales-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
