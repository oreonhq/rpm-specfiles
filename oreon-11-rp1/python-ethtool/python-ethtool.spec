%global source0_hash 567260ea5805063bbcff71dabd6fb820f89bc84f720e9ebe315c7eef1449d908
%bcond_with tests
%global pypi_name ethtool
Name:           python-%{pypi_name}
Version:        0.15
Release:        16%{?dist}
Summary:        Python module to interface with ethtool
License:        GPL-2.0-only
URL:            https://github.com/fedora-python/%{name}
Source0:        https://files.pythonhosted.org/packages/source/e/ethtool/ethtool-0.15.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  libnl3-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Python bindings for the ethtool kernel interface, that allows querying and
changing of Ethernet card settings, such as speed, port, auto-negotiation, and
PCI locations.

%package -n     python3-%{pypi_name}
Summary:        Python module to interface with ethtool
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
Python 3 bindings for the ethtool kernel interface, that allows querying and
changing of Ethernet card settings, such as speed, port, auto-negotiation, and
PCI locations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
a2x -d manpage -f manpage man/pethtool.8.asciidoc
a2x -d manpage -f manpage man/pifconfig.8.asciidoc
%install
%py3_install
%if "%{_sbindir}" != "%{_bindir}"
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}{%{_bindir},%{_sbindir}}/pifconfig
mv %{buildroot}{%{_bindir},%{_sbindir}}/pethtool
%endif
mkdir -p %{buildroot}%{_mandir}/man8/
cp -p man/*.8 %{buildroot}%{_mandir}/man8/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{__python3} tests/parse_ifconfig.py -v
%{__python3}  -m unittest discover -v
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-ethtool -f %{oreon_filedir}/python3-ethtool.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15-16
- Prepare for Oreon 11 (RP1)
