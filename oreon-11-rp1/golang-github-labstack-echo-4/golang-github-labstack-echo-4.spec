%global source0_hash 00c2594da9650fd199391666a7cf7f98b1c594f725ab2cddb1a8e710ce75c9de
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/labstack/echo/v4
%global forgeurl        https://github.com/labstack/echo
Version:                5.4.0
%gometa
%global common_description %{expand:
High performance, minimalist Go web framework.}
%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md _fixture/_fixture/README.md\\\
                        _fixture/certs/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        High performance, minimalist Go web framework
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/echo-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/labstack/gommon/bytes)
BuildRequires:  golang(github.com/labstack/gommon/color)
BuildRequires:  golang(github.com/labstack/gommon/log)
BuildRequires:  golang(github.com/labstack/gommon/random)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/valyala/fasttemplate)
BuildRequires:  golang(golang.org/x/crypto/acme)
BuildRequires:  golang(golang.org/x/crypto/acme/autocert)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/h2c)
BuildRequires:  golang(golang.org/x/time/rate)
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
