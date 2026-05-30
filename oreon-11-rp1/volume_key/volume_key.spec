%global source0_hash 6ca3748fc1dad22c450bbf6601d4e706cb11c5e662d11bb4aeb473a9cd77309b

# Define `python3_sitearch' if there is no one:
%{!?python3_sitearch:%global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

# Enable Python 3 in Fedora and RHEL > 7 as default:
%if 0%{?fedora} || 0%{?rhel} > 7
# Add `--without python3' option (enable python3 by default):
%bcond_without python3
%else
# Add `--with python3' option (disable python3 by default):
%bcond_with python3
%endif

# Drop Python 2 in Fedora >= 30 and RHEL > 7 as default:
%if 0%{?fedora} >= 30 || 0%{?rhel} > 7
%global drop_python2 1
%global configure_with_python2 no
%else
# Define `python2_sitearch' if there is no one:
%{!?python2_sitearch:%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%global configure_with_python2 yes
%endif

%if %{with python3}
%global configure_with_python3 yes
%else
%global configure_with_python3 no
%endif

# Additional configure options:
%global with_pythons --with-python=%{configure_with_python2} --with-python3=%{?configure_with_python3}

Summary: An utility for manipulating storage encryption keys and passphrases
Name: volume_key
Version: 0.3.12
Release: 30%{?dist}
License: GPL-2.0-only AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL: https://pagure.io/%{name}/
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.xz
# Support all LUKS devices
# - backport of 26c09768662d8958debe8c9410dae9fda02292c3
Patch0: volume_key-0.3.12-support_LUKS2_and_more.patch
# Fix resource leaks
# - backport of bf6618ec0b09b4e51fc97fa021e687fbd87599ba
Patch1: volume_key-0.3.12-fix_resource_leaks.patch
BuildRequires: autoconf, automake, libtool
BuildRequires: make
BuildRequires: gcc
BuildRequires: cryptsetup-devel, gettext-devel, glib2-devel, /usr/bin/gpg2
BuildRequires: gpgme-devel, libblkid-devel, nss-devel
BuildRequires: python3-devel, python3-setuptools
%if 0%{?drop_python2} < 1
BuildRequires: python2-devel
%endif
# Needed by %%check:
BuildRequires: nss-tools

%global desc_common The main goal of the software is to allow restoring access to an encrypted\
hard drive if the primary user forgets the passphrase.  The encryption key\
back up can also be useful for extracting data after a hardware or software\
failure that corrupts the header of the encrypted volume, or to access the\
company data after an employee leaves abruptly.

%global desc_app This package provides a command-line tool for manipulating storage volume\
encryption keys and storing them separately from volumes.\
\
%{desc_common}

%global desc_lib This package provides lib%{name}, a library for manipulating storage volume\
encryption keys and storing them separately from volumes.\
\
%{desc_common}

%global desc_python(V:) This package provides %{-V:Python %{-V*}}%{!-V:Python} bindings for lib%{name}, a library for\
manipulating storage volume encryption keys and storing them separately from\
volumes.\
\
%{desc_common}\
\
%{name} currently supports only the LUKS volume encryption format.  Support\
for other formats is possible, some formats are planned for future releases.

%description
%{desc_app}

%package devel
Summary: A library for manipulating storage encryption keys and passphrases
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{desc_lib}

%package libs
Summary: A library for manipulating storage encryption keys and passphrases
Requires: /usr/bin/gpg2

%description libs
%{desc_lib}

%if 0%{?drop_python2} < 1
%package -n python2-%{name}
%{?python_provide:%python_provide python2-%{name}}
Summary: Python bindings for lib%{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python2-%{name}
%desc_python
%endif

%if %{with python3}
%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary: Python 3 bindings for lib%{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
%desc_python -V 3
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1
%patch -P1 -p1
autoreconf -fiv

%build
%configure %{?with_pythons}
%make_build

%install
%make_install

# Remove libtool archive
find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

%check
make check || { \
echo "======================== ./test-suite.log ========================"; \
cat ./test-suite.log; \
echo "=================================================================="; \
exit 1; \
}

%ldconfig_scriptlets libs

%files
%doc README contrib
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files libs -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/lib%{name}.so.*

%if 0%{?drop_python2} < 1
%files -n python2-%{name}
%{python2_sitearch}/_%{name}.so
%{python2_sitearch}/%{name}.py*
%endif

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/_%{name}.so
%{python3_sitearch}/%{name}.py*
%{python3_sitearch}/__pycache__/%{name}.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.12-30
- Prepare for Oreon 11 (RP1)
