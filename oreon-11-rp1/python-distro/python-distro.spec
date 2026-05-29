%global source0_hash 6ede051357868ed427ea71d16fc27f4d63cc0d9c8a32788aa11c450ecefcc76f

%global pypi_name distro

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        11%{?dist}
Summary:        Linux Distribution - a Linux OS platform information API

License:        Apache-2.0
URL:            https://github.com/python-distro/distro
Source0:        https://github.com/python-distro/distro/archive/v1.9.0/distro-1.9.0.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
 
%global _description \
The distro (for: Linux Distribution) package provides information about the\
Linux distribution it runs on, such as a reliable machine-readable ID, or\
version information.\
\
It is a renewed alternative implementation for Python's original\
platform.linux_distribution function, but it also provides much more\
functionality. An alternative implementation became necessary because\
Python 3.5 deprecated this function, and Python 3.7 is expected to remove it\
altogether. Its predecessor function platform.dist was already deprecated since\
Python 2.6 and is also expected to be removed in Python 3.7. Still, there are\
many cases in which access to that information is needed. See Python issue 1322\
for more information.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} || (0%{?oreon} >= 11)
Suggests:       /usr/bin/lsb_release
%endif

%description -n python3-%{pypi_name} %{_description}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTORS.md README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%{_bindir}/distro

%check
%pytest

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.0-11
- Import
