%global source0_hash 77b8e99717c5af30f3a6be5d2418397c8f5ef298c0fc40c5ce5158781ea67001
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gorilla/sessions
Version:                1.4.0
%gometa
%global common_description %{expand:
Package gorilla/sessions provides cookie and filesystem sessions and
infrastructure for custom session backends.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cookie and filesystem sessions and infrastructure for custom session backends
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sessions-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gorilla/securecookie)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
