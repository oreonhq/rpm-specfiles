%global source0_hash 4ad7fb7616dcbdc2d394ff98350226659e10dfe4dde9ed3256881351b0d515bb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/gofuzz
Version:                1.2.0
%gometa
%global common_description %{expand:
Gofuzz is a library for populating Go objects with random values.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fuzz testing for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gofuzz-%{version}.tar.gz
Patch0:         0001-Fix-int-overflow.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
