%global source0_hash 780c67643126afe56f57fdc0f82b952d08e01a4df7eefaa929766dfb6edf6580
%{?python_enable_dependency_generator}
%global pkgname pymacaroons-pynacl
%global desc This is a Python re-implementation of the libmacaroons C library.\
Macaroons, like cookies, are a form of bearer credential. Unlike\
opaque tokens, macaroons embed caveats that define specific authorization\
requirements for the target service, the service that issued the root macaroon\
and which is capable of verifying the integrity of macaroons it receives.\
\
Macaroons allow for delegation and attenuation of authorization. They are\
simple and fast to verify, and decouple authorization policy from the\
enforcement of that policy.\
Name:           python-%{pkgname}
Version:        0.13.0
Release:        1%{?dist}
Summary:        Library providing non-opaque cookies for authorization
License:        MIT
URL:            https://github.com/ecordell/pymacaroons
Source0:        https://github.com/ecordell/pymacaroons/archive/v%{version}/pymacaroons-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
%{desc}

%package -n python3-%{pkgname}
Summary:        Library providing non-opaque cookies for authorization
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
%{desc}

%package doc
Summary: Documentation for python-pymacaroons-pynacl
BuildRequires:  python3-sphinx
%description doc
Documentation for the python-pymacaroons-pynacl package.

%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pymacaroons-%{version}
%oreon_prep
%build

%py3_build
make %{?_smp_mflags} -C docs SPHINXBUILD=sphinx-build-3 html PYTHONPATH=$(pwd)
rm docs/_build/html/.buildinfo
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pymacaroons-pynacl -f %{oreon_filedir}/python3-pymacaroons-pynacl.list
%files -n python-pymacaroons-pynacl-doc -f %{oreon_filedir}/python-pymacaroons-pynacl-doc.list

%changelog

%autochangelog
