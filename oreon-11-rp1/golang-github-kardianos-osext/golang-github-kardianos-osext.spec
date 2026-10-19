%global source0_hash 2d4c4a4bbfdc3a34e50224f7b30ea4907a5e459e7940c03e34a9b7a13e07f841
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/kardianos/osext
%global commit          2bc1f35cddc0cc527b4bc3dce8578fc2a6c11384
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-bitbucket-kardianos-osext-devel < 0-0.25
}
%global goaltipaths     bitbucket.org/kardianos/osext
%global common_description %{expand:
Find the current Executable and ExecutableFolder.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Extensions to the standard "os" package
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/osext-%{commit}.tar.gz
Patch0:         0001-disable-broken-test.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
