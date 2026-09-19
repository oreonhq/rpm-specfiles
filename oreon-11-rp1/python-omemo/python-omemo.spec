%global source0_hash 49fb4597996dc0b4cc4fa2696a77b9e3c5af601e2f83462e811d0683d182635d

Name:           python-omemo
Version:        2.1.0
Release:        1%{?dist}
Summary:        Python implementation of the OMEMO Encryption protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source:         https://github.com/Syndace/%{name}/archive/v%{version}/python-omemo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
#BuildRequires:  python3-pytest

%description
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.

%package     -n python3-omemo
Summary:        Python implementation of the OMEMO Encryption protocol

%description -n  python3-omemo
This python library offers an open implementation of the OMEMO
Multi-End Message and Object Encryption protocol.

OMEMO is an extension of the XMPP protocol defined as XEP-0384. It
provides multi-end to multi-end encryption, allowing messages to be
synchronized securely across multiple clients, even if some of them
are offline.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
# cli package needs newer version of python-prettytable
# https://bugzilla.redhat.com/show_bug.cgi?id=2435941
%pyproject_buildrequires
#-x omemo,cli

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l omemo

%check
# Checking import of all submodules requires newer version of prettytable
# https://bugzilla.redhat.com/show_bug.cgi?id=2435941
%pyproject_check_import -t
# tests requires python-oldmemo-backend-signal, that introduce cyclic
# dependancy: Disabling.

%files -n python3-omemo -f %{pyproject_files}

%changelog
%autochangelog
