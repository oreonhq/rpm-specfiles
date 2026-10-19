%global source0_hash none
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/ccgo/v4
%global forgeurl        https://gitlab.com/cznic/ccgo
Version:                4.23.16
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
ccgo is a C compiler targeting Go.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        C compiler targeting Go
License:        BSD-3-Clause and blessing
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ccgo-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

%goprep
# Not free:
find . ! \( -name v4 -o -name _build  -o -name LICENSE -o -name AUTHORS -o -name CONTRIBUTORS -o -name README.md \) -maxdepth 1 -exec rm -rvf {} \;
mv v4/* .

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d lib
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
