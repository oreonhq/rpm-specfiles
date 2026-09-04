%global source0_hash 3ff6a8f4caf006f19c8340c55a1224ed10629747d9498316b6941f2d3a4509d1

%global commit 4194967f02db8e9f85e8bab6f3803029a4d9a243
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           koan
Version:        3.3.1
Release:        1%{?dist}
Summary:        Kickstart over a network

License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/koan
Source0:        https://github.com/cobbler/koan/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python%{python3_pkgversion}-koan = %{version}-%{release}

%description
Koan stands for kickstart-over-a-network and allows for both network
installation of new virtualized guests and reinstallation of an existing
system. For use with a boot-server configured with Cobbler.

%package -n python%{python3_pkgversion}-koan
Summary:        koan python%{python3_pkgversion} module
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       virt-install

%description -n python%{python3_pkgversion}-koan
koan python%{python3_pkgversion} module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%py3_shebang_fix bin

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l koan

%files
%license COPYING
%doc README.md
%{_bindir}/koan
%{_bindir}/cobbler-register

%files -n python%{python3_pkgversion}-koan -f %{pyproject_files}

%changelog
%autochangelog
