%global source0_hash 1256ad3907bceb4fcee7ed40d17c5726f8b602eea900e94500ba3352e96febbc
%bcond check 1
%global goipath         oss.terrastruct.com/d2
%global forgeurl        https://github.com/terrastruct/d2
Version:                0.9.0
%gometa -L -f
%global common_description %{expand:
D2 is a modern diagram scripting language that turns text to diagrams.}
Name:           d2
Release:        1%{?dist}
Summary:        Modern diagram scripting language that turns text to diagrams
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND FTL AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with check}
%endif
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

%gobuild -o %{gobuilddir}/bin/d2 %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 ci/release/template/man/d2.1
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck -t oss.terrastruct.com/d2/d2cli -t e2etests-cli
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
