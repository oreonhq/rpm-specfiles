%global source0_hash 3ac13de033e03dd97518d2bb0f8123379830f02e8be3068c0aaf58470c6154f0
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/AzureAD/microsoft-authentication-library-for-go
Version:                1.10.1
%gometa -f
%global common_description %{expand:
The MSAL library for Go is part of the Microsoft identity platform for
developers (formerly named Azure AD) v2.0. It enables you to acquire security
tokens to call protected APIs. It uses industry standard OAuth2 and OpenID
Connect.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md SECURITY.md\\\
                        changelog.md RELEASES.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        The MSAL library for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/microsoft-authentication-library-for-go-%{version}.tar.gz
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
