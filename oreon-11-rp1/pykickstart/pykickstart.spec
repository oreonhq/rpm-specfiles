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
Source0:   https://github.com/pykickstart/%{name}/releases/download/r%{version}/%{name}-%{version}.tar.gz
%if %{with signed}
Source1:   https://github.com/pykickstart/%{name}/releases/download/r%{version}/%{name}-%{version}.tar.gz.asc
# oreon url source checksums begin
%global source0_sha256 49bbc8a51b43a071af9e89944248929a6f3c038731e1a868701dc939aab4dc57
%global source0_file pykickstart-3.69.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pykickstart-3.69.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "49bbc8a51b43a071af9e89944248929a6f3c038731e1a868701dc939aab4dc57" || { echo "oreon: Source0 SHA256 mismatch for pykickstart-3.69.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
