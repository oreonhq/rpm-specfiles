%global source0_hash c2cffcba50754ad15ea9459d641f477ce815365868f4c6df4120ce756f26c32c
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/mgo.v2
%global forgeurl        https://github.com/go-mgo/mgo
Version:                r2016.08.01
%global commit          a6b53ec6cb22a3699387a57a161566f9402ee85b
%gometa -f
%global common_description %{expand:
The MongoDB driver for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        MongoDB driver for Go
License:        BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/mgo-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(gopkg.in/tomb.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
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

%gocheck -d . -d dbtest -d txn
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
