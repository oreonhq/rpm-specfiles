%global source0_hash 520c18bde521c37ac73c8e53190aa8bdac299ae9af0c4624d0a6ca198785a739
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         aead.dev/minisign
%global forgeurl        https://github.com/aead/minisign
Version:                0.3.0
%gometa -L -f
%global common_description %{expand:
A dead simple tool to sign files and verify digital signatures.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-aead-minisign
Release:        1%{?dist}
Summary:        A dead simple tool to sign files and verify digital signatures
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/minisign-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%build

%gobuild -o %{gobuilddir}/bin/go-minisign %{goipath}/cmd/minisign
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
