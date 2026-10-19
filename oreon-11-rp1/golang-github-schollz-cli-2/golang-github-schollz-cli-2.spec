%global source0_hash c67fe8a60f9f53c99311aeac72c3b0b0c0fb0e1377286bed1e3c463b26c7bf3c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/schollz/cli/v2
Version:                2.2.1
%gometa
%global common_description %{expand:
A simple, fast, and fun package for building command line apps in Go.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple, fast, and fun package for building command line apps in Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/schollz/cli/archive/v%{version}/cli-%{version}.tar.gz
Patch0:         https://github.com/schollz/cli/pull/1.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cpuguy83/go-md2man/v2/md2man)
BuildRequires:  golang(gopkg.in/yaml.v2)
# /oreon:deps
%description
%{common_description}

%package        doc
Summary:        Documentation for %{goname}
BuildArch:      noarch
%description    doc
This package contains documentation for %{goname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

rm docs_test.go fish_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n golang-github-masterminds-semver-1-doc -f %{oreon_filedir}/golang-github-masterminds-semver-1-doc.list

%changelog

%autochangelog
