%global source1_hash a5be30ddc4df21bf4335cf8930bebe37bd3d1dad96df44a3fbd2d76f65a27372
%global source0_hash efd2fcc0a7e6c1caaed77853275bec70f0d7829731531e0b80342492049e547e
%undefine __cmake_in_source_build
%bcond_without python2
%bcond_with static
%bcond_without python3
Name:       csdiff
Version:    3.5.6
Release:        1%{?dist}
Summary:        Non-interactive tools for processing code scan results in plain-text
License:    GPL-3.0-or-later
URL:        https://github.com/csutils/csdiff
Source0:        https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/csdiff/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:    kdudka.pgp
Conflicts:  csmock-plugin-shellcheck <= 2.5
Recommends: git-core
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-static
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-static
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  libstdc++-static
BuildRequires:  make
BuildRequires:  python2-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
This package contains the csdiff tool for comparing code scan defect lists in
order to find out added or fixed defects, and the csgrep utility for filtering
defect lists using various filtering predicates.

%if %{with static}
%package static
Summary:        Statically linked csgrep-static executable
BuildRequires:  boost-static
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
%py_provides    python3-%{name}
%description -n python3-%{name}
This package contains the Python 3 binding for the csdiff tool for comparing
code scan defect lists to find out added or fixed defects.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

make version.cc
%cmake                                   \
    -DCSGREP_STATIC=%{?with_static:ON}     \
    -DPYCSDIFF_PYTHON2=%{?with_python2:ON} \
    -DPYCSDIFF_PYTHON3=%{?with_python3:ON} \
    -DVERSION='%{name}-%{version}-%{release}'
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
