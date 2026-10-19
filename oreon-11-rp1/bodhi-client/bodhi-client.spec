%global source0_hash 3e10beb773fef5c45b8be44e016944bd48637a794a27ec81a2b629e16cf53b11
Name:           bodhi-client
Version:        26.4.0
Release:        1%{?dist}
Summary:        Bodhi client
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source0:        https://files.pythonhosted.org/packages/source/b/bodhi_client/bodhi_client-%{version}.tar.gz
BuildArch:      noarch
Requires: koji
Obsoletes: python3-bodhi-client <= 5.7.5
Obsoletes: bodhi <= 5.7.5
%py_provides python3-bodhi-client
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-bodhi-client = %{version}-%{release}
# /oreon:deps
%description
Command-line client for Bodhi, Fedora's update gating system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bodhi_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%make_build -C docs man
%install
%pyproject_install
install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/bodhi.1 %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm0644 bodhi-client.bash %{buildroot}%{_sysconfdir}/bash_completion.d/bodhi-client.bash
%oreon_autofiles main

%check

%pyproject_check_import
%{pytest} -v
%files

%changelog

%autochangelog
