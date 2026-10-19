%global source0_hash e1f33e9f8810b3b2977f4495f1236509ad5d456711d351ac844915389c64b25e
Name:           python-rpmautospec
Version:        0.8.5
Release:        1%{?dist}
Summary:        A package and CLI tool to generate RPM release fields and changelogs.
License:        MIT AND GPL-2.0-only WITH GCC-exception-2.0 AND (MIT OR GPL-2.0-or-later WITH GCC-exception-2.0)
URL:            https://github.com/fedora-infra/rpmautospec
Source0:        https://files.pythonhosted.org/packages/source/r/rpmautospec/rpmautospec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rpmautospec = %{version}-%{release}
# /oreon:deps
%package -n       python3-rpmautospec+click
Summary:        Metapackage for python3-rpmautospec click extras
Requires:       python3-rpmautospec = %{version}-%{release}
Requires:       python3dist(click) < 9
Requires:       python3dist(click) >= 8
Provides:       python3dist(rpmautospec[click]) = %{version}-%{release}

%description -n python3-rpmautospec+click
Metapackage for python3-rpmautospec click extras.

%package -n       python3-rpmautospec+pygit2
Summary:        Metapackage for python3-rpmautospec pygit2 extras
Requires:       python3-rpmautospec = %{version}-%{release}
Requires:       python3dist(pygit2) < 1.20.1
Requires:       python3dist(pygit2) >= 1.4.0
Requires:       python3dist(pygit2) < 2.0.0
Provides:       python3dist(rpmautospec[pygit2]) = %{version}-%{release}

%description -n python3-rpmautospec+pygit2
Metapackage for python3-rpmautospec pygit2 extras.

%package -n       python3-rpmautospec+rpm
Summary:        Metapackage for python3-rpmautospec rpm extras
Requires:       python3-rpmautospec = %{version}-%{release}
Provides:       python3dist(rpmautospec[rpm]) = %{version}-%{release}

%description -n python3-rpmautospec+rpm
Metapackage for python3-rpmautospec rpm extras.

%package -n       python3-rpmautospec+norpm
Summary:        Metapackage for python3-rpmautospec norpm extras
Requires:       python3-rpmautospec = %{version}-%{release}
Requires:       python3dist(norpm) < 2
Requires:       python3dist(norpm) >= 1.6
Provides:       python3dist(rpmautospec[norpm]) = %{version}-%{release}

%description -n python3-rpmautospec+norpm
Metapackage for python3-rpmautospec norpm extras.

%package -n       python3-rpmautospec+all
Summary:        Metapackage for python3-rpmautospec all extras
Requires:       python3-rpmautospec = %{version}-%{release}
Requires:       python3dist(click) < 9
Requires:       python3dist(click) >= 8
Requires:       python3dist(pygit2) < 1.20.1
Requires:       python3dist(pygit2) >= 1.4.0
Requires:       python3dist(pygit2) < 2.0.0
Requires:       python3dist(norpm) < 2
Requires:       python3dist(norpm) >= 1.6
Provides:       python3dist(rpmautospec[all]) = %{version}-%{release}

%description -n python3-rpmautospec+all
Metapackage for python3-rpmautospec all extras.

%description

%package -n     python3-rpmautospec
Summary:        A package and CLI tool to generate RPM release fields and changelogs.
# oreon:reqs
Requires:       python3dist(rpmautospec-core) < 1.0.0
Requires:       python3dist(rpmautospec-core) >= 0.1.4
# /oreon:reqs
%description -n python3-rpmautospec

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rpmautospec-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rpmautospec usr/lib/python3*/site-packages/rpmautospec* usr/lib64/python3*/site-packages/rpmautospec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rpmautospec* usr/lib64/python3*/site-packages/rpmautospec* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rpmautospec -f %{oreon_filedir}/python3-rpmautospec.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.3-0
- Prepare for Oreon 11 (RP1)
