%global source0_hash b2fbb041d17224b74398e184e0105abf2fcb5a10ee5fc57ee13241aced1ff7da
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/insomniacslk/xjson
%global commit          1589ccfd1a1add37673a8f1dca0f1d70af12af7f
%gometa
%global common_description %{expand:
Extended JSON marshallers and unmarshallers (like URL, Time, etc).}
%global golicenses      COPYING
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Extended JSON marshallers and unmarshallers (like URL, Time, etc)
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/xjson-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
