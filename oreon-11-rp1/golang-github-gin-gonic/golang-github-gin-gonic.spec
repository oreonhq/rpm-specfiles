%global source0_hash c4210a179c9f129462eafcbd4d6d6dfe9559597be32c09041c1c9f797fa558bc
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global debug_package %{nil}
%ifnarch s390x %{ix86} %{arm}
%bcond check 0
%endif
%global goipath         github.com/gin-gonic/gin
Version:                1.12.0
%gometa
%global common_description %{expand:
Gin is a web framework written in Go. It features a martini-like API with much
better performance, up to 40 times faster thanks to httprouter. If you need
performance and good productivity, you will love Gin.}
%global golicenses      LICENSE
%global godocs          examples AUTHORS.md BENCHMARKS.md CHANGELOG.md\\\
                        CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        HTTP web framework written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gin-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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

%gocheck -d render
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
