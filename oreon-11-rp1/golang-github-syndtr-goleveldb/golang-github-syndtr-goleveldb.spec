%global source0_hash d365a4ea7e214fa7cdef3c9ff734e58379eff00baeea2e02ee9dfefd1fc6b266
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/syndtr/goleveldb
Version:                1.0.0
%global commit          5c35d600f0caac04c20d52438103f1a7aa612598
%gometa
%global common_description %{expand:
This is an implementation of the LevelDB key/value database in the Go
programming language.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Leveldb key/value database in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goleveldb-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/ginkgo/config)
BuildRequires:  golang(github.com/onsi/gomega)
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

export ACK_GINKGO_DEPRECATIONS=1.16.5
export ACK_GINKGO_RC=true
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
