%global source0_hash efd2fcc0a7e6c1caaed77853275bec70f0d7829731531e0b80342492049e547e

# disable in source builds on EPEL <9
%undefine __cmake_in_source_build

# python2 is not available on RHEL > 7 and Fedora
%if 0%{?rhel} > 7 || 0%{?fedora}
%bcond_with python2
%else
%bcond_without python2
%endif

# build csdiff-static on 64bit RHEL-8+ and Fedora
%if 0%{?__isa_bits} == 64 && (0%{?rhel} > 7 || 0%{?fedora})
%bcond_without static
%else
%bcond_with static
%endif

# python3 support is optional
%bcond_without python3

Name:       csdiff
Version:    3.5.6
Release:    1%{?dist}
Summary:    Non-interactive tools for processing code scan results in plain-text

License:    GPL-3.0-or-later
URL:        https://github.com/csutils/csdiff
Source0:    https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

# the following upstream commit is needed to work with up2date csdiff/csgrep
# https://github.com/csutils/csmock/commit/48b09b3a
Conflicts:  csmock-plugin-shellcheck <= 2.5

# Use Boost 1.69 on EPEL 7
%if 0%{?rhel} == 7
BuildRequires: boost169-devel
%endif
# Use Boost 1.78 on EPEL 8 and 9
%if 0%{?rhel} == 8 || 0%{?rhel} == 9
BuildRequires: boost1.78-devel
%endif
# Use boost-devel everywhere else
%if 0%{?rhel} > 9 || 0%{?fedora}
BuildRequires: boost-devel
%endif

%if 0%{?rhel} == 7
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: help2man
BuildRequires: make

%if 0%{?rhel} == 7
Provides: bundled(boost_json)
Provides: bundled(boost_nowide)
%else
# needed for csfilter-kfp --kfp-git-url
Recommends: git-core
%endif

%description
This package contains the csdiff tool for comparing code scan defect lists in
order to find out added or fixed defects, and the csgrep utility for filtering
defect lists using various filtering predicates.

%if %{with static}
%package static
Summary:        Statically linked csgrep-static executable
%if 0%{?rhel} == 8 || 0%{?rhel} == 9
BuildRequires:  boost1.78-static
%else
BuildRequires:  boost-static
%endif
BuildRequires:  glibc-static
BuildRequires:  libstdc++-static

%description static
This pacakge contains a statically linked csgrep-static executable needed
for context embedding in legacy build environments.
%endif

%if %{with python2}
%package -n python2-%{name}
Summary:        Python interface to csdiff for Python 2
BuildRequires:  python2-devel
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package contains the Python 2 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        Python interface to csdiff for Python 3
BuildRequires:  python3-devel
%if 0%{?rhel} == 7
# fallback for epel7 buildroots with outdated RPM macros
%{?python_provide:%python_provide python3-%{name}}
%else
%py_provides    python3-%{name}
%endif

%description -n python3-%{name}
This package contains the Python 3 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%if 0%{?rhel} == 7
# Set paths for CMake's FindBoost
export BOOST_INCLUDEDIR=/usr/include/boost169
export BOOST_LIBRARYDIR=/usr/lib64/boost169
%endif
%if 0%{?rhel} == 8 || 0%{?rhel} == 9
# Set paths for CMake's FindBoost
export BOOST_INCLUDEDIR=/usr/include/boost1.78
export BOOST_LIBRARYDIR=/usr/lib64/boost1.78
%endif

make version.cc
%if 0%{?rhel} == 7
%cmake3                                  \
%else
%cmake                                   \
%endif
    -DCSGREP_STATIC=%{?with_static:ON}     \
    -DPYCSDIFF_PYTHON2=%{?with_python2:ON} \
    -DPYCSDIFF_PYTHON3=%{?with_python3:ON} \
    -DVERSION='%{name}-%{version}-%{release}'
%if 0%{?rhel} == 7
%cmake3_build
%else
%cmake_build
%endif

%install
%if 0%{?rhel} == 7
%cmake3_install
%else
%cmake_install
%endif

%check
%if 0%{?rhel} == 7
%ctest3
%else
%ctest
%endif

%files
%doc README
%license COPYING
%{_bindir}/csdiff
%{_bindir}/csfilter-kfp
%{_bindir}/csgrep
%{_bindir}/cshtml
%{_bindir}/cslinker
%{_bindir}/cssort
%{_bindir}/cstrans-df-run
%{_datadir}/%{name}
%{_mandir}/man1/csdiff.1*
%{_mandir}/man1/csfilter-kfp.1*
%{_mandir}/man1/csgrep.1*
%{_mandir}/man1/cshtml.1*
%{_mandir}/man1/cslinker.1*
%{_mandir}/man1/cssort.1*
%{_mandir}/man1/cstrans-df-run.1*

%if %{with static}
%files static
%{_libexecdir}/csgrep-static
%endif

%if %{with python2}
%files -n python2-%{name}
%license COPYING
%{python2_sitearch}/pycsdiff.so
%endif

%if %{with python3}
%files -n python3-%{name}
%license COPYING
%{python3_sitearch}/pycsdiff.so
%endif

%changelog
%autochangelog
