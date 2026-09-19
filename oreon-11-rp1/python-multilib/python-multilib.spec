%global source0_hash 032e8c7251dabbf3d50101797f71a6944933751f52dc41f3ae93cfc76a46c371

Name:       python-multilib
Version:    1.3
Release:    6%{?dist}
Summary:    A module for determining if a package is multilib or not
License:    GPL-2.0-only
URL:        https://pagure.io/releng/python-multilib
Source0:    https://releases.pagure.org/releng/python-multilib/%{name}-%{version}.tar.bz2

BuildArch:  noarch

%global _description \
A Python module that supports several multilib "methods" useful for \
determining if a 32-bit package should be included with its 64-bit analogue \
in a compose.

%description %{_description}

%package conf
Summary:        Configuration files for %{name}

%description conf
This package provides the configuration files for %{name}.

%package -n python%{python3_pkgversion}-multilib
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}
Requires:       %{name}-conf = %{version}-%{release}

%description -n python%{python3_pkgversion}-multilib %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'
%{__install} -D -m 0644 etc/multilib.conf %{buildroot}%{_sysconfdir}/multilib.conf

%check
%pyproject_check_import

# testing requires complete composes available locally, which no buildsystem
# would ever want included in a build root
#{__python2} setup.py test
#{__python3} setup.py test

%files conf
%config(noreplace) %{_sysconfdir}/multilib.conf

%files -n python%{python3_pkgversion}-multilib -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
