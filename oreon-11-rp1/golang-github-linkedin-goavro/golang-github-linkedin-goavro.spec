%global source0_hash ad07f10aebd8448de39c31e8b2ee27f4a652ea5f70b0eb817f0359e08464da30
%ifnarch %{arm} %{ix86}
%bcond check 0
%endif
%global goipath         github.com/linkedin/goavro
Version:                2.15.0
%gometa
%global goaltipaths     github.com/linkedin/goavro/v2
%global common_description %{expand:
Goavro is a library that encodes and decodes Avro data.}
%global golicenses      LICENSE
%global godocs          examples AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Library that encodes and decodes Avro data
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goavro-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/snappy)
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
