%global source0_hash 9a9447d9410b2615c05d4e8abb85aaaed344dfbfeb48b466699f8774c9b27297
%bcond check 0
%global goipath         github.com/leonelquinteros/gotext
Version:                1.7.2
%gometa
%global common_description %{expand:
Go (Golang) GNU gettext utilities package.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md\\\
                        cli/xgotext/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang GNU gettext utilities package
License:        MIT AND BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gotext-%{version}.tar.gz
Patch:          https://github.com/leonelquinteros/gotext/commit/0251497c92e4b8579ba7c7dbbce02ea90600f209.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1 -q

%build

for cmd in cli/xgotext; do
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
