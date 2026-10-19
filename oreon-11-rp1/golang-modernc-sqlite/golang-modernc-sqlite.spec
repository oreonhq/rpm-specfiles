%global source0_hash none
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/sqlite
%global forgeurl        https://gitlab.com/cznic/sqlite
Version:                1.35.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
A port of SQLite/SQLite3 to Go without cgo.
SQLite is an in-process implementation of a self-contained, serverless, zero-
configuration, transactional SQL database engine.}
%global golicenses      LICENSE SQLITE-LICENSE
%global godocs          examples AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A port of SQLite/SQLite3 to Go without cgo
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/sqlite-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/ncruces/go-strftime)
# /oreon:deps
%description %{common_description}

%prep

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
