%global source0_hash d7bb392de6c9b6eedd23e5e05e7cd730822afa02b85ca6a69c9313638a945a24
%bcond check 0
%global goipath         github.com/pelletier/go-toml/v2
Version:                2.2.4
%gometa
%global common_description %{expand:
Go library for the TOML file format.}
%global golicenses      LICENSE
%global godocs          SECURITY.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for the TOML file format
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/pelletier/go-toml/archive/v%{version}/go-toml-%{version}.tar.gz
Patch1:         go-toml-2.2.4-const-format-strings.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

for cmd in cmd/{jsontoml,tomljson,tomll} ; do
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
