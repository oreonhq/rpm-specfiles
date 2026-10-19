%global source0_hash 405332595ffe256fb1d2e8311798de44d5e1a54883331d15484c2d6cc8446af2
%if 0%{?oreon} || 0%{?rhel} || 0%{?fedora}
%bcond_with tests
%else
%bcond tests 1
%endif
%bcond cython_compile 1
Name:           Cython
Version:        3.3.0
Release:        1%{?dist}
Summary:        Language for writing Python extension modules
License:        Apache-2.0
URL:            http://www.cython.org
Source0:        https://github.com/cython/cython/archive/refs/tags/%{version}.tar.gz#/Cython-%{version}.tar.gz
%if %{with tests}
%endif
%if %{with cython_compile}
%else
BuildArch:      noarch
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-Cython = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-cython
Summary:        Language for writing Python extension modules
Provides:       Cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       Cython%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cython%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%py_provides    python3-Cython
Provides:       python3dist(Cython) = %{version}
Obsoletes:      python3-Cython < 3~~
Provides:       bundled(python3dist(tempita))
%description -n python3-cython

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cython-%{version}
%oreon_prep
%build

%pyproject_wheel %{!?with_cython_compile:-C--global-option=--no-cython-compile}
%install
%pyproject_install
%oreon_autofiles python3-cython usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%if 0%{?__isa_bits} < 64
export CFLAGS="${CFLAGS} -g1"
%endif
%{python3} runtests.py -vv --no-pyregr %{?_smp_mflags} \
  --exclude 'run.pstats_profile_test*' \
  %ifarch %{ix86}
  --exclude run.parallel \
  --exclude run.numpy_parallel \
  %endif
%endif
%files
%files -n python3-cython -f %{oreon_filedir}/python3-cython.list

%changelog

%autochangelog
