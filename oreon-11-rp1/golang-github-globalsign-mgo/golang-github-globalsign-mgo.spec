%global source0_hash 617c48bd5a8b766d1ed0706fa31b9a7f6ffbbae1d56609e79c7f77e52ada3749
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/globalsign/mgo
Version:                r2018.06.15
%global tag             r2018.06.15
%gometa
%global common_description %{expand:
Package Mgo (pronounced as "mango") offers a rich MongoDB driver for Go.}
%global golicenses      LICENSE LICENSE-bson
%global godocs          CONTRIBUTING.md README.md README-bson.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        MongoDB driver for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/mgo-%{version}.tar.gz
Patch0:         0001-Fix-debugf-arguments.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/tomb.v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1
mv bson/README.md README-bson.md
mv bson/LICENSE LICENSE-bson

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
