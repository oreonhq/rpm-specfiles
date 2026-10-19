%global source0_hash 723ede1a61ca8311046f840020e485dec3ceb2e614d1a539cd154375bdd7b8cb
%bcond check 0
%global goipath         github.com/BurntSushi/toml
Version:                1.5.0
%gometa -L -f
%global common_description %{expand:
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library json and xml packages.
This package also supports the encoding.TextUnmarshaler and
encoding.TextMarshaler interfaces so that you can define custom data
representations.}
%global golicenses      COPYING
%global godocs          README.md
Name:           golang-github-burntsushi-toml
Release:        1%{?dist}
Summary:        TOML parser for Golang with reflection
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/toml-%{version}.tar.gz
Patch0:         0001-Encode-large-floats-as-exponent-syntax.patch
Patch1:         0002-Ensure-constant-format-strings-in-wf-calls.patch
Patch2:         0003-Ensure-constant-format-strings-in-runner.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
