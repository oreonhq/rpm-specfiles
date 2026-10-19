%global source0_hash 49fb4597996dc0b4cc4fa2696a77b9e3c5af601e2f83462e811d0683d182635d
Name:           python-omemo
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python implementation of the OMEMO Encryption protocol
License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/python-omemo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-omemo = %{version}-%{release}
# /oreon:deps
%package -n       python3-omemo+cli
Summary:        Metapackage for python3-omemo cli extras
Requires:       python3-omemo = %{version}-%{release}
Requires:       python3dist(prettytable) >= 3.16.0
Requires:       python3dist(prettytable) < 4
Provides:       python3dist(omemo[cli]) = %{version}-%{release}

%description -n python3-omemo+cli
Metapackage for python3-omemo cli extras.

%package -n       python3-omemo+docs
Summary:        Metapackage for python3-omemo docs extras
Requires:       python3-omemo = %{version}-%{release}
Provides:       python3dist(omemo[docs]) = %{version}-%{release}

%description -n python3-omemo+docs
Metapackage for python3-omemo docs extras.

%package -n       python3-omemo+test
Summary:        Metapackage for python3-omemo test extras
Requires:       python3-omemo = %{version}-%{release}
Provides:       python3dist(omemo[test]) = %{version}-%{release}

%description -n python3-omemo+test
Metapackage for python3-omemo test extras.

%package -n       python3-omemo+lint
Summary:        Metapackage for python3-omemo lint extras
Requires:       python3-omemo = %{version}-%{release}
Provides:       python3dist(omemo[lint]) = %{version}-%{release}

%description -n python3-omemo+lint
Metapackage for python3-omemo lint extras.

%package -n       python3-omemo+dev
Summary:        Metapackage for python3-omemo dev extras
Requires:       python3-omemo = %{version}-%{release}
Provides:       python3dist(omemo[dev]) = %{version}-%{release}

%description -n python3-omemo+dev
Metapackage for python3-omemo dev extras.

%description
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.

%package     -n python3-omemo
Summary:        Python implementation of the OMEMO Encryption protocol
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.3.0
Requires:       python3dist(xeddsa) < 2
Requires:       python3dist(xeddsa) >= 1.0.0
# /oreon:reqs
%description -n  python3-omemo
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-omemo usr/lib/python3*/site-packages/omemo* usr/lib64/python3*/site-packages/omemo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/omemo* usr/lib64/python3*/site-packages/omemo* usr/bin/*

%check

%pyproject_check_import -t
%files
%files -n python3-omemo -f %{oreon_filedir}/python3-omemo.list

%changelog

%autochangelog
