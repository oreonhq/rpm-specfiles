%global source0_hash 49bbc8a51b43a071af9e89944248929a6f3c038731e1a868701dc939aab4dc57

# Enable tests by default. To disable them use:
#     rpmbuild -ba --without runtests pykickstart.spec
%bcond_without runtests
%bcond_with signed

Name:      pykickstart
Version:   3.69
Release:   1%{?dist}
License:   GPL-2.0-only
Summary:   Python utilities for manipulating kickstart files.
Url:       http://fedoraproject.org/wiki/pykickstart
Source0:        https://github.com/pykickstart/pykickstart/releases/download/r3.69/pykickstart-3.69.tar.gz
%if %{with signed}
Source1:        https://github.com/pykickstart/pykickstart/releases/download/r3.69/pykickstart-3.69.tar.gz.asc
%endif

BuildArch: noarch

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-requests
BuildRequires: python3-setuptools
BuildRequires: make
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-pytest-cov

# Only required when building with runtests
%if %{with runtests}
BuildRequires: python3-sphinx
%endif

Requires: python3-kickstart = %{version}-%{release}

%description
Python utilities for manipulating kickstart files.

%package -n python3-kickstart
Summary:  Python 3 library for manipulating kickstart files.
Requires: python3-requests

%description -n python3-kickstart
Python 3 library for manipulating kickstart files.  The binaries are found in
the pykickstart package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
make PYTHON=%{__python3}

%install
make PYTHON=%{__python3} DESTDIR=%{buildroot} install

%check
%if %{with runtests}
LC_ALL=C make PYTHON=%{__python3} test-no-coverage
%endif

%files
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
%{_bindir}/ksshell
%{_mandir}/man1/ksflatten.1.gz
%{_mandir}/man1/ksshell.1.gz
%{_mandir}/man1/ksvalidator.1.gz
%{_mandir}/man1/ksverdiff.1.gz

%files -n python3-kickstart
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python3_sitelib}/pykickstart
%{python3_sitelib}/pykickstart-%{version}.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.69-1
- Prepare for Oreon 11 (RP1)
