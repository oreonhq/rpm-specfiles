%global source0_hash bcc3dc4f136e2c4b166e834dcd1d3f003a1b8c4e71324963f4062edbcb3931c9
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/z
%global forgeurl        https://gitlab.com/cznic/z
Version:                1.7.4
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Zlib for Go without cgo.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Zlib for Go without cgo
License:        Zlib AND BSD-3-Clause AND Apache-2.0 AND BSD-4-Clause AND APSL-2.0 AND LGPL-2.1-or-later
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/z-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/z %{goipath}
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
