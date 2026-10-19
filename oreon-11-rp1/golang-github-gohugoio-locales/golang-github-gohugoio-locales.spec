%global source0_hash 50ebfe7d16720ece0ceb7d4e2925e9ad544d769a998bb76cda1594ec80d93d31
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gohugoio/locales
Version:                0.14.0
%gometa
%global common_description %{expand:
Locales a set of locales generated from the CLDR Project which can be
used independently or within an i18n package; these were built for use with,
but not exclusive to https://github.com/go-playground/universal-translator.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for locales
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/locales-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/text/unicode/cldr)
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

%gocheck -d eu
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
