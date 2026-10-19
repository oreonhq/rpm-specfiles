%global source0_hash 10b012cf403a76dcad5c9df230db4dfa17c4027b7eeb77daeeccf84b7890a1af
Name:           python-datalad
Version:        1.6.3
Release:        1%{?dist}
Summary:        Distributed system for joint management of code, data, and their relationship
License:        MIT
URL:            https://www.datalad.org
Source0:        https://files.pythonhosted.org/packages/source/d/datalad/datalad-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 59.0.0
BuildRequires:  python3dist(typing-extensions) >= 4.0.0
Requires:       python3-datalad = %{version}-%{release}
# /oreon:deps
%package -n       python3-datalad+downloaders-extra
Summary:        Metapackage for python3-datalad downloaders-extra extras
Requires:       python3-datalad = %{version}-%{release}
Provides:       python3dist(datalad[downloaders-extra]) = %{version}-%{release}

%description -n python3-datalad+downloaders-extra
Metapackage for python3-datalad downloaders-extra extras.

%package -n       python3-datalad+misc
Summary:        Metapackage for python3-datalad misc extras
Requires:       python3-datalad = %{version}-%{release}
Requires:       python3dist(argcomplete) >= 1.12.3
Provides:       python3dist(datalad[misc]) = %{version}-%{release}

%description -n python3-datalad+misc
Metapackage for python3-datalad misc extras.

%package -n       python3-datalad+tests
Summary:        Metapackage for python3-datalad tests extras
Requires:       python3-datalad = %{version}-%{release}
Requires:       python3dist(httpretty) >= 0.9.4
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest-fail-slow) >= 0.2
Provides:       python3dist(datalad[tests]) = %{version}-%{release}

%description -n python3-datalad+tests
Metapackage for python3-datalad tests extras.

%package -n       python3-datalad+duecredit
Summary:        Metapackage for python3-datalad duecredit extras
Requires:       python3-datalad = %{version}-%{release}
Provides:       python3dist(datalad[duecredit]) = %{version}-%{release}

%description -n python3-datalad+duecredit
Metapackage for python3-datalad duecredit extras.

%package -n       python3-datalad+full
Summary:        Metapackage for python3-datalad full extras
Requires:       python3-datalad = %{version}-%{release}
Provides:       python3dist(datalad[full]) = %{version}-%{release}

%description -n python3-datalad+full
Metapackage for python3-datalad full extras.

%package -n       python3-datalad+devel-docs
Summary:        Metapackage for python3-datalad devel-docs extras
Requires:       python3-datalad = %{version}-%{release}
Requires:       python3dist(sphinx) >= 4.3.0
Requires:       python3dist(sphinx-rtd-theme) >= 0.5.1
Provides:       python3dist(datalad[devel-docs]) = %{version}-%{release}

%description -n python3-datalad+devel-docs
Metapackage for python3-datalad devel-docs extras.

%package -n       python3-datalad+devel-utils
Summary:        Metapackage for python3-datalad devel-utils extras
Requires:       python3-datalad = %{version}-%{release}
Requires:       python3dist(coverage)
Provides:       python3dist(datalad[devel-utils]) = %{version}-%{release}

%description -n python3-datalad+devel-utils
Metapackage for python3-datalad devel-utils extras.

%package -n       python3-datalad+devel
Summary:        Metapackage for python3-datalad devel extras
Requires:       python3-datalad = %{version}-%{release}
Provides:       python3dist(datalad[devel]) = %{version}-%{release}

%description -n python3-datalad+devel
Metapackage for python3-datalad devel extras.

%description

%package -n     python3-datalad
Summary:        Distributed system for joint management of code, data, and their relationship
# oreon:reqs
Requires:       python3dist(chardet) >= 3.0.4
Requires:       python3dist(fasteners) >= 0.14
Requires:       python3dist(keyring) >= 20.0
Requires:       python3dist(patool) >= 1.7
Requires:       python3dist(requests) >= 1.2
Requires:       python3dist(tqdm) >= 4.32.0
Requires:       python3dist(typing-extensions) >= 4.0.0
# /oreon:reqs
%description -n python3-datalad

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir datalad-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-datalad usr/lib/python3*/site-packages/datalad* usr/lib64/python3*/site-packages/datalad* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/datalad* usr/lib64/python3*/site-packages/datalad* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-datalad -f %{oreon_filedir}/python3-datalad.list

%changelog

%autochangelog
