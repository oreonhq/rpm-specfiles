%global source0_hash c5d3f4195b3456e210da63cc23ef88f42a5b771643e47ef79b8f6b067e662abe

%global desc \
The KIWI boxed plugin provides support for self contained building \
of images based on fast booting VM images.

%global srcname kiwi_boxed_plugin

Name:           kiwi-boxed-plugin
Version:        0.2.58
Release:        1%{?dist}
URL:            https://github.com/OSInside/kiwi-boxed-plugin
Summary:        KIWI - Boxed Build Plugin
License:        GPL-3.0-or-later
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# doc build requirements
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

Requires:       python3-%{name} = %{version}-%{release}
Supplements:    (kiwi-cli and qemu-kvm)
Provides:       %{srcname} = %{version}-%{release}

BuildArch:      noarch

%description %{desc}

%package -n python3-%{name}
Summary:        KIWI - Boxed Build Plugin - Python 3 implementation
Supplements:    (python%{python3_version}dist(kiwi) and qemu-kvm)
Requires:       qemu-kvm
Provides:       python3-%{srcname} = %{version}-%{release}

%description -n python3-%{name} %{desc}

This package provides the Python 3 library plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# Temporarily switch things back to docopt for everything but Fedora 41+
# FIXME: Drop this hack as soon as we can...
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
sed -e 's/docopt-ng.*/docopt = ">=0.6.2"/' -i pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build man pages
make -C doc man

%install
%pyproject_install

# Install documentation
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install

# Delete this now, we'll docify later
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/LICENSE
rm -f %{buildroot}%{_defaultdocdir}/python-%{srcname}/README

%files
%doc README.rst
%{_mandir}/man8/*.8*

%files -n python3-%{name}
%license LICENSE
%{python3_sitelib}/%{srcname}*

%changelog
%autochangelog
