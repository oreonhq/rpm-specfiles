%global source0_hash 1f3cd884d110e10ebd1e166f767df6da2981b51db3692a9fe33a53df83376bbf
%bcond check 0
%global goipath         github.com/hickford/git-credential-azure
Version:                0.3.1
%gometa -f
%global goname git-credential-azure
%global common_description %{expand:
A Git credential helper for Azure Repos.}
%global golicenses      LICENSE.txt
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Git credential helper for Azure Repos
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
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

%gobuild -o %{gobuilddir}/bin/git-credential-azure %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp git-credential-azure.1 -t %{buildroot}%{_mandir}/man1
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
