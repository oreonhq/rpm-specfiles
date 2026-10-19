%global source0_hash b185acc9bbb80f371e811a79391eb3303d11be6e0e73cd117161c8e7c54ac380
Name:           python-slixmpp-omemo
Version:        2.2.0
Release:        1%{?dist}
Summary:        OMEMO plugin for Slixmpp
License:        AGPL-3.0-only
URL:            https://github.com/Syndace/slixmpp-omemo
Source0:        https://files.pythonhosted.org/packages/source/s/slixmpp_omemo/slixmpp_omemo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-slixmpp-omemo = %{version}-%{release}
# /oreon:deps
%package -n       python3-slixmpp-omemo+docs
Summary:        Metapackage for python3-slixmpp-omemo docs extras
Requires:       python3-slixmpp-omemo = %{version}-%{release}
Provides:       python3dist(slixmpp-omemo[docs]) = %{version}-%{release}

%description -n python3-slixmpp-omemo+docs
Metapackage for python3-slixmpp-omemo docs extras.

%package -n       python3-slixmpp-omemo+test
Summary:        Metapackage for python3-slixmpp-omemo test extras
Requires:       python3-slixmpp-omemo = %{version}-%{release}
Provides:       python3dist(slixmpp-omemo[test]) = %{version}-%{release}

%description -n python3-slixmpp-omemo+test
Metapackage for python3-slixmpp-omemo test extras.

%package -n       python3-slixmpp-omemo+lint
Summary:        Metapackage for python3-slixmpp-omemo lint extras
Requires:       python3-slixmpp-omemo = %{version}-%{release}
Provides:       python3dist(slixmpp-omemo[lint]) = %{version}-%{release}

%description -n python3-slixmpp-omemo+lint
Metapackage for python3-slixmpp-omemo lint extras.

%package -n       python3-slixmpp-omemo+dev
Summary:        Metapackage for python3-slixmpp-omemo dev extras
Requires:       python3-slixmpp-omemo = %{version}-%{release}
Provides:       python3dist(slixmpp-omemo[dev]) = %{version}-%{release}

%description -n python3-slixmpp-omemo+dev
Metapackage for python3-slixmpp-omemo dev extras.

%description

%package -n     python3-slixmpp-omemo
Summary:        OMEMO plugin for Slixmpp
# oreon:reqs
Requires:       python3dist(oldmemo[xml]) < 3
Requires:       python3dist(oldmemo[xml]) >= 2.0.0
Requires:       python3dist(omemo) < 3
Requires:       python3dist(omemo) >= 2.0.0
Requires:       python3dist(slixmpp) < 2
Requires:       python3dist(slixmpp) >= 1.8.0
Requires:       python3dist(twomemo[xml]) < 3
Requires:       python3dist(twomemo[xml]) >= 2.0.0
Requires:       python3dist(typing-extensions) >= 4.4.0
# /oreon:reqs
%description -n python3-slixmpp-omemo

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir slixmpp_omemo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-slixmpp-omemo usr/lib/python3*/site-packages/slixmpp_omemo* usr/lib64/python3*/site-packages/slixmpp_omemo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/slixmpp_omemo* usr/lib64/python3*/site-packages/slixmpp_omemo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-slixmpp-omemo -f %{oreon_filedir}/python3-slixmpp-omemo.list

%changelog

%autochangelog
