%global source0_hash 7a85d9c72c36848529fe43e1d89651ceb64552221141025dbdb775b785f2375c
%bcond check 0
%global goipath         github.com/chmouel/clipman
Version:                1.7.0
%gometa -L -f
%global common_description %{expand:
A basic clipboard manager for Wayland, with support for persisting copy buffers
after an application exits.}
%global golicenses      COPYING
%global godocs          docs CHANGELOG.md CONTRIBUTING.md README.md
Name:           clipman
Release:        1%{?dist}
Summary:        A simple clipboard manager for Wayland
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       wl-clipboard >= 2.0
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/clipman %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0644 -vpD docs/clipman.1  -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
