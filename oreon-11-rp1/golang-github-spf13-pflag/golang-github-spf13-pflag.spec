%global source0_hash 27cc2a48635fd8d6c3efd30482c79e07464e916bc42a46d204a7b34e294ad4af
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/spf13/pflag
Version:                1.0.5
%global commit          d5e0c0615acee7028e1e2740a11102313be88de1
%gometa
%global common_description %{expand:
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.
pflag is compatible with the GNU extensions to the POSIX recommendations for
command-line options.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Drop-in replacement for Go's flag package, implementing posix/gnu-style --flags
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pflag-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       golang-github-spf13-pflag-devel
Summary:        replacement for Go's flag package, implementing posix/gnu-style --flags
BuildArch:      noarch

%description -n golang-github-spf13-pflag-devel
Drop-in replacement for Go's flag package, implementing posix/gnu-style --flags

%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

# Workaround flag_test.go test with golang-1.18
sed -e 's/fmt.Println/fmt.Print/' -i flag_test.go

%install
%gopkginstall
%oreon_autofiles golang-github-spf13-pflag-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n golang-github-spf13-pflag-devel -f %{oreon_filedir}/golang-github-spf13-pflag-devel.list

%changelog

%autochangelog
