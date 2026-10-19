%global source0_hash 277f4d91be4efcf83cf03665d505eda2686e892ad5c26b6e82601705083df0ba
%bcond check 0
%global goipath         github.com/crossdock/crossdock-go
%global commit          049aabb0122b03bc9bd30cab8f3f91fb60166361
%gometa
%global common_description %{expand:
A Go client for Crossdock.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go client for Crossdock
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/crossdock-go-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in _codegen; do
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
