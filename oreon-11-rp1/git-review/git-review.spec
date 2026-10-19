%global source0_hash 0633ae1cb874d2dae70b2b3a13a245c24c3b6726c5452f9a63fee21733ee5cd6
Name:		git-review
Version:	2.3.1
Release:        15%{?dist}
Summary:        A Git helper for integration with Gerrit
License:	Apache-2.0
URL:		https://opendev.org/opendev/git-review
Source0:        git-review-%{version}.tar.gz
BuildArch:	noarch
Requires:	git-core
Requires:	python3-requests
Requires:	python3-setuptools
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# /oreon:deps
%description
An extension for source control system Git that creates and manages
review requests in the patch management system Gerrit. It replaces the
rfc.sh script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%py3_build
sed -i 's/\r//' LICENSE
%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 0644 -D git-review.1 %{buildroot}%{_mandir}/man1/git-review.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
